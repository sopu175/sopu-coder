# 🚀 SopuCoder v1.0.0 — Official Public Release

We are thrilled to announce the official **v1.0.0 release of SopuCoder**, an open-source, community-driven AI coding model ecosystem designed for privacy-first, local-first software engineering.

---

## 🌟 What is SopuCoder?
SopuCoder brings production-grade coding intelligence to local developer workstations, eliminating dependence on costly or privacy-invasive cloud APIs.

### 🧠 Available Models:
1. **`sopu-coder` (Flagship Model)**
   - **Base:** `qwen2.5-coder:7b`
   - **Focus:** Complex full-stack development, multi-file architecture, deep refactoring, and strict typing.
   - **Context Window:** Up to 32,768 tokens.
   - **Tested Speed:** ~17 tokens/sec on Apple Silicon M1.

2. **`sopu-coder-fast` (Lightweight Model)**
   - **Base:** `qwen3.5:4b`
   - **Focus:** Ultra-low-latency inline completions, tab autocompletion, syntax fixes, and single-function generation.
   - **Context Window:** Up to 16,384 tokens.
   - **Tested Speed:** ~22.4 - 25+ tokens/sec on Apple Silicon M1.

---

## ⚡ Quick Start with Ollama

Run immediately with zero configuration:

```bash
# Chat & Architecture Model
ollama run sopu175/sopu-coder:v1.0.0

# Low-Latency Tab Autocomplete Model
ollama run sopu175/sopu-coder-fast:v1.0.0
```

---

## 📦 What's Included in This Release:
- 🧪 **Empirical Benchmark Suite:** 6 evaluation pillars covering Code Generation, Debugging, Refactoring, Multi-File Sync, Tool Calling, and Latency.
- 📚 **Validated Datasets:** Permissively licensed seed instruction sets across Python, TypeScript, React, JS, and PHP 8.x with automated AST validation.
- 🛠️ **Fine-Tuning Pipeline:** End-to-end 4-bit QLoRA training recipes, LoRA merger, and GGUF quantization workflow.
- 🤝 **Community Governance:** Code of Conduct, RFC guidelines, and GitHub Issue/PR templates.

---

## 📄 License & Attribution
SopuCoder is open-source software under the [Apache License 2.0](LICENSE). Upstream foundation models are attributed to Alibaba Cloud under Tongyi Qianwen terms.

