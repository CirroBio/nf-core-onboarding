# nf-core → Cirro Onboarding & Execution Report

Generated from live runs as of 2026-06-14. Cirro development tenant (project `28dc61c4-8632-443c-b003-c6f99dc46040`).

Each pipeline's Cirro configuration is built from the published nf-core pipeline definition, registered as a runnable process, and executed against the pipeline's own `-profile test` data on the Cirro tenant. The Nextflow build is pinned per the pipeline's `manifest.nextflowVersion`. Outcomes are triaged: `COMPLETED` ran to success; `TEST-DATA-GAP` = the pipeline's test inputs were unavailable; `PIPELINE-BUG`/`INFRA` are outside the onboarding layer; `HARNESS-GAP` = addressable in the onboarding configuration.

**3 of 17 executed pipelines ran to COMPLETED** on the pipeline's own `-profile test` data. The rest are triaged below; the bucket names indicate where the onboarding layer can help (`HARNESS-GAP`) versus where the wall is the pipeline's test data or code (`TEST-DATA-GAP`/`PIPELINE-BUG`/`INFRA`).

| Pipeline | Version | Nextflow | Run start | Duration | Outcome |
|---|---|---|---|---|---|
| nf-core/demo | 1.1.0 | env-default | 2026-06-14 00:52 UTC | 6m21s | **COMPLETED** |
| nf-core/smrnaseq | 2.3.1 | 25.04.8 | 2026-06-14 11:43 UTC | 21m31s | **COMPLETED** |
| nf-core/viralrecon | 2.6.0 | 25.04.8 | 2026-06-14 03:42 UTC | 30m08s | **COMPLETED** |
| nf-core/bactmap | 1.0.0 | 25.04.8 | 2026-06-14 14:44 UTC | 0m35s | **TEST-DATA-GAP** |
| nf-core/bamtofastq | 2.2.1 | 25.10.4 | 2026-06-14 15:01 UTC | 9m12s | **PIPELINE-BUG** |
| nf-core/callingcards | 1.0.0 | 25.04.8 | 2026-06-14 15:16 UTC | 0m49s | **HARNESS-GAP** |
| nf-core/circdna | 1.1.0 | 25.04.8 | 2026-06-14 12:08 UTC | 16m42s | **INFRA** |
| nf-core/coproid | 2.0.1 | 25.04.8 | 2026-06-14 15:17 UTC | 0m53s | **HARNESS-GAP** |
| nf-core/denovotranscript | 1.2.1 | 25.04.8 | 2026-06-14 15:18 UTC | 0m49s | **UNKNOWN** |
| nf-core/fastqrepair | 1.0.0 | 25.04.8 | 2026-06-14 04:13 UTC | 5m53s | **PIPELINE-BUG** |
| nf-core/funcscan | 3.0.0 | 25.10.4 | 2026-06-14 15:18 UTC | 1m03s | **UNKNOWN** |
| nf-core/hgtseq | 1.1.0 | 25.04.8 | 2026-06-14 15:07 UTC | 0m29s | **TEST-DATA-GAP** |
| nf-core/magmap | 1.1.0 | 25.10.4 | 2026-06-14 15:18 UTC | 0m36s | **UNKNOWN** |
| nf-core/metatdenovo | 1.3.0 | 25.10.4 | 2026-06-14 15:18 UTC | 0m33s | **UNKNOWN** |
| nf-core/nanoseq | 3.1.0 | 25.04.8 | 2026-06-14 15:07 UTC | 5m34s | **PIPELINE-BUG** |
| nf-core/scrnaseq | 4.1.0 | 25.04.8 | 2026-06-14 14:49 UTC | 0m30s | **UNKNOWN** |
| nf-core/viralmetagenome | 1.1.2 | 25.04.8 | 2026-06-14 15:18 UTC | 0m42s | **UNKNOWN** |

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
- Outcome: **PIPELINE-BUG** — a workflow process failed (pipeline tool/code)
- Cirro run status: FAILED
- Test data: nf-core/bamtofastq test data PE (2.2.1)
- Nextflow build: 25.10.4
- Run started: 2026-06-14 15:01 UTC  ·  Duration: 9m12s
- First error: `ERROR ~ Error executing process > 'NFCORE_BAMTOFASTQ:BAMTOFASTQ:PREPARE_INDICES:SAMTOOLS_FAIDX ([])'`
- Run id: `1f9a2ce6-4bd4-4cdb-9254-9019f7af1913`

### nf-core/callingcards 1.0.0  (`nf-callingcards-1-0-0`)
- Outcome: **HARNESS-GAP** — samplesheet: generated sheet fails the pipeline's schema_input
- Cirro run status: FAILED
- Test data: nf-core/callingcards test data PE (1.0.0)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 15:16 UTC  ·  Duration: 0m49s
- First error: `ERROR ~ ERROR: Validation of 'input' file failed!`
- Run id: `d667bca1-4fd9-4fa5-ac91-136d627829f3`

### nf-core/circdna 1.1.0  (`nf-circdna-1-1-0`)
- Outcome: **INFRA** — a process has no resolvable container / Batch job definition
- Cirro run status: FAILED
- Test data: nf-core/circdna test data PE (1.1.0)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 12:08 UTC  ·  Duration: 16m42s
- First error: `ERROR ~ Error executing process > 'NFCORE_CIRCDNA:CIRCDNA:CIRCLEFINDER (circdna_1)'`
- Run id: `90d47234-21f4-4b93-83ed-5eaba95d5829`

### nf-core/coproid 2.0.1  (`nf-coproid-2-0-1`)
- Outcome: **HARNESS-GAP** — params: process-input.json mapping / run params
- Cirro run status: FAILED
- Test data: nf-core/coproid test data PE (2.0.1)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 15:17 UTC  ·  Duration: 0m53s
- First error: `ERROR ~ Validation of pipeline parameters failed!`
- Run id: `2e469405-afad-4581-875f-fee6344c5af3`

### nf-core/denovotranscript 1.2.1  (`nf-denovotranscript-1-2-1`)
- Outcome: **UNKNOWN** — failed with no recognized signature
- Cirro run status: FAILED
- Test data: nf-core/denovotranscript test data PE (1.2.1)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 15:18 UTC  ·  Duration: 0m49s
- First error: `ERROR ~ Cannot invoke "java.nio.file.Path.getFileSystem()" because "path" is null`
- Run id: `694b9ebd-fa85-4e3b-ae3b-20dbece70e79`

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
- Nextflow build: 25.10.4
- Run started: 2026-06-14 15:18 UTC  ·  Duration: 1m03s
- Run id: `9f9ec0e8-a3de-4719-bcb8-06a02a94bb8f`

### nf-core/hgtseq 1.1.0  (`nf-hgtseq-1-1-0`)
- Outcome: **TEST-DATA-GAP** — a referenced input/genome file could not be staged (stale test data?)
- Cirro run status: FAILED
- Test data: nf-core/hgtseq test data PE (1.1.0)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 15:07 UTC  ·  Duration: 0m29s
- First error: `ERROR ~ No such file or directory: /opt/work/9ef541bfd18710d609e533da06a37c5e/None`
- Run id: `a4796210-3f7e-41f9-8c4d-e9ca36964278`

### nf-core/magmap 1.1.0  (`nf-magmap-1-1-0`)
- Outcome: **UNKNOWN** — failed with no recognized signature
- Cirro run status: FAILED
- Test data: nf-core/magmap test data PE (1.1.0)
- Nextflow build: 25.10.4
- Run started: 2026-06-14 15:18 UTC  ·  Duration: 0m36s
- First error: `ERROR ~ Unknown config attribute `params.optical_duplicate_pixel_distance` -- check config file: /opt/work/38bd79be2471041602f64b20ce98acde/nextflow-override.config`
- Run id: `41f72e0c-6206-4ae9-9779-52ff76239a28`

### nf-core/metatdenovo 1.3.0  (`nf-metatdenovo-1-3-0`)
- Outcome: **UNKNOWN** — failed with no recognized signature
- Cirro run status: FAILED
- Test data: nf-core/metatdenovo test data PE (1.3.0)
- Nextflow build: 25.10.4
- Run started: 2026-06-14 15:18 UTC  ·  Duration: 0m33s
- First error: `ERROR ~ Unknown config attribute `params.optical_duplicate_pixel_distance` -- check config file: /opt/work/7c3251ae5ad5c03996a58981ca40c16a/nextflow-override.config`
- Run id: `df8fdba3-1260-460c-be9c-19eec8a5f6a3`

### nf-core/nanoseq 3.1.0  (`nf-nanoseq-3-1-0`)
- Outcome: **PIPELINE-BUG** — a workflow process failed (pipeline tool/code)
- Cirro run status: FAILED
- Test data: nf-core/nanoseq test data PE (3.1.0)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 15:07 UTC  ·  Duration: 5m34s
- First error: `ERROR ~ Error executing process > 'NFCORE_NANOSEQ:NANOSEQ:INPUT_CHECK:SAMPLESHEET_CHECK (samplesheet.csv)'`
- Run id: `403b3c57-edd9-48d8-8eb9-e105a12b7811`

### nf-core/scrnaseq 4.1.0  (`nf-scrnaseq-4-1-0`)
- Outcome: **UNKNOWN** — failed with no recognized signature
- Cirro run status: FAILED
- Test data: nf-core/scrnaseq test data PE (4.1.0)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 14:49 UTC  ·  Duration: 0m30s
- First error: `ERROR ~ Requests specifying Server Side Encryption with AWS KMS managed keys require AWS Signature Version 4. (Service: Amazon S3; Status Code: 400; Error Code: InvalidArgument; Request ID: GCYH25P9PZ`
- Run id: `367dfacc-47e9-4292-8784-9f008bb7da3c`

### nf-core/viralmetagenome 1.1.2  (`nf-viralmetagenome-1-1-2`)
- Outcome: **UNKNOWN** — failed with no recognized signature
- Cirro run status: FAILED
- Test data: nf-core/viralmetagenome test data PE (1.1.2)
- Nextflow build: 25.04.8
- Run started: 2026-06-14 15:18 UTC  ·  Duration: 0m42s
- First error: `ERROR ~ Plugin nf-schema with version @2.7.2 does not exist in the repository`
- Run id: `1c17bafe-d2fd-4b2a-bc41-972e830db96e`

