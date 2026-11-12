# 🔍 SopuCoder Project & Environment Audit (Phase 0)

**Audit Date:** 2026-11-12  
**Auditor:** SopuCoder Autonomous Engineering Agent  
**Maintainer:** Md. Saiful Islam (Saif)  

---

## 1. System & Hardware Baseline
- **Operating System:** macOS (Version 26.6.2, Darwin Kernel)
- **Architecture:** Apple Silicon M1 (ARM64)
- **RAM:** 16 GB Unified Memory (17,179,869,184 bytes)
- **Storage:** 926 GB total, 422 GB available (~53% capacity)
- **Inference Runtime:** Ollama (Local Metal acceleration enabled)
- **ML Training Framework:** MLX / MLX-LM (`mlx` 0.32.4, `mlx-lm` 0.32.2) via Python 3.11/3.15 venv (`.venv/`)

---

## 2. Model Inventory & Status
| Identifier | Role | Upstream Base | Format / State | Memory Footprint | Speed |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`sopu-coder:latest` / `v1.0.0`** | Primary Software Engineer | `qwen2.5-coder:7b` | Ollama Modelfile (Q4_K_M) | ~4.7 GB RAM | ~17.03 t/s |
| **`sopu-coder-fast:latest` / `v1.0.0`** | Low-Latency Autocomplete | `qwen3.5:4b` | Ollama Modelfile (Q4_K_M) | ~3.3 GB RAM | ~22.38 t/s |
| **`sopu-coder-fast-mlx-adapters`** | Candidate Fine-Tuned LoRA | `Qwen2.5-Coder-1.5B-Instruct` | LoRA Adapter (Safetensors) | ~1.17 GB RAM | **68.71 t/s** |
| **`sopu-coder-fast-fused`** | Standalone Fused Candidate | `Qwen2.5-Coder-1.5B-Instruct` | Standalone MLX Weights | ~1.09 GB RAM | **60.55 t/s** |
| **`sopu-coder-fast:v1.1-candidate`** | Candidate Ollama Model | `qwen3.5:4b` | Candidate Ollama Modelfile | ~3.3 GB RAM | Verified |

---

## 3. Remote Distribution & Authentication Channels
- **GitHub:** `git@github.com:sopu175/sopu-coder.git` (Active branch: `main`, Authenticated via SSH, Tags: `v0.1.0` - `v1.0.0`)
- **Hugging Face Hub:** Authenticated as `saif24565`
  - Model Card (Main): `https://huggingface.co/saif24565/sopu-coder` (200 OK)
  - Model Card (Fast): `https://huggingface.co/saif24565/sopu-coder-fast` (200 OK)
  - LoRA Adapter Repo: `https://huggingface.co/saif24565/sopu-coder-fast-mlx-adapters` (200 OK)
- **Ollama Registry:** Authenticated as `sopu175`
  - `ollama.com/sopu175/sopu-coder` (200 OK)
  - `ollama.com/sopu175/sopu-coder-fast` (200 OK)

---

## 4. Discovered Safety & Capability Deficits
1. **Model Identity Missing in SYSTEM Prompts:**
   The base Modelfiles currently instruct the model that it is an elite AI software engineer, but lack explicit creator attribution to **Md. Saiful Islam (Saif)** and foundation acknowledgment of **Alibaba Cloud / Qwen Team**.
2. **Tool-Calling Disconnect:**
   When asked queries requiring live external data (e.g., weather, live docs), the model defaults to generating raw unexecuted JSON (`webfetch` with invalid OpenWeatherMap API keys) because no client-side tool execution dispatch loop exists.
3. **Dataset Scope:**
   Datasets currently cover 36 curated software engineering records (`datasets/v1.1/`). Expansion is required for interactive frontends (Three.js, GSAP) and full-stack SaaS architectures.

