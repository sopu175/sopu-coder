# 🗺️ SopuCoder Model Improvement Roadmap

A cyclical engineering framework for advancing SopuCoder from evaluated prompt configurations into continuously fine-tuned domain-specialized weights.

---

## 🔄 The SopuCoder Continuous Improvement Cycle

```text
┌────────────────────────────────────────────────────────┐
│ 1. Community & Curated Dataset Ingestion (datasets/)   │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. Automated Schema, License & Syntax Audit (AST)     │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. MLX / QLoRA LoRA Fine-Tuning Execution              │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. Isolated Benchmark Regression Testing (HumanEval+)  │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 5. Candidate Validation & Adapter Merging              │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 6. Public Release (Ollama Registry & Hugging Face Hub) │
└────────────────────────────────────────────────────────┘
```

---

## 🎯 Version Progression & Roadmap

### Milestone v1.0.0 (Production Release — Completed ✅)
- [x] Initial Modelfile engineering for `sopu-coder` (7B) and `sopu-coder-fast` (4B).
- [x] 6-category benchmark evaluation harness (`training/evaluation/benchmark_runner.py`).
- [x] Published to GitHub (`sopu175/sopu-coder`), Ollama Registry (`sopu175`), and Hugging Face (`saif24565`).

### Milestone v1.1.0 (Continuous Fine-Tuning & Candidate Packaging — Completed ✅)
- [x] Complete dataset audit and expansion to 36 high-signal instruction records (`datasets/v1.1/`).
- [x] Coverage across 10 critical web and backend technologies (Next.js, Node.js, Yii2, WordPress, Python Async/Pytest, TS Branded types, React 19, PHP 8.3/Laravel 11).
- [x] LoRA fine-tuning execution (**EXP-004**) on Apple Silicon M1 Metal (Train Loss 0.118, Val Loss 0.502).
- [x] Adapter fusion into standalone MLX weights (`training/checkpoints/sopu-coder-fast-v1-1-fused`).
- [x] Empirical evaluation on held-out test data showing **60.55 - 68.71 tokens/sec** at **1.09 GB RAM**.
- [x] Published LoRA adapters to Hugging Face: `saif24565/sopu-coder-fast-mlx-adapters`.
- [x] Candidate Ollama Modelfile created: `sopu-coder-fast/Modelfile.v1.1-candidate`.

### Milestone v1.2.0 (Scaled Corpus & Multi-Turn Refactoring)
- Expand curated dataset to 250+ production-grade software engineering samples.
- Multi-turn conversational refactoring and unified diff/patch application.
- Automated HumanEval and MBPP pass@1 reporting against candidate weights.

### Milestone v2.0.0 (Flagship 7B Model Weights Fine-Tuning)
- Perform full 4-bit QLoRA fine-tuning on `Qwen2.5-Coder-7B-Instruct` using Cloud GPU (A100 / H100) or 32GB+ Unified Memory.
- Direct GGUF quantizations (`Q4_K_M`, `Q5_K_M`, `Q8_0`) uploaded as native Ollama blobs and Hugging Face binaries.
- Native IDE plugins (VS Code / Cursor / Neovim) pre-configured with SopuCoder autocomplete shortcuts.
