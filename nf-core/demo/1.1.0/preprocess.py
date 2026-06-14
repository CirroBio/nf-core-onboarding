import pandas as pd

from cirro.helpers.preprocess_dataset import PreprocessDataset

# ---------------------------------------------------------------------------
# Column-name constants (as produced by Cirro's PreprocessDataset.files)
# ---------------------------------------------------------------------------
_SAMPLE_COL = "sample"
_FILE_COL = "file"       # absolute / S3 file path
_READ_COL = "read"       # integer: 1 = R1 (fastq_1), 2 = R2 (fastq_2)


def make_samplesheet(ds: PreprocessDataset) -> pd.DataFrame:
    """Build an nf-core/demo samplesheet from uploaded FASTQ files.

    nf-core/demo schema_input.json columns:
        sample  – sample identifier (required)
        fastq_1 – path to read-1 FASTQ (required)
        fastq_2 – path to read-2 FASTQ (optional; empty for single-end)

    Cirro ds.files schema:
        sample  – str, sample identifier
        file    – str, S3 / HTTPS path to the FASTQ file
        read    – int64, 1 for R1, 2 for R2
    """
    files = ds.files.copy()

    # --- resolve actual column names (defensive, handles minor API drift) ---
    sample_col = _SAMPLE_COL if _SAMPLE_COL in files.columns else "sampleName"
    file_col   = _FILE_COL   if _FILE_COL   in files.columns else next(
        (c for c in ("path", "relativePath", "dataPath") if c in files.columns),
        files.columns[1],  # last resort: second column
    )
    read_col = _READ_COL if _READ_COL in files.columns else None

    if read_col is not None:
        # pivot_table handles any duplicate (sample, read) pairs gracefully
        pivot = (
            files.pivot_table(
                index=sample_col,
                columns=read_col,
                values=file_col,
                aggfunc="first",
            )
            .reset_index()
        )
        pivot.columns.name = None  # drop "read" axis label

        # Map integer read numbers → nf-core column names.
        # Also handle string variants ("R1"/"R2", "1"/"2") for robustness.
        _R1 = {1, "1", "R1", "r1"}
        _R2 = {2, "2", "R2", "r2"}
        rename = {}
        for col in pivot.columns:
            if col in _R1:
                rename[col] = "fastq_1"
            elif col in _R2:
                rename[col] = "fastq_2"
        pivot = pivot.rename(columns=rename)
        if sample_col != "sample":
            pivot = pivot.rename(columns={sample_col: "sample"})

    else:
        # Fallback: no read-type column — assign files to fastq_1 / fastq_2
        # by sorting paths lexicographically (R1 < R2 in standard naming).
        rows: list[dict] = []
        for sample_val, grp in files.groupby(sample_col):
            paths = sorted(grp[file_col].dropna().tolist())
            rows.append(
                {
                    "sample": sample_val,
                    "fastq_1": paths[0] if len(paths) >= 1 else "",
                    "fastq_2": paths[1] if len(paths) >= 2 else "",
                }
            )
        pivot = pd.DataFrame(rows, columns=["sample", "fastq_1", "fastq_2"])

    # Guarantee fastq_2 column exists and NaN → ""
    if "fastq_2" not in pivot.columns:
        pivot["fastq_2"] = ""
    pivot["fastq_2"] = pivot["fastq_2"].fillna("").astype(str)

    return pivot[["sample", "fastq_1", "fastq_2"]]


if __name__ == "__main__":
    ds = PreprocessDataset.from_running()
    samplesheet = make_samplesheet(ds)
    samplesheet.to_csv("samplesheet.csv", index=False)
    # Wire --input to the samplesheet we just built; without this the
    # workflow falls back to the raw dataset dir (rejected by nf-schema).
    ds.add_param("input", "samplesheet.csv")
