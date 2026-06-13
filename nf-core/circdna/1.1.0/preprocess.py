#!/usr/bin/env python3
"""
preprocess.py for nf-core/circdna 1.1.0

Builds the CSV samplesheet that the pipeline reads via --input.

FASTQ samplesheet columns : sample, fastq_1, fastq_2
BAM   samplesheet columns  : sample, bam
"""
from __future__ import annotations

import json

from cirro.helpers.preprocess_dataset import PreprocessDataset
import pandas as pd


_DEFAULT_INPUT_FORMAT = "FASTQ"


# ---------------------------------------------------------------------------
# Samplesheet builders
# ---------------------------------------------------------------------------

def make_samplesheet_fastq(ds: PreprocessDataset) -> pd.DataFrame:
    """Build FASTQ samplesheet: sample, fastq_1, fastq_2.

    Pivots ds.files on the 'read' column so each sample row has paired
    fastq_1 / fastq_2 paths.  Index files (readType != 'R') are excluded.
    """
    # Drop index / auxiliary files so only raw reads remain
    ds.files = ds.files.loc[
        ds.files.apply(lambda r: r.get("readType", "R") == "R", axis=1)
    ]

    manifest: pd.DataFrame = ds.wide_samplesheet(
        index=["sample"],
        columns="read",
        values="file",
        column_prefix="fastq_",
    )

    assert manifest.shape[0] > 0, (
        "No FASTQ files detected — there may be an error with data ingest"
    )

    # Ensure columns are in the expected order; fastq_2 may be absent for
    # single-end data — fill with empty string so the CSV is always 3-col.
    for col in ("fastq_1", "fastq_2"):
        if col not in manifest.columns:
            manifest[col] = ""

    return manifest[["sample", "fastq_1", "fastq_2"]].reset_index(drop=True)


def make_samplesheet_bam(ds: PreprocessDataset) -> pd.DataFrame:
    """Build BAM samplesheet: sample, bam.

    Selects only .bam files from ds.files.
    """
    bam_rows = ds.files.loc[ds.files["file"].str.lower().str.endswith(".bam")].copy()

    assert bam_rows.shape[0] > 0, (
        "No BAM files detected — there may be an error with data ingest"
    )

    manifest = (
        bam_rows[["sample", "file"]]
        .rename(columns={"file": "bam"})
        .reset_index(drop=True)
    )
    return manifest


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    ds = PreprocessDataset.from_running()

    input_format = (
        ds.params.get("input_format") or _DEFAULT_INPUT_FORMAT
    ).upper()
    ds.logger.info(
        f"circdna preprocess — input_format={input_format!r}, "
        f"files={ds.files.shape[0]}"
    )

    if input_format == "BAM":
        samplesheet = make_samplesheet_bam(ds)
    else:
        samplesheet = make_samplesheet_fastq(ds)

    # Log the samplesheet for debugging
    for line in samplesheet.to_csv(index=None).split("\n"):
        ds.logger.info(line)

    samplesheet.to_csv("samplesheet.csv", index=None)
    ds.logger.info(f"Wrote {samplesheet.shape[0]} row(s) to samplesheet.csv")

    # Validate that circle_identifier was set (required param)
    circle_identifier = ds.params.get("circle_identifier")
    assert circle_identifier, (
        "ERROR: You must select at least one circle identifier "
        "(--circle_identifier)."
    )
    ds.logger.info(f"circle_identifier: {circle_identifier!r}")

    ds.logger.info(f"Final params ({len(ds.params)} total): {json.dumps(ds.params, default=str)}")
