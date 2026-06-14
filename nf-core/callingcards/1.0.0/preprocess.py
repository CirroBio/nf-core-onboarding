#!/usr/bin/env python3
"""Cirro preprocess: build the pipeline's DECLARED samplesheet from ds.files."""
import re

import pandas as pd
from cirro.helpers.preprocess_dataset import PreprocessDataset

SAMPLE_COL = 'sample'
FASTQ_COLS = ('fastq_1', 'fastq_2')
SINGLE_COLS = [('barcode_details', ('.json',))]
META_COLS = ()
COLUMNS = ('sample', 'fastq_1', 'fastq_2', 'barcode_details')
_FASTQ_EXTS = (".fastq.gz", ".fq.gz", ".fastq", ".fq")


def _sample_of(path, given):
    # Use the dataset's sample value when populated; otherwise derive it from the
    # filename (Cirro leaves `sample` empty for some ingests), stripping the data
    # extension then the read tag (_R1/_R2/_1/_2): e.g. test1_1.fastq.gz -> test1.
    # Strip COMPOUND index suffixes (A.bam.bai) so a file and its index collapse to
    # one sample (A), not two; otherwise the bam and its .bai land in separate rows.
    if isinstance(given, str) and given.strip():
        return given
    base = path.split("/")[-1].split("?")[0]
    base = re.sub(
        r"\.(fastq|fq)(\.gz)?$|\.(bam|cram)(\.(bai|crai|csi))?$|\.(bai|crai|csi)$|\.json$",
        "", base, flags=re.I)
    return re.sub(r"_R?[12]$", "", base)


def main():
    ds = PreprocessDataset.from_running()
    files = ds.files.copy()
    ds.logger.info(f"[preprocess] ds.files columns: {list(files.columns)}")
    scol = next((c for c in ("sample", "sampleName") if c in files.columns), None)
    fcol = next((c for c in ("file", "path", "relativePath", "dataPath") if c in files.columns),
                files.columns[-1])
    # fillna BEFORE astype: an empty `sample` cell reads back as NaN, and
    # NaN.astype(str) is the string "nan" — truthy, so it would defeat the
    # derive-from-filename fallback. Normalise empties to "" first.
    given = list(files[scol].fillna("").astype(str)) if scol else [""] * len(files)
    files = files.assign(_s=[_sample_of(str(f), g) for f, g in zip(files[fcol], given)])
    rows = []
    for sample_val, group in files.groupby("_s"):
        paths = sorted(str(p) for p in group[fcol].dropna())
        fastqs = [p for p in paths if p.split("?")[0].lower().endswith(_FASTQ_EXTS)] or paths
        row = {SAMPLE_COL: sample_val}
        for i, cn in enumerate(FASTQ_COLS):
            row[cn] = fastqs[i] if i < len(fastqs) else ""
        for cn, exts in SINGLE_COLS:
            row[cn] = next((p for p in paths if p.split("?")[0].lower().endswith(tuple(exts))), "")
        for cn in META_COLS:
            row[cn] = ""
        rows.append(row)
    sheet = pd.DataFrame(rows)
    for c in COLUMNS:
        if c not in sheet.columns:
            sheet[c] = ""
    sheet[list(COLUMNS)].to_csv("samplesheet.csv", index=False)
    ds.add_param("input", "samplesheet.csv", overwrite=True)


if __name__ == "__main__":
    main()
