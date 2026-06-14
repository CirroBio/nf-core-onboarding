#!/usr/bin/env python3
"""Cirro preprocess: build the workflow input samplesheet from the dataset."""
import pandas as pd
from cirro.helpers.preprocess_dataset import PreprocessDataset


def main() -> None:
    ds = PreprocessDataset.from_running()
    # Generic "Files" dataset has no pivot-able samplesheet; build one from
    # ds.files defensively — Cirro's column names and read encodings vary across
    # ingest shapes, so resolve them at runtime and pair R1/R2 into fastq_1/2.
    files = ds.files.copy()
    ds.logger.info(f"[preprocess] ds.files columns: {list(files.columns)}")
    sample_col = "sample" if "sample" in files.columns else (
        "sampleName" if "sampleName" in files.columns else files.columns[0])
    file_col = next(
        (c for c in ("file", "path", "relativePath", "dataPath") if c in files.columns),
        files.columns[-1])
    read_col = next((c for c in ("read", "readType", "read_type") if c in files.columns), None)
    _R1 = {1, 1.0, "1", "R1", "r1", "READ1", "read1"}
    _R2 = {2, 2.0, "2", "R2", "r2", "READ2", "read2"}
    if read_col is not None:
        sheet = files.pivot_table(
            index=sample_col, columns=read_col, values=file_col, aggfunc="first"
        ).reset_index()
        sheet.columns.name = None
        rename = {c: ("fastq_1" if c in _R1 else "fastq_2") for c in sheet.columns
                  if c in _R1 or c in _R2}
        sheet = sheet.rename(columns=rename)
    else:
        rows = []
        for sample_val, group in files.groupby(sample_col):
            paths = sorted(group[file_col].dropna().astype(str))
            rows.append({
                "sample": sample_val,
                "fastq_1": paths[0] if paths else "",
                "fastq_2": paths[1] if len(paths) > 1 else "",
            })
        sheet = pd.DataFrame(rows)
    if sample_col != "sample" and sample_col in sheet.columns:
        sheet = sheet.rename(columns={sample_col: "sample"})
    for col in ("fastq_1", "fastq_2"):
        if col not in sheet.columns:
            sheet[col] = ""
    sheet["fastq_2"] = sheet["fastq_2"].fillna("")
    sheet[["sample", "fastq_1", "fastq_2"]].to_csv("samplesheet.csv", index=False)
    ds.add_param("input", "samplesheet.csv")


if __name__ == "__main__":
    main()
