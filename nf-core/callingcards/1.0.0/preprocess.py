from __future__ import annotations

import pandas as pd

from cirro.helpers.preprocess_dataset import PreprocessDataset


def make_samplesheet(ds: PreprocessDataset) -> pd.DataFrame:
    """
    Build the samplesheet for nf-core/callingcards (mammalian bulk calling cards).

    Expected output columns:
        sample    – unique sample identifier
        fastq_1   – path to R1 FASTQ (required)
        fastq_2   – path to R2 FASTQ (optional; omitted for single-end data)

    Reference: https://nf-co.re/callingcards/usage#samplesheet-input
    """
    samplesheet = ds.pivot_samplesheet(
        metadata_columns=[],
    )

    # Rename Cirro pivot output columns → nf-core/callingcards samplesheet columns
    col_map: dict[str, str] = {}
    if "sampleName" in samplesheet.columns:
        col_map["sampleName"] = "sample"
    if "R1" in samplesheet.columns:
        col_map["R1"] = "fastq_1"
    if "R2" in samplesheet.columns:
        col_map["R2"] = "fastq_2"
    samplesheet = samplesheet.rename(columns=col_map)

    # Guard: required columns must be present
    required = ["sample", "fastq_1"]
    missing = [c for c in required if c not in samplesheet.columns]
    if missing:
        raise ValueError(
            f"Samplesheet is missing required column(s): {missing}. "
            f"Available columns: {list(samplesheet.columns)}"
        )

    # Return only the columns callingcards expects; drop any Cirro-internal extras
    keep = [c for c in ["sample", "fastq_1", "fastq_2"] if c in samplesheet.columns]
    return samplesheet[keep]


if __name__ == "__main__":
    ds = PreprocessDataset.from_running()
    samplesheet = make_samplesheet(ds)
    samplesheet.to_csv("samplesheet.csv", index=False)
