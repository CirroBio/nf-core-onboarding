# Onboarding report — nf-core/bactmap v0.9

**Cirro process:** `nf-bactmap-v0-9`  ·  **Data type:** nf-core/bactmap
**Last validated:** 2026-06-13 20:21 UTC  ·  **Validation time:** 1.5s
**Overall:** PASS

## Local oracle (Track B)

| Check | Result | Detail |
|---|---|---|
| `form_schema` | PASS | valid JSON Schema |
| `required_reachable` | PASS | all required params mapped |
| `paths_resolve` | PASS | all mappings resolve |
| `preprocess_runs` | PASS | 2026-06-13 13:21:22,615 INFO     [PreprocessDataset] {'input': 'test', 'outdir': './results', 'email': 'test', 'reference': 'test', 'trim': True, 'save_trimmed_fail': True, 'adapter_file': '${baseDir}/assets/adapters.fas', 'subsampling_off': True, 'subsampling_depth_cutoff': 100, 'genome_size': 'test', 'remove_recombination': True, 'non_GATC_threshold': 0.5, 'rapidnj': True, 'fasttree': True, 'iqtree': True, 'raxmlng': True, 'help': True, 'publish_dir_mode': 'copy', 'email_on_fail': 'test', 'plaintext_email': True, 'monochrome_logs': True, 'tracedir': '${params.outdir}/pipeline_info', 'singularity_pull_docker_container': True, 'max_multiqc_email_size': '25.MB', 'skip_multiqc': True, 'multiqc_config': 'test', 'multiqc_title': 'test', 'enable_conda': True, 'validate_params': True, 'show_hidden_params': True, 'max_cpus': 4, 'max_memory': '16.GB', 'max_time': '240.h', 'custom_config_version': 'master', 'custom_config_base': 'https://raw.githubusercontent.com/nf-core/configs/master', 'hostnames': 'test', 'config_profile_description': 'test', 'config_profile_contact': 'test', 'config_profile_url': 'test'} |

## Test data

- Source: nf-core/bactmap `-profile test` (`conf/test.config`)
- Samplesheet: https://raw.githubusercontent.com/nf-core/test-datasets/bactmap/samplesheet.csv
- Samples: 2  ·  Input files: 4

## Generation

- Reference config adapted: `scrnaseq/cellranger`

## Config

`nf-core/bactmap/v0.9/` in this repository — the 6-file Cirro bundle
(`process-form.json`, `process-input.json`, `process-definition.json`,
`process-output.json`, `process-compute.config`, `preprocess.py`).

Registered as a custom process in the Cirro development account.
