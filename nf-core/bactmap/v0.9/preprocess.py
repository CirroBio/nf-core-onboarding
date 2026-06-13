#!/usr/bin/env python3
"""
Preprocess for nf-core/bactmap v0.9
Builds the input samplesheet (CSV) from uploaded FASTQ files.

bactmap samplesheet format:
    sample,fastq_1,fastq_2
    SAMPLE_PE,reads_R1.fastq.gz,reads_R2.fastq.gz
    SAMPLE_SE,reads_R1.fastq.gz,
"""

import pandas as pd
from cirro.helpers.preprocess_dataset import PreprocessDataset


def make_samplesheet(ds: PreprocessDataset) -> pd.DataFrame:
    """Pivot uploaded FASTQ files into the bactmap samplesheet format."""

    # Drop any index / non-read files (e.g. .bai, .fai)
    ds.files = ds.files.loc[
        ds.files.apply(
            lambda r: r.get("readType", "R") == "R",
            axis=1,
        )
    ]

    # Pivot to wide format: one row per sample, columns fastq_1 / fastq_2
    samplesheet = ds.wide_samplesheet(
        index=["sampleIndex", "sample", "lane"],
        columns="read",
        values="file",
        column_prefix="fastq_",
    )

    assert samplesheet.shape[0] > 0, (
        "No FASTQ files detected — check that data was uploaded correctly."
    )

    # Keep only the columns bactmap expects; fastq_2 may be absent for SE data
    ordered = ["sample", "fastq_1", "fastq_2"]
    for col in ordered:
        if col not in samplesheet.columns:
            samplesheet[col] = ""

    samplesheet = samplesheet.reindex(columns=ordered)
    samplesheet = samplesheet.fillna("")

    return samplesheet


if __name__ == "__main__":

    ds = PreprocessDataset.from_running()

    samplesheet = make_samplesheet(ds)

    # Write the samplesheet that nextflow will receive via --input
    samplesheet.to_csv("samplesheet.csv", index=False)

    ds.logger.info(f"Wrote samplesheet with {samplesheet.shape[0]} sample(s)")
    ds.logger.info(ds.params)
