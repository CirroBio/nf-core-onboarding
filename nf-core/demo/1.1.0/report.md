# Onboarding report — nf-core/demo 1.1.0

**Cirro process:** `nf-demo-1-1-0`  ·  **Data type:** nf-core/demo
**Last validated:** 2026-06-13 19:49 UTC  ·  **Validation time:** 1.7s
**Overall:** PASS

## Local oracle (Track B)

| Check | Result | Detail |
|---|---|---|
| `form_schema` | PASS | valid JSON Schema |
| `required_reachable` | PASS | all required params mapped |
| `paths_resolve` | PASS | all mappings resolve |
| `preprocess_runs` | PASS |  |

## Test data

- Source: nf-core/demo `-profile test` (`conf/test.config`)
- Samplesheet: https://raw.githubusercontent.com/nf-core/test-datasets/viralrecon/samplesheet/samplesheet_test_illumina_amplicon.csv
- Samples: 3  ·  Input files: 6

## Generation

- Reference config adapted: `scrnaseq/cellranger`
- Agent: 46 turns, $1.24

## Config

`nf-core/demo/1.1.0/` in this repository — the 6-file Cirro bundle
(`process-form.json`, `process-input.json`, `process-definition.json`,
`process-output.json`, `process-compute.config`, `preprocess.py`).

Registered as a custom process in the Cirro development account.
