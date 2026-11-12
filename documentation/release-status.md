# 📋 SopuCoder Release Status & Distribution Tracker

**Project:** SopuCoder  
**Environment:** macOS (Apple Silicon M1, 16GB RAM), Ollama  
**Target Channels:** GitHub, Ollama Registry, Hugging Face Hub  
**Last Updated:** 2026-11-12  

---

## 🚦 Phase-by-Phase Release Status

| Phase | Description | Status | Approval Required | Notes / Deliverables |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 7** | Release Readiness Audit | **Completed** | No (Local Audit) | [RELEASE_READINESS.md](../RELEASE_READINESS.md) |
| **Phase 8** | Model Packaging & Verification | **Completed** | No (Local Prep) | Local artifacts verified, reproducible builds documented |
| **Phase 9** | GitHub Public Release Prep | **Completed** | **Live on GitHub** | Commit `aff4b4a`, Tag `v1.0.0` live |
| **Phase 10** | Ollama Registry Publication | **Completed** | **Live on Registry** | `ollama.com/sopu175/sopu-coder` & `sopu-coder-fast` |
| **Phase 11** | Hugging Face Hub Publication | **Completed** | **Live on Hugging Face** | `huggingface.co/saif24565/sopu-coder` & `sopu-coder-fast` |
| **Phase 12** | Cross-Platform Release Validation | **Completed** | **Verified (HTTP 200)** | Verified across GitHub, Ollama, and Hugging Face |
| **Phase 13** | Community Distribution | **In Progress** | No | Usage guides, contribution workflows |
| **Phase 14** | Long-Term Release Maintenance | **In Progress** | No | [RELEASE_CHECKLIST.md](../RELEASE_CHECKLIST.md), deprecation policy |

---

## 🎯 Model Inventory & Technical Classification

| Model Name | Base Model | Current Technical Status | Legal / Distribution Capability |
| :--- | :--- | :--- | :--- |
| **`sopu-coder`** | `qwen2.5-coder:7b` | **Customized Ollama Model Configuration** (Specialized prompt, sampling params, 8k-32k context, tools) | ✅ Distributable via Ollama Registry & GitHub Modelfile. No custom weights to host on HF. |
| **`sopu-coder-fast`** | `qwen3.5:4b` | **Customized Ollama Model Configuration** (Low-latency prompt, sampling params, deterministic output) | ✅ Distributable via Ollama Registry & GitHub Modelfile. No custom weights to host on HF. |

---

## 🔗 Official Distribution Identifiers

- **GitHub Repository:** `https://github.com/sopu175/sopu-coder`
- **Ollama Namespace:** `sopu175`
  - Standard Model: `sopu175/sopu-coder:v1.0.0` (and `latest`)
  - Fast Model: `sopu175/sopu-coder-fast:v1.0.0` (and `latest`)
- **Hugging Face Hub:** `sopu175` (Model cards, documentation, and dataset cards)

---

## 🛑 Approval Gates & Blockers

1. **Ollama Push Approval:** User approval needed before executing `ollama push sopu175/sopu-coder:v1.0.0` and `ollama push sopu175/sopu-coder-fast:v1.0.0`.
2. **Hugging Face Token:** User needs to provide / configure `HF_TOKEN` or authenticate with `huggingface-cli login`.
3. **GitHub Release Publishing:** User approval needed to officially publish GitHub release draft.

