# Onboarding report — nf-core/clipseq 1.0.0

**Cirro process:** `nf-clipseq-1-0-0`  ·  **Data type:** nf-core/clipseq
**Last validated:** 2026-06-13 20:21 UTC  ·  **Validation time:** 1.5s
**Overall:** PASS

## Local oracle (Track B)

| Check | Result | Detail |
|---|---|---|
| `form_schema` | PASS | valid JSON Schema |
| `required_reachable` | PASS | all required params mapped |
| `paths_resolve` | PASS | all mappings resolve |
| `preprocess_runs` | PASS | 2026-06-13 13:21:29,234 INFO     [PreprocessDataset] Saving parameters |

## Test data

- Source: nf-core/clipseq `-profile test` (`conf/test.config`)
- Samplesheet: https://raw.githubusercontent.com/nf-core/test-datasets/clipseq/metadata.csv
- Samples: 2  ·  Input files: 2

## Generation

- Reference config adapted: `scrnaseq/cellranger`

## Config

`nf-core/clipseq/1.0.0/` in this repository — the 6-file Cirro bundle
(`process-form.json`, `process-input.json`, `process-definition.json`,
`process-output.json`, `process-compute.config`, `preprocess.py`).

Registered as a custom process in the Cirro development account.
