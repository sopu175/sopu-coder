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

## 🎯 Target Milestones for Future Versions

### Milestone v1.1.0 (Current Phase: Dataset & Proof-of-Concept)
- [x] Dataset audit and gap identification.
- [x] Multi-stack expansion (Next.js, Node.js, Yii2, WordPress, Python Async/Pytest, TS Branded types).
- [x] Versioned splits in `datasets/v1.1/` (Train: 19, Val: 4, Test: 4).
- [ ] Approval and execution of MLX-LM LoRA Proof-of-Concept on Apple M1.
- [ ] Post-training benchmark evaluation vs baseline.

### Milestone v1.2.0 (Scaled Corpus & Multi-Turn Refactoring)
- Scale dataset to 500+ curated software engineering samples.
- Multi-turn conversational refactoring and git patch application.
- Automated HumanEval and MBPP pass@1 reporting.

### Milestone v2.0.0 (Dedicated Base Weight Quantizations)
- Full adapter fusion into 16-bit standalone weights.
- Multi-format distribution (GGUF Q4_K_M, Q5_K_M, Q8_0, AWQ, EXL2).
- Native IDE plugins (VS Code, Cursor, Neovim) pre-configured for SopuCoder endpoints.
