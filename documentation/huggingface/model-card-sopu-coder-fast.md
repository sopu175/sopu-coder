---
language:
- en
- python
- typescript
- javascript
- php
license: apache-2.0
tags:
- code
- coding
- text-generation
- qwen2.5
- ollama
- gguf
- autocomplete
- low-latency
pipeline_tag: text-generation
inference: false
---

# ⚡ SopuCoder Fast (v1.0.0)

**SopuCoder Fast** is an ultra-low-latency coding model optimized for instant tab autocomplete, real-time function generation, lint fixes, and seamless execution on consumer laptops and edge hardware.

## 🚀 Key Specifications

- **Base Architecture:** Qwen 2.5 Coder 1.5B
- **Context Length:** 16,384 tokens
- **Target Use Cases:** Real-time IDE inline completions, syntax diagnostics, single-function generation
- **Throughput:** ~22.4 - 25+ tokens/second on CPU / Apple Silicon
- **Quantization Formats:** GGUF (`Q4_K_M`, `Q5_K_M`), Safetensors

---

## 🦙 Quick Run with Ollama

```bash
ollama run sopu175/sopu-coder-fast:v1.0.0
```

## 🛠️ VS Code & Cursor IDE Autocomplete Configuration

Using the [Continue](https://continue.dev) extension:

```json
{
  "tabAutocompleteModel": {
    "title": "SopuCoder Fast",
    "provider": "ollama",
    "model": "sopu175/sopu-coder-fast:v1.0.0"
  }
}
```

---

## 📄 License & Attribution
- SopuCoder Fast configuration & prompts: Apache License 2.0.
- Base foundation model: Qwen 2.5 Coder 1.5B (Alibaba Cloud).
