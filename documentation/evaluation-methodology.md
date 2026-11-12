# 🔬 SopuCoder Evaluation & Benchmark Methodology

This document defines the formal testing methodology used to benchmark SopuCoder candidate configurations against upstream base models.

## 🎯 Evaluation Objectives
A successful coding model must excel beyond surface-level system prompts. Our evaluation tests 6 core pillars:

1. **Code Generation:** Complete, functional, syntactically correct implementations with edge-case handling.
2. **Debugging:** Identification of subtle bugs (concurrency races, memory leaks, off-by-one errors) and sound root-cause fixes.
3. **Refactoring:** Converting imperative legacy code to clean OOP/functional paradigms adhering to standards (PSR-12, PEP 8, TypeScript strictness).
4. **Multi-File Consistency:** Shared interface alignment, parameter order parity, and endpoint synchronization between backend and frontend code.
5. **Tool Calling & Structured Output:** Strict adherence to function schemas and pure JSON serialization.
6. **Inference Latency & Throughput:** Evaluation of tokens generated per second and response latency across device profiles.

---

## 🚀 Running the Benchmarks

To execute the test suite on any Ollama model:

```bash
# Benchmark SopuCoder standard candidate
python3 training/evaluation/benchmark_runner.py --model sopu-coder:v1-candidate

# Benchmark SopuCoder fast candidate
python3 training/evaluation/benchmark_runner.py --model sopu-coder-fast:v1-candidate

# Benchmark upstream base model for comparison
python3 training/evaluation/benchmark_runner.py --model qwen2.5-coder:7b
```

Results are automatically saved to `training/evaluation/results/` as structured JSON and Markdown summary reports.

