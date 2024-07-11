import os

import pandas as pd
import torch

import futureframe as ff
import research.models.cm2
from futureframe.utils import save_or_append_to_csv


def run(
    model_name="cm2",
    benchmark_name="openmlcc18",
    batch_size=256,
    num_epochs=100,
    num_eval=25,
    patience=10,
    lr=1e-3,
    seed=42,
):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    config = research.models.cm2.get_tiny_config()
    model = research.models.cm2.CM2ForFineTuning(config, freeze_backbone=False)
    model.to(device)
    trainable, non_trainable = ff.utils.get_num_parameters(model)
    print(f"{trainable=}, {non_trainable=}")
    benchmark = ff.benchmarks.openmlb.ModifOpenMLCC18Benchmark(csv_results_name="run_benchmark.csv")
    results = benchmark.run(
        model, batch_size=batch_size, seed=seed, num_epochs=num_epochs, num_eval=num_eval, patience=patience, lr=lr
    )

    for res in results:
        res["model"] = model_name
        res["benchmark"] = benchmark_name
        res["lr"] = lr

    results = pd.DataFrame(results)
    print(results.to_markdown())

    # save results to csv
    save_or_append_to_csv(results, os.path.join(ff.config.RESULTS_ROOT, "run_benchmark_script.csv"))


if __name__ == "__main__":
    from fire import Fire

    Fire(run)
