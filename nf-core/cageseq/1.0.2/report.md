# Onboarding report — nf-core/cageseq 1.0.2

**Cirro process:** `nf-cageseq-1-0-2`  ·  **Data type:** nf-core/cageseq
**Last validated:** 2026-06-13 20:21 UTC  ·  **Validation time:** 1.3s
**Overall:** PASS

## Local oracle (Track B)

| Check | Result | Detail |
|---|---|---|
| `form_schema` | PASS | valid JSON Schema |
| `required_reachable` | PASS | all required params mapped |
| `paths_resolve` | PASS | all mappings resolve |
| `preprocess_runs` | PASS | 2026-06-13 13:21:24,149 WARNING  [PreprocessDataset] Pivot column not found, grouping by sample instead. |

## Test data

- Source: nf-core/cageseq `-profile test` (`conf/test.config`)
- Samplesheet: (not resolved)
- Samples: 0  ·  Input files: 0

## Generation

- Reference config adapted: `scrnaseq/cellranger`

## Config

`nf-core/cageseq/1.0.2/` in this repository — the 6-file Cirro bundle
(`process-form.json`, `process-input.json`, `process-definition.json`,
`process-output.json`, `process-compute.config`, `preprocess.py`).

Registered as a custom process in the Cirro development account.
