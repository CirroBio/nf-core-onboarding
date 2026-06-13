# Onboarding report — nf-core/airrflow 5.1.0

**Cirro process:** `nf-airrflow-5-1-0`  ·  **Data type:** nf-core/airrflow
**Last validated:** 2026-06-13 20:21 UTC  ·  **Validation time:** 1.5s
**Overall:** PASS

## Local oracle (Track B)

| Check | Result | Detail |
|---|---|---|
| `form_schema` | PASS | valid JSON Schema |
| `required_reachable` | PASS | all required params mapped |
| `paths_resolve` | PASS | all mappings resolve |
| `preprocess_runs` | PASS | 2026-06-13 13:21:21,026 INFO     [PreprocessDataset] Final params (110 total): {'input': 's3://example-bucket/dataset/sample_R1.fastq.gz', 'mode': 'fastq', 'outdir': 's3://example-bucket/dataset/sample_R1.fastq.gz', 'email': 'test', 'miairr': '${projectDir}/assets/reveal/mapping_MiAIRR_BioSample_v1.3.1.tsv', 'library_generation_method': 'test', 'race_linker': 'test', 'vprimers': 'test', 'cprimers': 'test', 'vprimer_start': 0, 'cprimer_start': 0, 'cprimer_position': 'R1', 'primer_revpr': True, 'umi_position': 'R1', 'umi_length': -1, 'umi_start': 0, 'index_file': True, 'trim_fastq': True, 'adapter_fasta': 'test', 'clip_r1': 0, 'clip_r2': 0, 'three_prime_clip_r1': 0, 'three_prime_clip_r2': 0, 'trim_nextseq': True, 'save_trimmed': True, 'filterseq_q': 20, 'primer_consensus': 0.6, 'buildconsensus_maxerror': 0.1, 'buildconsensus_maxgap': 0.5, 'cluster_sets': True, 'primer_r1_maxerror': 0.2, 'primer_r2_maxerror': 0.2, 'maskprimers_align': True, 'primer_maxlen': 50, 'primer_r1_mask_mode': 'cut', 'primer_r2_mask_mode': 'cut', 'maskprimers_align_race': True, 'maskprimers_extract': True, 'primer_r1_extract_len': 0, 'primer_r2_extract_len': 0, 'assemblepairs_sequential': True, 'align_cregion': True, 'internal_cregion_sequences': 'test', 'cregion_maxlen': 100, 'cregion_maxerror': 0.3, 'cregion_mask_mode': 'tag', 'skip_alignment_filter': True, 'reference_10x': 'test', 'trust4_cell_barcode_read': 'test', 'trust4_umi_read': 'test', 'trust4_read_format': 'test', 'trust4_barcode_whitelist': 'test', 'reassign': True, 'productive_only': True, 'save_germlines': True, 'reference_fasta': 'https://raw.githubusercontent.com/nf-core/test-datasets/airrflow/database-cache/imgtdb_base.zip', 'reference_igblast': 'https://raw.githubusercontent.com/nf-core/test-datasets/airrflow/database-cache/igblast_base.zip', 'fetch_germlines': 'none', 'collapseby': 'sample_id', 'detect_contamination': True, 'remove_chimeric': True, 'clonal_threshold': 'auto', 'lineage_trees': True, 'cloneby': 'subject_id', 'crossby': 'subject_id', 'lineage_tree_builder': 'raxml', 'lineage_tree_exec': '/usr/local/bin/raxml-ng', 'singlecell': 'single_cell', 'skip_all_clones_report': True, 'skip_report_threshold': True, 'skip_clonal_analysis': True, 'genotyping': True, 'genotypeby': 'subject_id', 'genotyping_clonal_threshold': 0.2, 'single_clone_representative': True, 'novel_allele_inference': True, 'translate': True, 'embeddings': 'test', 'embedding_chain': 'H', 'use_gpu': True, 'report_rmd': '${projectDir}/assets/repertoire_comparison.Rmd', 'report_css': '${projectDir}/assets/nf-core_style.css', 'report_logo': '${projectDir}/assets/nf-core-airrflow_logo_light.png', 'report_logo_img': '${projectDir}/assets/nf-core-airrflow_logo_reports.png', 'skip_report': True, 'skip_multiqc': True, 'igenomes_ignore': True, 'igenomes_base': 's3://ngi-igenomes/igenomes/', 'custom_config_version': 'master', 'custom_config_base': 'https://raw.githubusercontent.com/nf-core/configs/master', 'config_profile_name': 'test', 'config_profile_description': 'test', 'config_profile_contact': 'test', 'config_profile_url': 'test', 'version': True, 'publish_dir_mode': 'copy', 'email_on_fail': 'test', 'plaintext_email': True, 'multiqc_title': 'test', 'max_multiqc_email_size': '25.MB', 'monochrome_logs': True, 'multiqc_config': 's3://example-bucket/dataset/sample_R1.fastq.gz', 'multiqc_logo': 'test', 'multiqc_methods_description': 'test', 'validate_params': True, 'pipelines_testdata_base_path': 'https://raw.githubusercontent.com/nf-core/test-datasets/airrflow/', 'trace_report_suffix': 'test', 'help': True, 'help_full': True, 'show_hidden': True} |

## Test data

- Source: nf-core/airrflow `-profile test` (`conf/test.config`)
- Samplesheet: (not resolved)
- Samples: 0  ·  Input files: 0

## Generation

- Reference config adapted: `scrnaseq/cellranger`

## Config

`nf-core/airrflow/5.1.0/` in this repository — the 6-file Cirro bundle
(`process-form.json`, `process-input.json`, `process-definition.json`,
`process-output.json`, `process-compute.config`, `preprocess.py`).

Registered as a custom process in the Cirro development account.
