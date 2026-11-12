# 📝 Changelog

All notable changes to the **SopuCoder** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [v1.0.0] - 2026-11-12

### Added
- **Global Release Configurations:** Finalized `sopu-coder` (Qwen 2.5 Coder 7B base) and `sopu-coder-fast` (Qwen 3.5 4B base) for Ollama Registry publication.
- **Hugging Face Model Cards:** Complete metadata, benchmark numbers, and prompt templates for Hugging Face Hub (`documentation/huggingface/`).
- **Ollama Distribution Guide:** Step-by-step registry authentication and namespace publishing instructions (`documentation/ollama-distribution-guide.md`).
- **Release Readiness Audit:** 10-point audit verifying licensing, local model execution, and distribution readiness (`RELEASE_READINESS.md`).

---

## [v0.5.0] - 2026-11-12

### Added
- **Fine-Tuning Pipeline:** 4-bit QLoRA training harness with PEFT and TRL (`training/fine-tuning/train_lora.py`).
- **Hyperparameter Configuration:** Declarative training setup in `training/fine-tuning/config.yaml`.
- **GGUF Export Script:** Automated LoRA adapter merging and GGUF quantization workflow (`training/fine-tuning/export_gguf.py`).
- **Pipeline Documentation:** Complete hardware requirements and step-by-step training instructions.

---

## [v0.3.0] - 2026-11-12

### Added
- **Curated Multi-Language Seed Datasets:** High-quality instruction-code pairs for Python, TypeScript, React, JavaScript, and modern PHP 8.x (`datasets/`).
- **Dataset Quality Validator:** AST syntax validation, permissive license filtering, deduplication, and deterministic 80/10/10 train/val/test splitter (`training/scripts/validate_datasets.py`).
- **Dataset Documentation:** Provenance, licensing policy, and schema specification (`datasets/README.md`).

---

## [v0.2.0] - 2026-11-12

### Added
- **Automated Benchmark Runner:** Python evaluation runner testing against local Ollama API endpoints (`training/evaluation/benchmark_runner.py`).
- **6-Category Evaluation Suite:** Rigorous test cases covering Code Generation, Debugging, Refactoring, Multi-File Sync, Tool Calling, and Latency (`training/evaluation/benchmarks.json`).
- **Comparative Benchmark Report:** Empirical results comparing `sopu-coder:v1-candidate` and `sopu-coder-fast:v1-candidate` (`training/evaluation/BENCHMARK_REPORT.md`).
- **Methodology Documentation:** Testing guidelines and metrics calculation (`documentation/evaluation-methodology.md`).

---

## [v0.1.0] - 2026-11-12

### Added
- **Initial Ecosystem Foundation:** Root README with vision and goals, folder structure, `.gitkeep` files for empty directories.
- **Licensing Framework:** Apache 2.0 source code license and upstream attribution notices (`LICENSE`).
- **Initial Modelfiles:** Main model and fast model Ollama configurations.
- **Roadmap & Contributing Docs:** Initial roadmap and governance framework (`documentation/`).
