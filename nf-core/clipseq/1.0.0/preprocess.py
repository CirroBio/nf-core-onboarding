from __future__ import annotations

import pandas as pd
from cirro.helpers.preprocess_dataset import PreprocessDataset

# ---------------------------------------------------------------------------
# Column-name aliases the Cirro SDK / emulator may use
# ---------------------------------------------------------------------------
_SAMPLE_COLS = ("sampleName", "sample")
_PATH_COLS   = ("uri", "s3Path", "path", "filePath", "s3uri", "file")
_RTYPE_COLS  = ("readType", "read")


def _col(df: pd.DataFrame, candidates: tuple[str, ...]) -> str | None:
    """Return the first candidate column that exists in *df*, else None."""
    return next((c for c in candidates if c in df.columns), None)


def make_samplesheet(ds: PreprocessDataset) -> pd.DataFrame:
    """Build the nf-core/clipseq samplesheet from uploaded FASTQ files.

    nf-core/clipseq 1.0.0 expects a CSV samplesheet with columns:
        sample, fastq_1[, fastq_2]

    CLIP-seq data is typically single-end, so fastq_2 is optional.
    Handles two Cirro file-metadata conventions:
      • readType / R1 / R2 / R  (live Cirro)
      • read / R1 / R2 / R      (oracle test emulator)
    """
    files = ds.files

    rtype_col = _col(files, _RTYPE_COLS)
    name_col  = _col(files, _SAMPLE_COLS)
    path_col  = _col(files, _PATH_COLS)

    has_read_type = rtype_col is not None
    read_types: set[str] = (
        set(files[rtype_col].dropna().astype(str)) if has_read_type else set()
    )

    if has_read_type and ("R1" in read_types or "R2" in read_types):
        # Paired-end upload tagged as R1 / R2
        samplesheet = ds.pivot_samplesheet(
            metadata_columns=[],
            file_filter_predicate=f'{rtype_col} in ["R1", "R2"]',
        )
        samplesheet = samplesheet.rename(
            columns={"R1": "fastq_1", "R2": "fastq_2"},
            errors="ignore",
        )

    elif has_read_type and "R" in read_types:
        # Single-end upload tagged as R (typical for CLIP-seq)
        samplesheet = ds.pivot_samplesheet(
            metadata_columns=[],
            file_filter_predicate=f'{rtype_col} == "R"',
        )
        samplesheet = samplesheet.rename(columns={"R": "fastq_1"}, errors="ignore")

    else:
        # No recognised read-type — build directly from ds.files to avoid
        # pivot_samplesheet pivoting integer-typed columns and hitting NaN errors.
        if name_col is None or path_col is None:
            raise RuntimeError(
                f"Cannot build samplesheet: ds.files has columns {list(files.columns)}. "
                "Expected a sample-name column (sampleName/sample) and a path column "
                f"({'/'.join(_PATH_COLS)})."
            )

        rows: list[dict] = []
        for sample_name, grp in files.groupby(name_col, sort=True):
            paths = grp.sort_values(path_col)[path_col].dropna().tolist()
            if not paths:
                continue
            row: dict = {"sample": sample_name, "fastq_1": paths[0]}
            if len(paths) > 1:
                row["fastq_2"] = paths[1]
            rows.append(row)
        samplesheet = pd.DataFrame(rows)

    # Normalise the sample-name column to "sample"
    if "sample" not in samplesheet.columns and "sampleName" in samplesheet.columns:
        samplesheet = samplesheet.rename(columns={"sampleName": "sample"})

    # Enforce column order expected by nf-core/clipseq
    ordered = ["sample", "fastq_1"]
    if "fastq_2" in samplesheet.columns:
        ordered.append("fastq_2")
    present = [c for c in ordered if c in samplesheet.columns]
    return samplesheet[present]


if __name__ == "__main__":
    ds = PreprocessDataset.from_running()

    samplesheet = make_samplesheet(ds)
    samplesheet.to_csv("samplesheet.csv", index=False)

    # Point the pipeline's --input param at the generated samplesheet
    ds.add_param("input", "samplesheet.csv", overwrite=True)
