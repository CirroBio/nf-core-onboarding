#!/usr/bin/env python3
"""Cirro preprocess: build the workflow input samplesheet from the dataset."""
import pandas as pd
from cirro.helpers.preprocess_dataset import PreprocessDataset


def main() -> None:
    ds = PreprocessDataset.from_running()
    # Generic "Files" dataset has no pivot-able samplesheet; build one from
    # ds.files (a DataFrame with columns sample/file, plus read=1/2 when Cirro
    # detected R1/R2). Pair reads into fastq_1/fastq_2 so paired-end pipelines
    # work; fall back to sorted paths when no read column is present.
    files = ds.files.copy()
    if "read" in files.columns:
        sheet = (
            files.pivot_table(index="sample", columns="read", values="file", aggfunc="first")
            .rename(columns={1: "fastq_1", 2: "fastq_2", "1": "fastq_1", "2": "fastq_2"})
            .reset_index()
        )
        sheet.columns.name = None
    else:
        rows = []
        for sample, group in files.groupby("sample"):
            paths = sorted(group["file"].dropna().astype(str))
            rows.append({
                "sample": sample,
                "fastq_1": paths[0] if paths else "",
                "fastq_2": paths[1] if len(paths) > 1 else "",
            })
        sheet = pd.DataFrame(rows)
    if "fastq_2" not in sheet.columns:
        sheet["fastq_2"] = ""
    sheet["fastq_2"] = sheet["fastq_2"].fillna("")
    sheet[["sample", "fastq_1", "fastq_2"]].to_csv("samplesheet.csv", index=False)
    ds.add_param("input", "samplesheet.csv")


if __name__ == "__main__":
    main()
