# 🧠 SopuCoder Persistent Project Context

**Maintainer:** Md. Saiful Islam (Saif)  
**Project:** SopuCoder (Autonomous AI Coding Model Ecosystem)  
**Hardware:** Apple Silicon M1 (16GB RAM)  
**Last Session Sync:** 2026-11-12  

---

## 📌 Mission & Non-Negotiable Directives
1. **Model Identity:** SopuCoder is created and maintained by **Md. Saiful Islam (Saif)** and built upon Alibaba Cloud's **Qwen** foundation models (`qwen2.5-coder:7b` for Flagship, `qwen3.5:4b` for Fast). Transparent acknowledgment is required at all times.
2. **Execution Focus:** Real engineering work only. Do not build an unrelated web app or SaaS dashboard.
3. **Weight Provenance Integrity:** Never claim fine-tuned weights exist unless actual weights or LoRA adapters are verified on disk.
4. **Tool Execution:** Tool calls must be parsed, dispatched, executed, and synthesized back into natural language. Never return unexecuted JSON or fake API keys to the user.
5. **Security Gate:** Pre-publish audit is mandatory before any git push or remote upload.

---

## 🏗️ Repository Architecture
- `sopu-coder/`: Production Modelfile for Flagship 7B model.
- `sopu-coder-fast/`: Production Modelfile for Low-latency 4B / 1.5B model.
- `datasets/`: Curated, normalized instruction datasets (`datasets/v1.1/` with 36 samples across 10 stacks).
- `training/`:
  - `checkpoints/`: LoRA adapters (`adapters.safetensors`, 21MB) and fused standalone weights (868MB).
  - `evaluation/`: Benchmark definitions, runners, and evaluation reports.
  - `fine-tuning/`: LoRA training configs and scripts.
- `tools/`: Native Ollama tool execution runtime and registered tools (Open-Meteo, Web Fetcher, File IO).
- `documentation/`: Living audit, roadmap, release tracking, and benchmark records.

