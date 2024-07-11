import logging
from enum import Enum
from pathlib import Path
from typing import Dict, Optional, Tuple, Union

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
from torch import Tensor, nn
from transformers import (
    AutoModel,
    AutoTokenizer,
    EarlyStoppingCallback,
    PretrainedConfig,
    PreTrainedModel,
    Trainer,
    TrainingArguments,
)
from transformers.activations import ACT2FN
from transformers.models.bert.modeling_bert import BertEncoder, BertPooler

from futureframe.config import PRETRAINED_MODELS_ROOT
from futureframe.data_types import ColumnDtype, ValueDtype, valuedtype_to_columndtype
from futureframe.features import from_flat_indices_to_column_idx, prepare_df
from futureframe.models.base import finetuning_loss
from futureframe.tabular_datasets import FeatureDataset, SupervisedDataset
from futureframe.utils import freeze, unfreeze

log = logging.getLogger(__name__)


########
# Config
########
class FFPreTrainedConfig(PretrainedConfig):
    model_type = "ff"

    def __init__(
        self,
        pretrained_text_encoder_name="BAAI/bge-small-en-v1.5",
        pretrained_root=PRETRAINED_MODELS_ROOT,
        numerical_transformation="quantile",
        add_pooling_layer=True,
        #
        hidden_size=768,
        num_hidden_layers=12,
        num_attention_heads=12,
        intermediate_size=3072,
        hidden_act="gelu",
        hidden_dropout_prob=0.1,
        attention_probs_dropout_prob=0.1,
        max_position_embeddings=1024,
        initializer_range=0.02,
        layer_norm_eps=1e-12,
        _attn_implementation="eager",  # TODO: support sdpa
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.pretrained_text_encoder_name = pretrained_text_encoder_name
        self.pretrained_root = pretrained_root
        self.numerical_transformation = numerical_transformation
        self.add_pooling_layer = add_pooling_layer
        #
        self.hidden_size = hidden_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.hidden_act = hidden_act
        self.intermediate_size = intermediate_size
        self.hidden_dropout_prob = hidden_dropout_prob
        self.attention_probs_dropout_prob = attention_probs_dropout_prob
        self.initializer_range = initializer_range
        self.layer_norm_eps = layer_norm_eps
        self.max_position_embeddings = max_position_embeddings
        self._attn_implementation = _attn_implementation

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items()}


class FFFineTunedConfig(FFPreTrainedConfig):
    def __init__(
        self,
        num_classes: int,
        head_type: str,
        #
        pretrained_text_encoder_name="BAAI/bge-small-en-v1.5",
        pretrained_root=PRETRAINED_MODELS_ROOT,
        numerical_transformation="quantile",
        add_pooling_layer=True,
        #
        hidden_size=768,
        num_hidden_layers=12,
        num_attention_heads=12,
        intermediate_size=3072,
        hidden_act="gelu",
        hidden_dropout_prob=0.1,
        attention_probs_dropout_prob=0.1,
        max_position_embeddings=512,
        initializer_range=0.02,
        layer_norm_eps=1e-12,
        _attn_implementation="eager",
    ):
        super().__init__(
            pretrained_text_encoder_name,
            pretrained_root,
            numerical_transformation,
            add_pooling_layer,
            hidden_size,
            num_hidden_layers,
            num_attention_heads,
            intermediate_size,
            hidden_act,
            hidden_dropout_prob,
            attention_probs_dropout_prob,
            max_position_embeddings,
            initializer_range,
            layer_norm_eps,
            _attn_implementation,
        )

        self.num_classes = num_classes
        self.head_type = head_type


def get_tiny_config():
    """0.5M parameters"""
    return FFPreTrainedConfig(hidden_size=128, num_hidden_layers=2, num_attention_heads=2, intermediate_size=512)


def get_mini_config():
    """3.5M parameters"""
    return FFPreTrainedConfig(hidden_size=256, num_hidden_layers=4, num_attention_heads=4, intermediate_size=1024)


def get_small_config():
    """10M parameters"""
    return FFPreTrainedConfig(hidden_size=512, num_hidden_layers=4, num_attention_heads=4, intermediate_size=1024)


def get_medium_config():
    """26M parameters"""
    return FFPreTrainedConfig(hidden_size=512, num_hidden_layers=8, num_attention_heads=8, intermediate_size=2048)


def get_base_config():
    """88M parameters"""
    return FFPreTrainedConfig(hidden_size=768, num_hidden_layers=12, num_attention_heads=12, intermediate_size=3072)


def get_large_config():
    """306M parameters"""
    return FFPreTrainedConfig(hidden_size=1024, num_hidden_layers=24, num_attention_heads=16, intermediate_size=4096)


def get_xlarge_config():
    """609M parameters"""
    return FFPreTrainedConfig(hidden_size=1024, num_hidden_layers=48, num_attention_heads=16, intermediate_size=4096)


###########
# Tokenizer
###########
class FFTokenizer:
    def __init__(self, config: FFPreTrainedConfig, download: bool = False) -> None:
        self.config = config
        self.download = download

        self.numerical_transformer = None
        self.categorical_columns = []
        self.numerical_columns = []

        if download:
            self.text_tokenizer = AutoTokenizer.from_pretrained(config.pretrained_text_encoder_name)
            self.text_tokenizer.save_pretrained(
                Path(config.pretrained_root) / config.model_type / config.pretrained_text_encoder_name
            )
        else:
            self.text_tokenizer = AutoTokenizer.from_pretrained(
                Path(config.pretrained_root) / config.model_type / config.pretrained_text_encoder_name
            )

    @property
    def special_text_tokens(self):
        # '[UNK]', '[SEP]', '[PAD]', '[CLS]', '[MASK]'
        return self.text_tokenizer.special_tokens_map

    @property
    def special_text_tokens_ids(self):
        return self.text_tokenizer.convert_tokens_to_ids(self.special_text_tokens.values())

    def _tokenize(self, x):
        # log.debug(f"Tokenizing {x}")
        if len(x) == 0:
            return {
                "input_ids": torch.tensor([], dtype=torch.long).reshape(0, 0),
                "token_type_ids": torch.tensor([], dtype=torch.long).reshape(0, 0),
                "attention_mask": torch.tensor([], dtype=torch.long).reshape(0, 0),
            }

        out = self.text_tokenizer.batch_encode_plus(
            x,
            return_tensors="pt",
            padding=True,
            truncation=True,
            # add_special_tokens=False,
            max_length=self.config.max_position_embeddings // 4,  # 128
        )
        out = {k: v for k, v in out.items()}
        return out

    def fit(self, x: pd.DataFrame):
        prepared = prepare_df(x)
        self.numerical_columns = prepared["numerical_columns"]
        self.numerical_transformer = prepared["numerical_transformer"]

    def __call__(self, x: pd.DataFrame):
        out = prepare_df(x, numerical_transformation_name=self.config.numerical_transformation)

        columns = out["columns"]
        columns_dtypes = out["columns_dtypes"]
        shape = out["shape"]
        values = out["values"]
        values_dtypes = out["values_dtypes"]

        columns_inputs = self._tokenize(columns)
        columns_dtypes_inputs = torch.tensor(
            [list(map(ColumnDtype.name_to_value, columns_dtypes))], dtype=torch.long
        ).view(-1, 1)
        # values_dtypes_inputs = torch.tensor([list(map(ValueDtype.name_to_value, values_dtypes))], dtype=torch.long)

        text_indices = np.where(values_dtypes != "float")[0]
        text_values = {}
        if text_indices.any():
            text_values = self._tokenize(values[text_indices].tolist())

        # empty tensor if no numerical values
        float_indices = np.where(values_dtypes == "float")[0]
        float_values = torch.tensor(values[float_indices].astype(float), dtype=torch.float32).view(-1, 1)

        text_col_map = from_flat_indices_to_column_idx(text_indices, columns)
        text_idx_col_map = torch.from_numpy(
            np.concatenate([text_indices.reshape(-1, 1), text_col_map.reshape(-1, 1)], axis=1),
        ).to(dtype=torch.long)

        float_col_map = from_flat_indices_to_column_idx(float_indices, columns)
        float_idx_col_map = torch.from_numpy(
            np.concatenate([float_indices.reshape(-1, 1), float_col_map.reshape(-1, 1)], axis=1)
        ).to(dtype=torch.long)

        return {
            "columns_inputs": columns_inputs,
            "columns_dtypes_inputs": columns_dtypes_inputs,
            "categorical_values_inputs": text_values,
            "categorical_values_indices": text_idx_col_map,
            "numerical_values_inputs": float_values,
            "numerical_values_indices": float_idx_col_map,
            "shape": shape,
            "attention_mask": None,
        }

    def encode(self, df: pd.DataFrame):
        assert len(df) == 1
        keys = df.columns
        shape = df.shape
        values = df.values.flatten()

        columns_inputs = self._tokenize(keys.tolist())
        columns_indices = torch.arange(len(keys), dtype=torch.long).view(-1, 1)

        dtypes = np.array([ValueDtype.convert_dtype(v) for v in values])
        columns_dtypes_inputs = np.array(list(map(valuedtype_to_columndtype, dtypes)))
        columns_dtypes_inputs = torch.tensor([v.value for v in columns_dtypes_inputs], dtype=torch.long).view(-1, 1)
        assert columns_dtypes_inputs.shape[0] == len(values)

        text_indices = np.where(dtypes != ValueDtype.FLOAT)[0]
        text_values = {
            "input_ids": torch.tensor([], dtype=torch.long).reshape(0, 0),
            "attention_mask": torch.tensor([], dtype=torch.long).reshape(0, 0),
            "token_type_ids": torch.tensor([], dtype=torch.long).reshape(0, 0),
        }
        if text_indices.any():
            text_values = self._tokenize(values[text_indices].astype(str).tolist())
        text_indices = torch.tensor(text_indices, dtype=torch.long).view(-1, 1)
        text_col_map = from_flat_indices_to_column_idx(text_indices[:, 0], keys)
        text_col_map = torch.from_numpy(text_col_map).to(dtype=torch.long).view(-1, 1)
        text_indices = torch.cat([text_indices, text_col_map], dim=1)

        float_indices = np.where(dtypes == ValueDtype.FLOAT)[0]
        float_values = torch.tensor(values[float_indices].astype(float), dtype=torch.float32).view(-1, 1)
        float_indices = torch.tensor(float_indices, dtype=torch.long).view(-1, 1)
        float_col_map = from_flat_indices_to_column_idx(float_indices[:, 0], keys)
        float_col_map = torch.from_numpy(float_col_map).to(dtype=torch.long).view(-1, 1)
        float_indices = torch.cat([float_indices, float_col_map], dim=1)

        return {
            "columns_inputs": columns_inputs,
            "columns_indices": columns_indices,
            "columns_dtypes_inputs": columns_dtypes_inputs,
            "categorical_values_inputs": text_values,
            "categorical_values_indices": text_indices,
            "numerical_values_inputs": float_values,
            "numerical_values_indices": float_indices,
            "shape": shape,
        }

    def encode_plus(self, keys, values, dtypes, mapping, shapes):
        columns_inputs = self._tokenize(keys)

        dtypes = np.array(dtypes)
        values = np.array(values)

        numerical_values_indices = np.where(dtypes == "float")[0]
        numerical_values = values[numerical_values_indices].astype(float)
        numerical_values_inputs = torch.tensor(numerical_values, dtype=torch.float32).view(-1, 1)

        categorical_values_indices = np.where(dtypes != "float")[0]
        non_numerical_values = values[categorical_values_indices].astype(str).tolist()
        categorical_values_inputs = self._tokenize(non_numerical_values)

        columns_dtypes_inputs = torch.tensor(
            list(map(lambda x: valuedtype_to_columndtype(ValueDtype.get(x)).value, dtypes)), dtype=torch.long
        )
        mapping = torch.tensor(mapping, dtype=torch.long)
        numerical_values_indices = torch.tensor(numerical_values_indices, dtype=torch.long)
        categorical_values_indices = torch.tensor(categorical_values_indices, dtype=torch.long)

        return dict(
            columns_inputs=columns_inputs,
            columns_dtypes_inputs=columns_dtypes_inputs,
            numerical_values_indices=numerical_values_indices,
            numerical_values_inputs=numerical_values_inputs,
            categorical_values_indices=categorical_values_indices,
            categorical_values_inputs=categorical_values_inputs,
            mapping=mapping,
            shapes=shapes,
        )


#################
# Feature Encoder
#################
class FFTextEncoder(nn.Module):
    """Uses a text encoding model to encode the column name of a table cell."""

    def __init__(self, config: FFPreTrainedConfig, download: bool = False) -> None:
        super().__init__()
        self.config = config
        self.download = download

        if download:
            self.embeddings = AutoModel.from_pretrained(config.pretrained_text_encoder_name)
            self.embeddings.save_pretrained(
                Path(config.pretrained_root) / config.model_type / config.pretrained_text_encoder_name
            )
        else:
            self.embeddings = AutoModel.from_pretrained(
                Path(config.pretrained_root) / config.model_type / config.pretrained_text_encoder_name
            )
        freeze(self.embeddings)

        self.orig_hidden_size = self.embeddings.config.hidden_size
        self.dim_adapter = nn.Linear(self.orig_hidden_size, config.hidden_size)
        freeze(self.dim_adapter)
        if isinstance(config.hidden_act, str):
            self.transform_act_fn = ACT2FN[config.hidden_act]
        else:
            self.transform_act_fn = config.hidden_act
        self.ln = nn.LayerNorm(config.hidden_size, eps=config.layer_norm_eps)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)

    def forward(
        self,
        input_ids: Optional[torch.Tensor] = None,
        attention_mask: Optional[torch.Tensor] = None,
        token_type_ids: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.Tensor] = None,
        head_mask: Optional[torch.Tensor] = None,
        inputs_embeds: Optional[torch.Tensor] = None,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: Optional[bool] = None,
    ):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        outputs = self.embeddings(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        # Could have extracted the orig here, but would have to know the dim in advance
        pooled_output = outputs[1]
        pooled_output = self.dim_adapter(pooled_output)
        orig = pooled_output.detach().clone()
        pooled_output = self.transform_act_fn(pooled_output)
        pooled_output = self.ln(pooled_output)
        pooled_output = self.dropout(pooled_output)
        return pooled_output, orig


class FFNumericalEncoder(nn.Module):
    def __init__(self, config: FFPreTrainedConfig) -> None:
        super().__init__()
        self.config = config

        self.dim_adapter = nn.Linear(1, config.hidden_size)
        if isinstance(config.hidden_act, str):
            self.transform_act_fn = ACT2FN[config.hidden_act]
        else:
            self.transform_act_fn = config.hidden_act
        self.ln = nn.LayerNorm(config.hidden_size, eps=config.layer_norm_eps)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)

    def forward(self, x: Tensor):
        x = self.dim_adapter(x)
        orig = x.detach().clone()
        x = self.transform_act_fn(x)
        x = self.ln(x)
        x = self.dropout(x)
        return x, orig


class FFValueTypeEncoder(nn.Module):
    def __init__(self, config: FFPreTrainedConfig) -> None:
        super().__init__()
        self.config = config
        self.embedding = nn.Embedding(16, config.hidden_size)

    def forward(self, x: Tensor):
        return self.embedding(x).squeeze()


class FuseLayer(nn.Module):
    def __init__(self, config: FFPreTrainedConfig) -> None:
        super().__init__()
        self.config = config

        self.fc1 = nn.Linear(config.hidden_size, config.hidden_size)
        self.fc2 = nn.Linear(config.hidden_size, 1, bias=False)

    def forward(self, col_emb: Tensor, dtype_emb: Tensor):
        g = torch.sigmoid(self.fc2(torch.relu(self.fc1(dtype_emb))))
        x = (1 - g) * col_emb + g * dtype_emb
        return x


class LinkingLayer(nn.Module):
    def __init__(self, config: FFPreTrainedConfig) -> None:
        super().__init__()
        self.config = config

        self.fc1 = nn.Linear(config.hidden_size, config.hidden_size)
        self.fc2 = nn.Linear(config.hidden_size, 1, bias=False)

    def forward(self, col_dtype_emb: Tensor, val_emb: Tensor):
        g = torch.sigmoid(self.fc2(torch.relu(self.fc1(col_dtype_emb))))
        x = val_emb + g * col_dtype_emb
        return x


class FFFeatureEncoder(nn.Module):
    def __init__(self, config) -> None:
        super().__init__()
        self.config = config

        self.col_embedding = FFTextEncoder(config)
        self.col_dtype_embedding = FFValueTypeEncoder(config)

        self.cat_val_embedding = self.col_embedding  # share parameters
        self.num_val_embedding = FFNumericalEncoder(config)

        self.col_dtype_fuse = FuseLayer(config)

        self.num_link = LinkingLayer(config)
        self.cat_link = LinkingLayer(config)

        self.mask_token = nn.Parameter(torch.randn(config.hidden_size))
        self.pad_token = nn.Parameter(torch.zeros(config.hidden_size))

    def mask_strategy(self, x, p_mask):
        mask = torch.rand(x.shape[0]).to(x.device) < p_mask
        # assure at least one token is masked
        if not mask.any() and x.shape[0] > 0 and p_mask > 0:
            mask[torch.randint(0, x.shape[0], (1,)).to(mask.device)] = True
        return mask

    def forward(
        self,
        columns_inputs,
        columns_dtypes_inputs,
        numerical_values_indices,
        numerical_values_inputs,
        categorical_values_indices,
        categorical_values_inputs,
        mapping,
        shapes,
        p_mask: float = 0,
        **kwargs,
    ):
        assert all([c[1] == shapes[0][1] for c in shapes]), "Padding not yet supported"
        num_cols = shapes[0][1]

        # Embed column names with text encoder
        col_emb, _ = self.col_embedding(**columns_inputs)  # ncols x dim

        # Broadcast col_emb to match the shape of the mapping
        col_emb = col_emb[mapping]  # nvals x dim
        assert col_emb.shape[0] == mapping.shape[0]

        # Embed value dtypes with value type encoder
        col_dtype_emb = self.col_dtype_embedding(columns_dtypes_inputs.view(-1, 1))  # nvals x dim

        # Embed numerical values with numerical encoder
        num_val_emb, orig_num = self.num_val_embedding(numerical_values_inputs.view(-1, 1))  # nnumvals x dim

        # Embed categorical values with text encoder
        cat_val_emb, orig_cat = (
            torch.tensor([], device=col_emb.device).reshape(0, col_emb.shape[1]),
            torch.tensor([], device=col_emb.device).reshape(0, col_emb.shape[1]),
        )
        if len(categorical_values_inputs["input_ids"]) > 0:
            cat_val_emb, orig_cat = self.cat_val_embedding(**categorical_values_inputs)

        # Mask values
        cat_mask = self.mask_strategy(cat_val_emb, p_mask)
        if cat_mask.any():
            cat_val_emb[cat_mask] = self.mask_token

        num_mask = self.mask_strategy(num_val_emb, p_mask)
        if num_mask.any():
            num_val_emb[num_mask] = self.mask_token

        # Fuse column and dtype embeddings
        col_dtype_fused_emb = self.col_dtype_fuse(col_emb, col_dtype_emb)  # nvals x dim

        # Link value embeddings with fused embeddings
        cat_dtype_col_emb = col_dtype_fused_emb[columns_dtypes_inputs != 2]
        cat_dtype_col_val_emb = self.cat_link(cat_dtype_col_emb, cat_val_emb)  # ncatvals x dim

        num_dtype_col_emb = col_dtype_fused_emb[columns_dtypes_inputs == 2]
        num_dtype_col_val_emb = self.num_link(num_dtype_col_emb, num_val_emb)  # nnumvals x dim

        # Group inputs and labels in the original sequence
        indices = torch.cat([categorical_values_indices, numerical_values_indices], dim=0)
        sorting_indices = torch.argsort(indices).to(col_emb.device)
        # (ncatvals + nnumvals) x dim
        x = torch.cat([cat_dtype_col_val_emb, num_dtype_col_val_emb], dim=0)[sorting_indices]

        mask = torch.cat([cat_mask, num_mask], dim=0)[sorting_indices]
        # labels = torch.cat([orig_cat, orig_num], dim=0)[sorting_indices]  # TODO: unify training objective

        assert x.shape[0] == mapping.shape[0]
        x = x.reshape(-1, num_cols, x.shape[-1])
        mask = mask.reshape(-1, num_cols)

        return x, mask, orig_cat, orig_num


#######
# Model
#######
class FFPreTrainedModel(PreTrainedModel):
    def _init_weights(self, module):
        """Initialize the weights"""
        if isinstance(module, nn.Linear):
            module.weight.data.normal_(mean=0.0, std=self.config.initializer_range)
            if module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.Embedding):
            module.weight.data.normal_(mean=0.0, std=self.config.initializer_range)
            if module.padding_idx is not None:
                module.weight.data[module.padding_idx].zero_()
        elif isinstance(module, nn.LayerNorm):
            module.bias.data.zero_()
            module.weight.data.fill_(1.0)


class FFModel(FFPreTrainedModel):
    def __init__(self, config: FFPreTrainedConfig):
        super().__init__(config)
        self.config = config
        self.add_pooling_layer = config.add_pooling_layer

        self.embeddings = FFFeatureEncoder(config)
        self.cls_token = nn.Parameter(torch.randn(config.hidden_size))
        self.encoder = BertEncoder(config)
        self.pooler = BertPooler(config) if self.add_pooling_layer else None

        self.attn_implementation = config._attn_implementation

        # Initialize weights and apply final processing
        self.post_init()

    def forward(
        self,
        columns_inputs,
        columns_dtypes_inputs,
        numerical_values_indices,
        numerical_values_inputs,
        categorical_values_indices,
        categorical_values_inputs,
        mapping,
        shapes,
        p_mask: float = 0,
        attention_mask: Optional[torch.Tensor] = None,
        head_mask: Optional[torch.Tensor] = None,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: Optional[bool] = None,
        **kwargs,
    ) -> Union[Tuple[Tensor], Dict[str, Tensor]]:
        embedding_output, mask_token_mask, orig_cat, orig_num = self.embeddings(
            columns_inputs=columns_inputs,
            columns_dtypes_inputs=columns_dtypes_inputs,
            categorical_values_inputs=categorical_values_inputs,
            categorical_values_indices=categorical_values_indices,
            numerical_values_inputs=numerical_values_inputs,
            numerical_values_indices=numerical_values_indices,
            mapping=mapping,
            shapes=shapes,
            p_mask=p_mask,
        )

        # broadcast cls token on the first dim
        final_shape = embedding_output.shape
        cls_token = self.cls_token.expand(final_shape[0], 1, -1)
        embedding_output = torch.cat([cls_token, embedding_output], dim=1)
        # cls_token_mask = torch.tensor([False], device=mask_token_mask.device).expand(final_shape[0], 1)
        # mask_token_mask = torch.cat([cls_token_mask, mask_token_mask], dim=1)

        batch_size, seq_length, hidden_size = embedding_output.size()
        device = embedding_output.device

        if attention_mask is None:
            attention_mask = torch.ones((batch_size, seq_length), device=device)
        else:
            attention_mask = attention_mask.view(batch_size, seq_length - 1)
            attention_mask = torch.cat([torch.ones((batch_size, 1), device=device), attention_mask], dim=1)
        # attention_mask = attention_mask.to(dtype=next(self.parameters()).dtype)  # fp16 compatibility

        input_shape = (batch_size, seq_length, hidden_size)
        extended_attention_mask = self.get_extended_attention_mask(attention_mask, input_shape)
        head_mask = self.get_head_mask(head_mask, self.config.num_hidden_layers)

        encoder_outputs = self.encoder(
            embedding_output,
            attention_mask=extended_attention_mask,
            head_mask=head_mask,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        sequence_output = encoder_outputs[0]

        pooled_output = self.pooler(sequence_output) if self.pooler is not None else None

        if not return_dict:
            return (sequence_output, pooled_output, mask_token_mask, orig_cat, orig_num) + encoder_outputs[1:]

        return dict(
            last_hidden_state=sequence_output,
            pooler_output=pooled_output,
            mask_token_mask=mask_token_mask,
            orig_cat=orig_cat,
            orig_num=orig_num,
            past_key_values=encoder_outputs.past_key_values,
            hidden_states=encoder_outputs.hidden_states,
            attentions=encoder_outputs.attentions,
            cross_attentions=encoder_outputs.cross_attentions,
        )


#############
# Pretraining
#############
# class SiluAdapter(nn.Module):
#     def __init__(self, hidden_size: int = 4096) -> None:
#         super().__init__()
#         self.norm = RMSNorm(hidden_size)
#         self.linear1 = nn.Linear(hidden_size, hidden_size, bias=False)
#         self.linear2 = nn.Linear(hidden_size, hidden_size, bias=False)
#         torch.nn.init.zeros_(self.linear1.weight)
#         torch.nn.init.zeros_(self.linear2.weight)
#
#     def forward(self, x: torch.Tensor) -> torch.Tensor:
#         return self.norm(x + self.linear2(F.silu(self.linear1(x))))


class PreTrainingHeadTransform(nn.Module):
    def __init__(self, config: FFPreTrainedConfig):
        super().__init__()
        # self.dense = nn.Linear(config.hidden_size, config.hidden_size, bias=False)
        # if isinstance(config.hidden_act, str):
        #     self.transform_act_fn = ACT2FN[config.hidden_act]
        # else:
        #     self.transform_act_fn = config.hidden_act
        self.ln = nn.LayerNorm(config.hidden_size, eps=config.layer_norm_eps)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x = self.dense(x)
        # x = self.transform_act_fn(x)
        x = self.ln(x)
        x = self.dropout(x)
        return x


class PreTrainingHeadForMaskedNumericalValues(nn.Module):
    # MSE Objective
    def __init__(self, config: FFPreTrainedConfig) -> None:
        super().__init__()
        self.config = config

        self.transform = PreTrainingHeadTransform(config)
        self.fc = nn.Linear(config.hidden_size, config.hidden_size, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.transform(x)
        x = self.fc(x)
        x = F.normalize(x, p=2, dim=-1)
        return x


class PreTrainingHeadForMaskedCategoricalValues(nn.Module):
    # Cos sim objective - l2 norm
    def __init__(self, config: FFPreTrainedConfig) -> None:
        super().__init__()
        self.config = config

        self.transform = PreTrainingHeadTransform(config)
        self.fc = nn.Linear(config.hidden_size, config.hidden_size, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.transform(x)
        x = self.fc(x)
        x = F.normalize(x, p=2, dim=-1)
        return x


class PreTrainingHead(nn.Module):
    def __init__(
        self,
        config: FFPreTrainedConfig,
        numerical_head_cls=PreTrainingHeadForMaskedNumericalValues,
        categorical_head_cls=PreTrainingHeadForMaskedCategoricalValues,
    ) -> None:
        super().__init__()
        self.config = config

        self.numerical_head = numerical_head_cls(config)
        self.categorical_head = categorical_head_cls(config)

    def forward(self, num_sequence_output, cat_sequence_output, pooled_output):
        num_output = self.numerical_head(num_sequence_output)
        cat_output = self.categorical_head(cat_sequence_output)
        return num_output, cat_output


class FFForPreTraining(FFPreTrainedModel):
    def __init__(self, config: FFPreTrainedConfig) -> None:
        super().__init__(config)
        self.config = config

        self.backbone = FFModel(config)
        self.head = PreTrainingHead(config)

        self.num_criterion = nn.CosineEmbeddingLoss(reduction="none")
        self.cat_criterion = nn.CosineEmbeddingLoss(reduction="none")

        self.post_init()

    def forward(
        self,
        columns_inputs,
        columns_dtypes_inputs,
        numerical_values_indices,
        numerical_values_inputs,
        categorical_values_indices,
        categorical_values_inputs,
        mapping,
        shapes,
        p_mask: float = 0.3,
        attention_mask: Optional[torch.Tensor] = None,
        head_mask: Optional[torch.Tensor] = None,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: Optional[bool] = None,
        **kwargs,
    ):
        outputs = self.backbone(
            columns_inputs=columns_inputs,
            columns_dtypes_inputs=columns_dtypes_inputs,
            categorical_values_inputs=categorical_values_inputs,
            categorical_values_indices=categorical_values_indices,
            numerical_values_inputs=numerical_values_inputs,
            numerical_values_indices=numerical_values_indices,
            p_mask=p_mask,
            attention_mask=attention_mask,
            mapping=mapping,
            shapes=shapes,
            head_mask=head_mask,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=False,
        )
        sequence_output, pooled_output, mask_token_mask, cat_true, num_true = outputs[:5]

        mask_token_mask = mask_token_mask.view(-1)

        # Remove CLS token
        sequence_output = sequence_output[:, 1:, :]
        sequence_output = sequence_output.reshape(-1, self.config.hidden_size)

        # get only masked values
        num_sequence_output = sequence_output[numerical_values_indices]
        num_sequence_output = num_sequence_output[mask_token_mask[numerical_values_indices]]
        num_true = num_true[mask_token_mask[numerical_values_indices]]

        cat_sequence_output = sequence_output[categorical_values_indices]
        cat_sequence_output = cat_sequence_output[mask_token_mask[categorical_values_indices]]
        cat_true = cat_true[mask_token_mask[categorical_values_indices]]

        num_pred, cat_pred = self.head(
            num_sequence_output=num_sequence_output,
            cat_sequence_output=cat_sequence_output,
            pooled_output=pooled_output,
        )

        num_loss = torch.tensor(0, device=num_true.device).float()
        if num_true.shape[0] > 0:
            target = torch.ones(num_true.shape[0], device=cat_true.device)
            num_loss = self.num_criterion(num_pred, num_true, target)
            if num_loss.isnan().any():
                log.warning(f"Num loss is NaN: {num_loss=}, {num_pred=}, {num_true=}")

        # Original bert vector is the input
        cat_loss = torch.tensor(0, device=cat_true.device).float()
        if cat_true.shape[0] > 0:
            target = torch.ones(cat_true.shape[0], device=cat_true.device)
            cat_loss = self.cat_criterion(cat_pred, cat_true, target)
            if cat_loss.isnan().any():
                log.warning(f"Cat loss is NaN: {cat_loss=}, {cat_pred=}, {cat_true=}")

        loss = 0.5 * (num_loss + cat_loss)

        if not return_dict:
            return loss, num_loss, cat_loss

        return dict(loss=loss, num_loss=num_loss, cat_loss=cat_loss)


############
# Finetuning
############
class FineTuningLinearHead(nn.Module):
    def __init__(self, config: FFPreTrainedConfig, num_classes: int) -> None:
        super().__init__()
        self.config = config
        self.num_classes = num_classes

        self.fc = nn.Linear(config.hidden_size, num_classes)

    def forward(self, x: Tensor):
        x = self.fc(x)
        return x


class FineTuningNonLinearHead(nn.Module):
    def __init__(self, config: FFPreTrainedConfig, num_classes: int) -> None:
        super().__init__()
        self.config = config
        self.num_classes = num_classes

        self.fc1 = nn.Linear(config.hidden_size, config.hidden_size)
        self.act_fn = nn.GELU()
        self.fc2 = nn.Linear(config.hidden_size, num_classes)

    def forward(self, x: Tensor):
        x = self.fc1(x)
        x = self.act_fn(x)
        x = self.fc2(x)
        return x


class HeadTypes(Enum):
    LINEAR = FineTuningLinearHead
    NON_LINEAR = FineTuningNonLinearHead


def get_head_cls(head: str):
    head = head.upper()
    return HeadTypes[head].value


class FFForFineTuning(FFPreTrainedModel):
    def __init__(
        self,
        head_type: str,
        config: FFPreTrainedConfig,
        freeze_backbone=True,
        pretrained_ckpt_path: Optional[str] = None,
        backbone=None,
    ) -> None:
        super().__init__(config)
        self.config = config
        self.freeze_backbone = freeze_backbone
        self.head_type = head_type
        self.pretrained_ckpt_path = pretrained_ckpt_path

        if self.pretrained_ckpt_path is not None:
            self.backbone = FFModel.from_pretrained(self.pretrained_ckpt_path)
        elif backbone is not None:
            self.backbone = backbone
        else:
            raise ValueError("Either config or backbone must be provided")

        self.head = None
        self.trainer = None

        if self.freeze_backbone:
            freeze(self.backbone)

    def forward(self, x: Tensor, y: Tensor | None = None):
        assert self.head is not None, "Head must be initialized first"
        assert isinstance(self.backbone, FFModel), "Backbone must be initialized first"

        x = self.backbone(x)
        x = x[:, 0, :]  # take the cls token embedding
        x = self.head(x)

        if y is None:
            return x

        return x, finetuning_loss(x, y, self.num_classes)

    def finetune(
        self,
        X_train,
        y_train,
        head="linear",
        freeze_backbone=True,
        early_stopping_patience=3,
    ):
        self.train()
        if freeze_backbone:
            freeze(self.backbone)
        else:
            self.freeze_backbone = False
            unfreeze(self.backbone)

        y_train, num_classes = prepare_target(y_train)
        self.head = get_head_cls(head)(self.config, num_classes)

        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1)

        train_dataset = SupervisedDataset(X_train, y_train, self.tokenizer)
        eval_dataset = SupervisedDataset(X_val, y_val, self.tokenizer)

        training_args = TrainingArguments(
            output_dir="test_trainer",
            eval_strategy="epoch",
            load_best_model_at_end=True,
        )
        early_stopping = EarlyStoppingCallback(early_stopping_patience=early_stopping_patience)
        self.trainer = Trainer(
            model=self,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            # compute_metrics=compute_metrics,
            # data_collator=...,
            callbacks=[
                early_stopping,
            ],
        )
        self.trainer.train()

        return self

    def predict(self, X):
        assert self.head is not None, "Head must be initialized first"
        assert isinstance(self.backbone, FFModel), "Backbone must be initialized first"
        assert self.trainer is not None, "Model must be finetuned first"

        self.eval()
        dataset = FeatureDataset(X)
        predictions = self.trainer.predict(dataset, metric_key_prefix="eval")

        # dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=4)
        #
        # predictions = torch.zeros(len(dataset), self.num_classes)
        # idx = 0
        # for batch in dataloader:
        #     pred = self(batch)
        #     batch_s = len(batch)
        #     predictions[idx : idx + batch_s] = pred
        #     idx += batch_s

        return predictions

    # TODO: test how from_pretrained works


if __name__ == "__main__":
    config = get_xlarge_config()
    model = FFModel(config)
    num_parameters = sum(p.numel() for p in model.parameters())
    print(num_parameters)
