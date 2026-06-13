import pandas as pd

from cirro.helpers.preprocess_dataset import PreprocessDataset


def make_samplesheet(ds: PreprocessDataset) -> pd.DataFrame:
    """
    Build the nf-core/coproid input samplesheet (sample,fastq_1,fastq_2)
    from uploaded paired-end FASTQ files.

    coproid expects a 3-column CSV:
        sample  - unique sample identifier
        fastq_1 - path to R1 (forward) FASTQ (gzipped)
        fastq_2 - path to R2 (reverse) FASTQ (gzipped); empty string for SE
    """
    samplesheet = ds.pivot_samplesheet(
        metadata_columns=[],
    )

    # pivot_samplesheet names the read columns read1 / read2;
    # coproid expects fastq_1 / fastq_2.
    samplesheet = samplesheet.rename(
        columns={
            "read1": "fastq_1",
            "read2": "fastq_2",
        }
    )

    # Ensure required columns are present; fill missing fastq_2 for SE data.
    if "fastq_2" not in samplesheet.columns:
        samplesheet["fastq_2"] = ""

    return samplesheet[["sample", "fastq_1", "fastq_2"]]


if __name__ == "__main__":
    ds = PreprocessDataset.from_running()
    samplesheet = make_samplesheet(ds)
    samplesheet.to_csv("samplesheet.csv", index=False)
