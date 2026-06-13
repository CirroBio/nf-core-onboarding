# Onboarding report — nf-core/callingcards 1.0.0

**Cirro process:** `nf-callingcards-1-0-0`  ·  **Data type:** nf-core/callingcards
**Last validated:** 2026-06-13 20:21 UTC  ·  **Validation time:** 1.5s
**Overall:** PASS

## Local oracle (Track B)

| Check | Result | Detail |
|---|---|---|
| `form_schema` | PASS | valid JSON Schema |
| `required_reachable` | PASS | all required params mapped |
| `paths_resolve` | PASS | all mappings resolve |
| `preprocess_runs` | PASS |  |

## Test data

- Source: nf-core/callingcards `-profile test` (`conf/test.config`)
- Samplesheet: https://raw.githubusercontent.com/cmatKhan/test-datasets/callingcards/yeast/samplesheet.csv
- Samples: 1  ·  Input files: 2

## Generation

- Reference config adapted: `scrnaseq/cellranger`

## Config

`nf-core/callingcards/1.0.0/` in this repository — the 6-file Cirro bundle
(`process-form.json`, `process-input.json`, `process-definition.json`,
`process-output.json`, `process-compute.config`, `preprocess.py`).

Registered as a custom process in the Cirro development account.
