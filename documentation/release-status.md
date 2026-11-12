# 📋 SopuCoder Release Status & Distribution Tracker

**Project:** SopuCoder  
**Environment:** macOS (Apple Silicon M1, 16GB RAM), Ollama, MLX  
**Target Channels:** GitHub, Ollama Registry, Hugging Face Hub  
**Last Updated:** 2026-11-12  

---

## 🚦 Phase-by-Phase Release Status

| Phase | Description | Status | Deliverables / URLs |
| :--- | :--- | :--- | :--- |
| **Phase 7** | Release Readiness Audit | **Completed** | [RELEASE_READINESS.md](../RELEASE_READINESS.md) |
| **Phase 8** | Model Packaging & Verification | **Completed** | Local artifacts verified, reproducible builds documented |
| **Phase 9** | GitHub Public Release | **Live on GitHub** | [github.com/sopu175/sopu-coder](https://github.com/sopu175/sopu-coder) (Tag `v1.0.0`) |
| **Phase 10** | Ollama Registry Publication | **Live on Registry** | [ollama.com/sopu175/sopu-coder](https://ollama.com/sopu175/sopu-coder) & `sopu-coder-fast` |
| **Phase 11** | Hugging Face Hub Publication | **Live on HF** | [huggingface.co/saif24565/sopu-coder](https://huggingface.co/saif24565/sopu-coder) & `sopu-coder-fast` |
| **Phase 12** | Continuous Dataset Improvement | **Completed** | `datasets/v1.1/` (36 curated samples, 10 stacks) |
| **Phase 13** | Continuous MLX LoRA Fine-Tuning | **Completed** | `EXP-004` (Train loss 0.118, Val loss 0.502, Apple M1 Metal) |
| **Phase 14** | Fine-Tuned Evaluation & Fusing | **Completed** | [EVALUATION_REPORT.md](../training/evaluation/EVALUATION_REPORT.md) (Speed: 68.7 t/s) |
| **Phase 15** | Candidate Release (v1.1-candidate) | **Live on HF** | [huggingface.co/saif24565/sopu-coder-fast-mlx-adapters](https://huggingface.co/saif24565/sopu-coder-fast-mlx-adapters) |

---

## 🎯 Model Inventory & Technical Classification

| Model Name | Version | Base Architecture | Format / Artifacts | Distribution Target |
| :--- | :--- | :--- | :--- | :--- |
| **`sopu-coder`** | `v1.0.0` | `qwen2.5-coder:7b` | Ollama Modelfile (Q4_K_M) | GitHub / Ollama Registry / Hugging Face |
| **`sopu-coder-fast`** | `v1.0.0` | `qwen3.5:4b` | Ollama Modelfile (Q4_K_M) | GitHub / Ollama Registry / Hugging Face |
| **`sopu-coder-fast-mlx-adapters`** | `v1.1-candidate` | `Qwen2.5-Coder-1.5B-Instruct` | LoRA Adapter (`adapters.safetensors`, 21MB) | Hugging Face Hub (`saif24565/sopu-coder-fast-mlx-adapters`) |
| **`sopu-coder-fast-fused`** | `v1.1-candidate` | `Qwen2.5-Coder-1.5B-Instruct` | Standalone MLX Safetensors (868MB) | Local Checkpoint (`training/checkpoints/`) |
| **`sopu-coder-fast:v1.1-candidate`** | `v1.1-candidate` | `qwen3.5:4b` | Candidate Ollama Modelfile | Local Ollama Runtime (`sopu-coder-fast:v1.1-candidate`) |

---

## 🔗 Official Distribution Identifiers

- **GitHub Repository:** `https://github.com/sopu175/sopu-coder`
- **Ollama Registry:**
  - Standard Model: `ollama run sopu175/sopu-coder:v1.0.0`
  - Fast Model: `ollama run sopu175/sopu-coder-fast:v1.0.0`
  - Candidate Modelfile: `sopu-coder-fast/Modelfile.v1.1-candidate`
- **Hugging Face Hub:**
  - Flagship: `https://huggingface.co/saif24565/sopu-coder`
  - Fast Model: `https://huggingface.co/saif24565/sopu-coder-fast`
  - Fine-Tuned LoRA Adapters: `https://huggingface.co/saif24565/sopu-coder-fast-mlx-adapters`
