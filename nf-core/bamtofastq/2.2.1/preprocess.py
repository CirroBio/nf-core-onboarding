from __future__ import annotations

import pandas as pd
from cirro.helpers.preprocess_dataset import PreprocessDataset


def make_samplesheet(ds: PreprocessDataset) -> pd.DataFrame:
    """
    Build the nf-core/bamtofastq samplesheet from uploaded BAM/CRAM files.

    nf-core/bamtofastq expects a CSV samplesheet with columns:
        sample  – unique sample identifier
        bam     – absolute path to BAM or CRAM file
        bai     – path to BAI or CRAI index file (optional; empty string if absent)

    Files in the dataset are expected to be BAM/CRAM alignment files, optionally
    accompanied by BAI/CRAI index files placed alongside (same base path + suffix).
    """
    files_df = ds.files.copy()

    # Partition into alignment files and index files by extension
    is_bam = files_df["file"].str.lower().str.endswith((".bam", ".cram"))
    is_idx = files_df["file"].str.lower().str.endswith((".bai", ".crai"))

    bam_df = files_df[is_bam]
    idx_df = files_df[is_idx]

    # Build lookup: bam/cram path (without .bai/.crai) → index path
    # Handles both <file>.bam.bai and <file>.bam styles
    idx_lookup: dict[str, str] = {}
    for _, row in idx_df.iterrows():
        f: str = row["file"]
        for suffix in (".bai", ".crai"):
            if f.lower().endswith(suffix):
                idx_lookup[f[: -len(suffix)]] = f
                break

    rows = []
    for _, row in bam_df.iterrows():
        bam_path: str = row["file"]

        # Use dataset sample name if present; otherwise derive from filename
        sample: str = str(row.get("sample", "")).strip()
        if not sample:
            basename = bam_path.rsplit("/", 1)[-1]
            for ext in (".bam", ".cram"):
                if basename.lower().endswith(ext):
                    basename = basename[: -len(ext)]
                    break
            sample = basename

        bai_path = idx_lookup.get(bam_path, "")
        rows.append({"sample": sample, "bam": bam_path, "bai": bai_path})

    return pd.DataFrame(rows, columns=["sample", "bam", "bai"])


if __name__ == "__main__":
    ds = PreprocessDataset.from_running()
    samplesheet = make_samplesheet(ds)
    samplesheet.to_csv("samplesheet.csv", index=False)
