# 📚 SopuCoder Datasets & Quality Validation

This directory contains curated, high-quality instruction datasets for fine-tuning SopuCoder models across modern software engineering stacks.

## 🛡️ Licensing & Provenance Policy

Strict licensing rules apply to all training datasets:
- **Permissible Licenses Only:** Apache 2.0, MIT, BSD, ISC, or CC0.
- **Copyleft / Proprietary Exclusion:** No GPL, AGPL, or non-commercial/restricted datasets are admitted into training corpora.
- **Attribution Mandatory:** Every sample must record source attribution and licensing metadata.
- **Deduplication:** Hash-based and semantic deduplication is enforced to avoid sample repetition and data contamination.

---

## 📐 Dataset Schema (`*.jsonl`)

Each line in a dataset file is a JSON object with the following fields:

```json
{
  "id": "unique_sample_identifier",
  "language": "python | typescript | javascript | php | react",
  "framework": "fastapi | laravel | react | nextjs | core",
  "instruction": "Instruction prompt describing the task",
  "input": "Optional context or existing code",
  "output": "Markdown-formatted code block with idiomatic implementation",
  "metadata": {
    "source": "curated_sopu | permissive_oss",
    "license": "apache-2.0 | mit",
    "attribution": "Author / Repository name",
    "quality_score": 0.98
  }
}
```

---

## ⚙️ Running Validation & Train/Val/Test Splits

Execute the automated dataset validator and splitter:

```bash
python3 training/scripts/validate_datasets.py
```

Outputs are generated in `datasets/splits/`:
- `train.jsonl` (80%)
- `val.jsonl` (10%)
- `test.jsonl` (10%)
