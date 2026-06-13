# Onboarding report — nf-core/coproid 2.0.1

**Cirro process:** `nf-coproid-2-0-1`  ·  **Data type:** nf-core/coproid
**Last validated:** 2026-06-13 20:21 UTC  ·  **Validation time:** 1.9s
**Overall:** PASS

## Local oracle (Track B)

| Check | Result | Detail |
|---|---|---|
| `form_schema` | PASS | valid JSON Schema |
| `required_reachable` | PASS | all required params mapped |
| `paths_resolve` | PASS | all mappings resolve |
| `preprocess_runs` | PASS |  |

## Test data

- Source: nf-core/coproid `-profile test` (`conf/test.config`)
- Samplesheet: https://github.com/nf-core/test-datasets/raw/coproid/reads/samplesheet.csv
- Samples: 2  ·  Input files: 4

## Generation

- Reference config adapted: `scrnaseq/cellranger`

## Config

`nf-core/coproid/2.0.1/` in this repository — the 6-file Cirro bundle
(`process-form.json`, `process-input.json`, `process-definition.json`,
`process-output.json`, `process-compute.config`, `preprocess.py`).

Registered as a custom process in the Cirro development account.
