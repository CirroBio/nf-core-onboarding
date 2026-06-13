# Onboarding report — nf-core/circdna 1.1.0

**Cirro process:** `nf-circdna-1-1-0`  ·  **Data type:** nf-core/circdna
**Last validated:** 2026-06-13 20:21 UTC  ·  **Validation time:** 1.5s
**Overall:** PASS

## Local oracle (Track B)

| Check | Result | Detail |
|---|---|---|
| `form_schema` | PASS | valid JSON Schema |
| `required_reachable` | PASS | all required params mapped |
| `paths_resolve` | PASS | all mappings resolve |
| `preprocess_runs` | PASS | 2026-06-13 13:21:27,529 INFO     [PreprocessDataset] Final params (58 total): {"input": "s3://example-bucket/dataset/sample_R1.fastq.gz", "input_format": "test", "bam_sorted": true, "save_sorted_bam": true, "outdir": "s3://example-bucket/dataset/sample_R1.fastq.gz", "email": "test", "multiqc_title": "test", "circle_identifier": "test", "genome": "test", "fasta": "s3://example-bucket/dataset/sample_R1.fastq.gz", "igenomes_ignore": true, "save_reference": false, "bwa_index": "s3://example-bucket/dataset/sample_R1.fastq.gz", "skip_qc": false, "skip_multiqc": false, "skip_markduplicates": false, "keep_duplicates": true, "save_markduplicates_bam": true, "clip_r1": 1, "clip_r2": 1, "three_prime_clip_r1": 1, "three_prime_clip_r2": 1, "trim_nextseq": 1, "skip_trimming": false, "save_trimmed": false, "save_merged_fastq": false, "save_circle_map_intermediate": false, "save_circle_finder_intermediate": false, "save_unicycler_intermediate": false, "aa_data_repo": "s3://example-bucket/dataset/sample_R1.fastq.gz", "aa_cngain": "4.5", "mosek_license_dir": "s3://example-bucket/dataset/sample_R1.fastq.gz", "reference_build": "test", "cnvkit_cnn": "test", "custom_config_version": "master", "custom_config_base": "https://raw.githubusercontent.com/nf-core/configs/master", "config_profile_name": "test", "config_profile_description": "test", "config_profile_contact": "test", "config_profile_url": "test", "max_cpus": 16, "max_memory": "128.GB", "max_time": "240.h", "help": true, "version": true, "publish_dir_mode": "copy", "email_on_fail": "test", "plaintext_email": true, "max_multiqc_email_size": "25.MB", "monochrome_logs": true, "hook_url": "test", "multiqc_config": "s3://example-bucket/dataset/sample_R1.fastq.gz", "multiqc_logo": "test", "multiqc_methods_description": "test", "validate_params": true, "validationShowHiddenParams": true, "validationFailUnrecognisedParams": true, "validationLenientMode": true} |

## Test data

- Source: nf-core/circdna `-profile test` (`conf/test.config`)
- Samplesheet: https://raw.githubusercontent.com/nf-core/test-datasets/circdna/samplesheet/samplesheet.csv
- Samples: 3  ·  Input files: 6

## Generation

- Reference config adapted: `scrnaseq/cellranger`

## Config

`nf-core/circdna/1.1.0/` in this repository — the 6-file Cirro bundle
(`process-form.json`, `process-input.json`, `process-definition.json`,
`process-output.json`, `process-compute.config`, `preprocess.py`).

Registered as a custom process in the Cirro development account.
