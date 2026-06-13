# nf-core-onboarding

Cirro pipeline configurations for onboarding [nf-core](https://nf-co.re) pipelines into the Cirro **development** account.

> **Development account only.** This repository is kept separate from the production pipeline catalog ([CirroBio/Cirro-pipelines](https://github.com/CirroBio/Cirro-pipelines)).

## Layout

Each pipeline version lives in its own directory:

```
nf-core/<pipeline>/<version>/
```

containing the Cirro custom-process configuration bundle:

| File | Purpose |
|------|---------|
| `process-definition.json` | Process metadata — id, name, executor, data type, category |
| `process-form.json` | The parameter form presented to users in Cirro |
| `process-input.json` | Maps form values and dataset files to pipeline inputs |
| `process-output.json` | Declares output files for the results view |
| `process-compute.config` | Compute and resource configuration |
| `preprocess.py` | Builds the pipeline samplesheet/manifest at launch |

## Pipelines

Configurations are added incrementally and validated against the development tenant before use. Each registered process is named with an `nf-` prefix (e.g. `nf-bamtofastq`) so the onboarded pipelines sort together in the catalog.

## Scope

Everything here targets the **development** account for testing and review. Nothing in this repository is production.
