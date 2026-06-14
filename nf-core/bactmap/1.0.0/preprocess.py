#!/usr/bin/env python3
"""Cirro preprocess: build the workflow input samplesheet from the dataset."""
from cirro.helpers.preprocess_dataset import PreprocessDataset


def main() -> None:
    ds = PreprocessDataset.from_running()
    # Structured dataset: pivot the samplesheet (long file rows -> wide form).
    # Cirro names the columns 'sampleName' + one per read position 'R1'/'R2'
    # (readType R = sequencing read, I = index); rename to the nf-core columns.
    sheet = ds.pivot_samplesheet(metadata_columns=[])
    sheet = sheet.rename(columns={"sampleName": "sample", "R1": "fastq_1", "R2": "fastq_2"})
    if "fastq_2" not in sheet.columns:
        sheet["fastq_2"] = ""
    sheet[["sample", "fastq_1", "fastq_2"]].to_csv("samplesheet.csv", index=False)
    ds.add_param("input", "samplesheet.csv", overwrite=True)


if __name__ == "__main__":
    main()
