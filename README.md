# sampleGen

`sampleGen` is a research-oriented music sample generation project.

The current priority is the generation module:

- `v1`: `text -> sample`
- `v2`: `text + key -> sample`

The transposition module is planned, but not the current implementation focus.

## Project Layout

```text
sampleGen/
├── configs/                 # Experiment and data configuration files
├── data/                    # Local dataset workspace
│   ├── interim/
│   ├── metadata/
│   ├── processed/
│   └── raw/
├── memory/                  # Project notes, plans, and rollback records
├── outputs/                 # Checkpoints, logs, samples, reports
├── scripts/                 # CLI entry scripts
├── src/samplegen/           # Core project package
│   ├── data/
│   ├── evaluation/
│   ├── models/
│   ├── training/
│   └── utils/
└── tests/                   # Basic test placeholders
```

## Current Goal

Build a clean research workflow that supports:

1. dataset definition and preprocessing
2. prompt normalization
3. `v1` baseline training
4. `v2` key-conditioned training
5. later `L_key` experiments and ablations

## Quick Start

Create a virtual environment and install the project in editable mode after dependencies are decided:

```bash
pip install -e .
```

For now, the command-line entry points are placeholders used to keep the project structure stable while implementation is added incrementally.
