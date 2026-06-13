import pandas as pd

from cirro.helpers.preprocess_dataset import PreprocessDataset


def make_samplesheet(ds: PreprocessDataset) -> pd.DataFrame:
    """
    Build an nf-core/seqinspector samplesheet (sample,fastq_1,fastq_2)
    from a Cirro dataset containing paired- or single-end FASTQ files.

    Cirro file metadata uses readType "R" for sequencing reads (vs "I" for
    index files).  pivot_samplesheet groups by sample and creates one column
    per distinct readNumber/readType, which we rename to the nf-core columns
    expected by assets/schema_input.json.
    """
    df = ds.pivot_samplesheet(
        metadata_columns=[],
    )

    # pivot_samplesheet returns a column named 'sampleName'; nf-core expects 'sample'
    df = df.rename(columns={"sampleName": "sample"})

    # Map Cirro read-position columns → nf-core column names
    # Cirro typically names these R1 / R2 after the readNumber attribute
    rename_map = {}
    if "R1" in df.columns:
        rename_map["R1"] = "fastq_1"
    if "R2" in df.columns:
        rename_map["R2"] = "fastq_2"
    df = df.rename(columns=rename_map)

    # Ensure required column exists; pad optional fastq_2 with empty string
    # so single-end datasets are handled gracefully
    if "fastq_1" not in df.columns:
        raise ValueError(
            "No R1 read files found in dataset — cannot build seqinspector samplesheet."
        )
    if "fastq_2" not in df.columns:
        df["fastq_2"] = ""

    # Return only the columns seqinspector expects, in order
    return df[["sample", "fastq_1", "fastq_2"]]


if __name__ == "__main__":
    ds = PreprocessDataset.from_running()
    samplesheet = make_samplesheet(ds)
    samplesheet.to_csv("samplesheet.csv", index=False)
