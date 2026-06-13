#!/usr/bin/env python3
"""
preprocess.py — nf-core/airrflow 5.1.0

Builds an airrflow samplesheet (TSV) from files uploaded to Cirro.

Samplesheet format depends on --mode:
  fastq      (default) paired FASTQ files → filename_R1 / filename_R2 columns
  assembled  pre-assembled AIRR sequences  → filename column

Per-sample metadata (subject_id, species, pcr_target_loci, tissue,
single_cell, …) is read from the Cirro samplesheet, falling back to
ds.params for any column not supplied per-sample.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request

import pandas as pd

from cirro.helpers.preprocess_dataset import PreprocessDataset


# ── Column definitions ───────────────────────────────────────────────────────

_FASTQ_COLS = [
    "sample",
    "filename_R1",
    "filename_R2",
    "subject_id",
    "species",
    "pcr_target_loci",
    "tissue",
    "single_cell",
    "sex",
    "age",
    "biomaterial_provider",
    "disease_state_sample",
    "cell_subset",
]

_ASSEMBLED_COLS = [
    "sample",
    "filename",
    "subject_id",
    "species",
    "pcr_target_loci",
    "tissue",
    "single_cell",
    "sex",
    "age",
    "biomaterial_provider",
    "disease_state_sample",
    "cell_subset",
]

_META_COLS = [
    "subject_id",
    "species",
    "pcr_target_loci",
    "tissue",
    "single_cell",
    "sex",
    "age",
    "biomaterial_provider",
    "disease_state_sample",
    "cell_subset",
]

_DEFAULT_WORKFLOW_VERSION = "5.1.0"

_PROTECTED_PARAMS = frozenset({"input", "outdir", "monochrome_logs"})

_MAX_EXTRA_JSON_BYTES = 10_000


# ── Helpers ──────────────────────────────────────────────────────────────────

def _sample_metadata(ds: PreprocessDataset) -> pd.DataFrame:
    """
    Return a DataFrame indexed by 'sample' with AIRR metadata columns.

    Columns present in ds.samplesheet win; any column absent from the
    samplesheet is filled from ds.params (global default) or left empty.
    """
    ss = getattr(ds, "samplesheet", None)
    if ss is None or ss.empty:
        ss = pd.DataFrame(columns=["sample"])

    # Normalise the sample-name column
    if "sample" not in ss.columns:
        for alt in ("sampleName", "sample_id", "id", "Sample"):
            if alt in ss.columns:
                ss = ss.rename(columns={alt: "sample"})
                break
        else:
            ss["sample"] = ""

    for col in _META_COLS:
        if col not in ss.columns:
            ss[col] = ds.params.get(col, "")

    return ss.set_index("sample")


def _merge_meta(manifest: pd.DataFrame, meta: pd.DataFrame) -> pd.DataFrame:
    """Left-join AIRR metadata onto manifest (keyed by 'sample')."""
    if meta.empty:
        for col in _META_COLS:
            manifest[col] = ""
        return manifest

    cols_present = [c for c in _META_COLS if c in meta.columns]
    return manifest.join(meta[cols_present], on="sample", how="left")


# ── Samplesheet builders ─────────────────────────────────────────────────────

def make_fastq_samplesheet(ds: PreprocessDataset) -> pd.DataFrame:
    """
    Build the airrflow samplesheet for --mode fastq.

    One row per sample (or per-sample per-lane if multiple lanes exist).
    Columns: filename_R1, filename_R2 (empty string when single-end).
    """
    files = ds.files.copy()

    # Drop index / UMI reads so only R1 / R2 remain
    if "readType" in files.columns:
        files = files.loc[~files["readType"].isin(["I", "I1", "I2"])]

    # Pivot to wide: one column per read direction
    manifest: pd.DataFrame = ds.wide_samplesheet(
        index=["sample"],
        columns="read",
        values="file",
        column_prefix="filename_",
    )

    assert manifest.shape[0] > 0, "No FASTQ files detected — check data ingest"

    # Ensure filename_R2 exists even for single-end data
    if "filename_R2" not in manifest.columns:
        manifest["filename_R2"] = ""
    manifest["filename_R2"] = manifest["filename_R2"].fillna("")

    meta = _sample_metadata(ds)
    manifest = _merge_meta(manifest, meta)

    for col in _FASTQ_COLS:
        if col not in manifest.columns:
            manifest[col] = ""

    return manifest.reindex(columns=_FASTQ_COLS)


def make_assembled_samplesheet(ds: PreprocessDataset) -> pd.DataFrame:
    """
    Build the airrflow samplesheet for --mode assembled.

    Expects one assembled sequence file (FASTA/TSV) per sample.
    """
    files = ds.files.copy()

    # One file per sample row
    if "sample" not in files.columns:
        files["sample"] = files.get("sampleName", files.index.astype(str))

    manifest = files[["sample", "file"]].rename(columns={"file": "filename"})
    assert manifest.shape[0] > 0, "No assembled files detected — check data ingest"

    meta = _sample_metadata(ds)
    manifest = _merge_meta(manifest, meta)

    for col in _ASSEMBLED_COLS:
        if col not in manifest.columns:
            manifest[col] = ""

    return manifest.reindex(columns=_ASSEMBLED_COLS)


# ── Extra-JSON / schema-filter helpers ───────────────────────────────────────

def apply_extra_json_params(ds: PreprocessDataset) -> None:
    """Parse the extra_params_json textarea and merge into ds.params."""
    raw = (ds.params.get("extra_params_json") or "").strip()
    ds.remove_param("extra_params_json", force=True)

    if not raw:
        ds.logger.info("extra_params_json: nothing to apply")
        return

    if len(raw) > _MAX_EXTRA_JSON_BYTES:
        ds.logger.warning(
            f"extra_params_json: payload too large ({len(raw):,} chars), skipping"
        )
        return

    try:
        extra = json.loads(raw)
    except json.JSONDecodeError as exc:
        ds.logger.warning(f"extra_params_json: JSON parse error ({exc}), skipping")
        return

    if not isinstance(extra, dict):
        ds.logger.warning(
            f"extra_params_json: expected a JSON object, got {type(extra).__name__}, skipping"
        )
        return

    applied = skipped = 0
    for key, value in extra.items():
        if not isinstance(key, str) or not key.strip():
            skipped += 1
            continue
        if key in _PROTECTED_PARAMS:
            ds.logger.warning(f"extra_params_json: skipping protected param '{key}'")
            skipped += 1
            continue
        ds.add_param(key, value, overwrite=True)
        applied += 1

    ds.logger.info(f"extra_params_json: applied {applied}, skipped {skipped}")


def filter_params_by_schema(ds: PreprocessDataset) -> None:
    """Drop params absent from nf-core/airrflow nextflow_schema.json."""
    version = ds.params.get("workflow_version", _DEFAULT_WORKFLOW_VERSION)
    ds.remove_param("workflow_version", force=True)

    url = (
        f"https://raw.githubusercontent.com/nf-core/airrflow/"
        f"{version}/nextflow_schema.json"
    )
    ds.logger.info(f"filter_params_by_schema: fetching schema for airrflow {version}")

    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            schema = json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            raise RuntimeError(
                f"nf-core/airrflow version '{version}' not found. "
                "See https://nf-co.re/airrflow/releases for available versions."
            ) from exc
        ds.logger.warning(f"filter_params_by_schema: HTTP {exc.code}, skipping filter")
        return
    except Exception as exc:  # noqa: BLE001
        ds.logger.warning(f"filter_params_by_schema: could not fetch schema — {exc}, skipping")
        return

    allowed: set[str] = set()
    for section in {**schema.get("$defs", {}), **schema.get("definitions", {})}.values():
        allowed.update(section.get("properties", {}).keys())

    ds.logger.info(f"filter_params_by_schema: {len(allowed):,} schema params")

    removed = [k for k in list(ds.params) if k not in allowed]
    for k in removed:
        ds.remove_param(k, force=True)

    if removed:
        ds.logger.info(f"filter_params_by_schema: removed {removed}")
    ds.logger.info(f"filter_params_by_schema: {len(ds.params)} params remain")


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    ds = PreprocessDataset.from_running()

    mode = ds.params.get("mode", "fastq")
    ds.logger.info(
        f"airrflow preprocess — "
        f"version={ds.params.get('workflow_version', _DEFAULT_WORKFLOW_VERSION)!r}, "
        f"mode={mode!r}"
    )

    if mode == "assembled":
        samplesheet = make_assembled_samplesheet(ds)
    else:
        # covers 'fastq', 'sc_10x_genomics', 'trust4', and any future modes
        samplesheet = make_fastq_samplesheet(ds)

    ds.logger.info(samplesheet.to_csv(sep="\t", index=False))
    samplesheet.to_csv("samplesheet.tsv", sep="\t", index=False)
    ds.logger.info(f"Wrote {samplesheet.shape[0]} row(s) to samplesheet.tsv")

    apply_extra_json_params(ds)
    filter_params_by_schema(ds)

    ds.logger.info(f"Final params ({len(ds.params)} total): {ds.params}")
