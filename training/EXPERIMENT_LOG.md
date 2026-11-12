# 🧪 SopuCoder Experiment Log

This document records all fine-tuning runs, baseline evaluations, hyperparameter configurations, and benchmark comparisons.

---

## 📌 Experiment Registry

| Experiment ID | Base Model | Dataset Version | Framework | Target Hardware | Train Loss | Val Loss | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EXP-001** (Baseline) | `qwen2.5-coder:7b` | N/A (Modelfile) | Ollama | Apple M1 | N/A | N/A | **Evaluated (17.03 t/s)** |
| **EXP-002** (Baseline Fast) | `qwen3.5:4b` | N/A (Modelfile) | Ollama | Apple M1 | N/A | N/A | **Evaluated (22.38 t/s)** |
| **EXP-003** (PoC Proposed) | `Qwen2.5-Coder-7B-Instruct` | `v1.1.0` (27 samples) | MLX-LM LoRA | Apple M1 (16GB) | Pending | Pending | **Planned / Ready for Approval** |

---

## 🔬 Benchmark Baseline Metrics (v1.0.0 Pre-Training)

- **Code Generation (React/TS AbortController):** 657 tokens, 17.08 t/s
- **Debugging (Python Concurrency Race):** 386 tokens, 16.35 t/s
- **Refactoring (PHP 8.2+ DTO & Match):** 680 tokens, 17.55 t/s
- **Multi-File Sync (FastAPI & TS Fetch):** 760 tokens, 17.61 t/s
- **Tool Calling (SQL JSON):** 82 tokens, 16.48 t/s
- **Latency (Knapsack DP O(W)):** 610 tokens, 17.12 t/s
