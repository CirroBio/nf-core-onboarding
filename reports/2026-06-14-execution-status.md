# nf-core → Cirro Onboarding & Execution Report

Generated from live runs as of 2026-06-14. Cirro development tenant (project `28dc61c4-8632-443c-b003-c6f99dc46040`).

Each pipeline's Cirro configuration is built from the published nf-core pipeline definition, registered as a runnable process, and executed against the pipeline's own `-profile test` data on the Cirro tenant. The Nextflow build is pinned per the pipeline's `manifest.nextflowVersion`. Outcomes are triaged: `COMPLETED` ran to success; `TEST-DATA-GAP` = the pipeline's test inputs were unavailable; `PIPELINE-BUG`/`INFRA` are outside the onboarding layer; `HARNESS-GAP` = addressable in the onboarding configuration.

**3 of 12 executed pipelines ran to COMPLETED** on the pipeline's own `-profile test` data. The rest are triaged below; the bucket names indicate where the onboarding layer can help (`HARNESS-GAP`) versus where the wall is the pipeline's test data or code (`TEST-DATA-GAP`/`PIPELINE-BUG`/`INFRA`).

| Pipeline | Version | Nextflow | Run start | Duration | Outcome |
|---|---|---|---|---|---|
| nf-core/demo | 1.1.0 | env-default | 2026-06-14 00:52 UTC | 6m21s | **COMPLETED** |
| nf-core/smrnaseq | 2.3.1 | 25.04.8 | 2026-06-14 11:43 UTC | 21m31s | **COMPLETED** |
| nf-core/viralrecon | 2.6.0 | 25.04.8 | 2026-06-14 03:42 UTC | 30m08s | **COMPLETED** |
| nf-core/bactmap | 1.0.0 | 25.04.8 | 2026-06-14 14:44 UTC | 0m35s | **TEST-DATA-GAP** |
| nf-core/bamtofastq | 2.2.1 | 25.10.4 | 2026-06-14 12:29 UTC | 0m10s | **HARNESS-GAP** |
| nf-core/callingcards | 1.0.0 | 25.04.8 | 2026-06-14 11:47 UTC | 0m56s | **HARNESS-GAP** |
| nf-core/circdna | 1.1.0 | 25.04.8 | 2026-06-14 12:08 UTC | 16m42s | **INFRA** |
| nf-core/coproid | 2.0.1 | 25.04.8 | 2026-06-14 16:55 UTC | 7m56s | **PIPELINE-BUG** |
| nf-core/denovotranscript | 1.2.1 | 25.04.8 | 2026-06-14 14:43 UTC | 0m50s | **UNKNOWN** |
| nf-core/fastqrepair | 1.0.0 | 25.04.8 | 2026-06-14 04:13 UTC | 5m53s | **PIPELINE-BUG** |
| nf-core/funcscan | 3.0.0 | 25.04.8 | 2026-06-14 16:57 UTC | 3m15s | **UNKNOWN** |
| nf-core/metatdenovo | 1.3.0 | 25.10.4 | 2026-06-14 16:23 UTC | 6m42s | **PIPELINE-BUG** |

## Details
### nf-core/demo 1.1.0  (`nf-demo-1-1-0`)
- Outcome: **COMPLETED**
- Cirro run status: COMPLETED
- Test data: nf-core/demo test data (1.1.0)
- Nextflow build: env-default
- Run started: 2026-06-14 00:52 UTC  ·  Duration: 6m21s
- Run id: `d12308b0-0d35-4f9f-b35f-4fb5b0fe3344`

### nf-core/smrnaseq 2.3.1  (`nf-smrnaseq-2-3-1`)
- Outcome: **COMPLETED**
- Cirro run status: COMPLETED
- Test data: nf-core/smrnaseq test data PE (2.3.1)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 11:43 UTC  ·  Duration: 21m31s
- Run id: `9fb3740f-c6a5-48d7-8f33-42208606db84`

### nf-core/viralrecon 2.6.0  (`nf-viralrecon-2-6-0`)
- Outcome: **COMPLETED**
- Cirro run status: COMPLETED
- Test data: nf-core/viralrecon test data PE (2.6.0)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 03:42 UTC  ·  Duration: 30m08s
- Run id: `732d986f-40c9-4214-930b-2945d6c7ef28`

### nf-core/bactmap 1.0.0  (`nf-bactmap-1-0-0`)
- Outcome: **TEST-DATA-GAP** — a referenced input/genome file could not be staged (stale test data?)
- Cirro run status: FAILED
- Test data: nf-core/bactmap test data PE (1.0.0)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 14:44 UTC  ·  Duration: 0m35s
- First error: `ERROR ~ No such file or directory: https://raw.githubusercontent.com/nf-core/test-datasets/bactmap/genome/NCTC13799.fna`
- Run id: `7c5841da-b298-4566-8ec1-b30551330dba`

### nf-core/bamtofastq 2.2.1  (`nf-bamtofastq-2-2-1`)
- Outcome: **HARNESS-GAP** — preprocess: generated preprocess.py failed
- Cirro run status: FAILED
- Test data: nf-core/bamtofastq test data PE (2.2.1)
- Nextflow build: 25.10.4
- Run started: 2026-06-14 12:29 UTC  ·  Duration: 0m10s
- Run id: `75b95634-ce6d-4e8d-914a-3abae1d39cf6`

### nf-core/callingcards 1.0.0  (`nf-callingcards-1-0-0`)
- Outcome: **HARNESS-GAP** — samplesheet: generated sheet fails the pipeline's schema_input
- Cirro run status: FAILED
- Test data: nf-core/callingcards test data PE (1.0.0)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 11:47 UTC  ·  Duration: 0m56s
- First error: `ERROR ~ ERROR: Validation of 'input' file failed!`
- Run id: `d9cf8347-2c9b-47c5-8cec-93df5a6a3126`

### nf-core/circdna 1.1.0  (`nf-circdna-1-1-0`)
- Outcome: **INFRA** — a process has no resolvable container / Batch job definition
- Cirro run status: FAILED
- Test data: nf-core/circdna test data PE (1.1.0)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 12:08 UTC  ·  Duration: 16m42s
- First error: `ERROR ~ Error executing process > 'NFCORE_CIRCDNA:CIRCDNA:CIRCLEFINDER (circdna_1)'`
- Run id: `90d47234-21f4-4b93-83ed-5eaba95d5829`

### nf-core/coproid 2.0.1  (`nf-coproid-2-0-1`)
- Outcome: **PIPELINE-BUG** — a workflow process failed (pipeline tool/code)
- Cirro run status: FAILED
- Test data: nf-core/coproid test data PE (2.0.1)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 16:55 UTC  ·  Duration: 7m56s
- First error: `ERROR ~ Error executing process > 'NFCORE_COPROID:COPROID:QUARTO_REPORTING:QUARTONOTEBOOK (quarto_notebook)'`
- Run id: `0e32672e-9c06-4b9e-90c6-acc5282e7229`

### nf-core/denovotranscript 1.2.1  (`nf-denovotranscript-1-2-1`)
- Outcome: **UNKNOWN** — failed with no recognized signature
- Cirro run status: FAILED
- Test data: nf-core/denovotranscript test data PE (1.2.1)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 14:43 UTC  ·  Duration: 0m50s
- First error: `ERROR ~ Cannot invoke "java.nio.file.Path.getFileSystem()" because "path" is null`
- Run id: `c05a32e9-d779-4d27-9505-8a2669eac40e`

### nf-core/fastqrepair 1.0.0  (`nf-fastqrepair-1-0-0`)
- Outcome: **PIPELINE-BUG** — a workflow process failed (pipeline tool/code)
- Cirro run status: FAILED
- Test data: nf-core/fastqrepair test data PE (1.0.0)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 04:13 UTC  ·  Duration: 5m53s
- First error: `ERROR ~ No such variable: meta`
- Run id: `3510acd6-e7f7-4ce2-b185-f6e68af240f9`

### nf-core/funcscan 3.0.0  (`nf-funcscan-3-0-0`)
- Outcome: **UNKNOWN** — failed with no recognized signature
- Cirro run status: FAILED
- Test data: nf-core/funcscan test data PE (3.0.0)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 16:57 UTC  ·  Duration: 3m15s
- First error: `ERROR ~ Unknown method invocation `multiply` on ConfigObject type`
- Run id: `d6befa0d-a484-47d4-8bd5-7d2618c6d9e7`

### nf-core/metatdenovo 1.3.0  (`nf-metatdenovo-1-3-0`)
- Outcome: **PIPELINE-BUG** — a workflow process failed (pipeline tool/code)
- Cirro run status: FAILED
- Test data: nf-core/metatdenovo test data PE (1.3.0)
- Nextflow build: 25.10.4
- Run started: 2026-06-14 16:23 UTC  ·  Duration: 6m42s
- First error: `ERROR ~ Error executing process > 'NFCORE_METATDENOVO:METATDENOVO:PRODIGAL:PRODIGAL_MODULE (megahit.prodigal)'`
- Run id: `b00a2f89-eca9-4414-80b2-ad435dc10d39`

