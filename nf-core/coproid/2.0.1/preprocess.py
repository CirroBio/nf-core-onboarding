#!/usr/bin/env python3
"""Cirro preprocess: build the workflow input samplesheet from the dataset."""
import pandas as pd
from cirro.helpers.preprocess_dataset import PreprocessDataset


def main() -> None:
    ds = PreprocessDataset.from_running()
    # Structured dataset: pivot the samplesheet (Cirro names columns 'sampleName' +
    # one per read position 'R1'/'R2'); rename to the nf-core columns.
    sheet = None
    try:
        sheet = ds.pivot_samplesheet(metadata_columns=[]).rename(
            columns={"sampleName": "sample", "R1": "fastq_1", "R2": "fastq_2"})
    except Exception as exc:
        ds.logger.info(f"[preprocess] pivot_samplesheet failed ({exc!r}); building from ds.files")
    if sheet is None or "fastq_1" not in sheet.columns:
        # Cirro could not tag reads (e.g. files named _1/_2 rather than _R1/_R2), so
        # the pivot has no R1/R2. Build from ds.files by sorted filename per sample.
        files = ds.files.copy()
        ds.logger.info(f"[preprocess] no read columns; ds.files = {list(files.columns)}")
        sample_col = "sample" if "sample" in files.columns else (
            "sampleName" if "sampleName" in files.columns else files.columns[0])
        file_col = next(
            (c for c in ("file", "path", "relativePath", "dataPath") if c in files.columns),
            files.columns[-1])
        rows = []
        for sample_val, group in files.groupby(sample_col):
            paths = sorted(group[file_col].dropna().astype(str))
            rows.append({"sample": sample_val,
                         "fastq_1": paths[0] if paths else "",
                         "fastq_2": paths[1] if len(paths) > 1 else ""})
        sheet = pd.DataFrame(rows)
    if "fastq_2" not in sheet.columns:
        sheet["fastq_2"] = ""
    sheet["fastq_2"] = sheet["fastq_2"].fillna("")
    sheet[["sample", "fastq_1", "fastq_2"]].to_csv("samplesheet.csv", index=False)
    ds.add_param("input", "samplesheet.csv", overwrite=True)


if __name__ == "__main__":
    main()
