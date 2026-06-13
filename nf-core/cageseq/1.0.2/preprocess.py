import pandas as pd

from cirro.helpers.preprocess_dataset import PreprocessDataset


def make_samplesheet(ds: PreprocessDataset) -> pd.DataFrame:
    """
    Build the samplesheet CSV for nf-core/cageseq.

    CAGE-seq is typically single-end sequencing.
    nf-core/cageseq expects columns: sample, fastq_1[, fastq_2]

    pivot_samplesheet returns one row per sample with a column per
    read type (R1 / R2). We rename to the nf-core expected headers.
    """
    samplesheet = ds.pivot_samplesheet(
        metadata_columns=[],
    )

    # Rename Cirro pivot columns → nf-core/cageseq samplesheet headers
    col_map: dict[str, str] = {}
    if "sampleName" in samplesheet.columns:
        col_map["sampleName"] = "sample"
    if "R1" in samplesheet.columns:
        col_map["R1"] = "fastq_1"
    if "R2" in samplesheet.columns:
        col_map["R2"] = "fastq_2"
    samplesheet = samplesheet.rename(columns=col_map)

    # Ensure required columns are present
    if "sample" not in samplesheet.columns:
        raise ValueError(
            "pivot_samplesheet did not produce a 'sampleName'/'sample' column. "
            "Check that uploaded files have sampleName metadata."
        )
    if "fastq_1" not in samplesheet.columns:
        raise ValueError(
            "pivot_samplesheet did not produce an R1 column. "
            "Check that uploaded FASTQ files are labelled readType=R1."
        )

    return samplesheet


if __name__ == "__main__":
    ds = PreprocessDataset.from_running()
    samplesheet = make_samplesheet(ds)
    samplesheet.to_csv("samplesheet.csv", index=False)
