# ⚡ SopuCoder Fast (Low-Latency Autocomplete Model)

**Model:** `sopu-coder-fast`  
**Creator & Maintainer:** Md. Saiful Islam (Saif)  
**Base Architecture:** Alibaba Qwen3.5 4B  
**License:** Apache 2.0  
**Ollama Registry:** [`sopu175/sopu-coder-fast`](https://ollama.com/sopu175/sopu-coder-fast)  
**Hugging Face:** [`saif24565/sopu-coder-fast`](https://huggingface.co/saif24565/sopu-coder-fast)  

---

## 🚀 Overview

**SopuCoder Fast** is an ultra-low-latency coding model optimized for real-time inline code completions, tab assistance, instant syntax diagnostics, single-function generation, and smooth execution on low-spec laptops and edge hardware.

---

## ⚙️ Specifications

| Parameter | Value |
| :--- | :--- |
| **Base Model** | `qwen3.5:4b` |
| **Context Window** | 16,384 tokens |
| **Memory Footprint** | ~3.3 GB RAM |
| **Generation Speed** | ~22.38 tokens/second on Apple Silicon M1 |
| **Fine-Tuned Standalone (1.5B)** | **68.71 tokens/second** at **1.09 GB RAM** |
| **Temperature** | 0.1 (high precision, low variance) |
| **Top P / Top K** | 0.9 / 30 |
| **Repeat Penalty** | 1.05 |

---

## 🦙 Quickstart

```bash
# Pull and run directly from Ollama Registry
ollama run sopu175/sopu-coder-fast:v1.1.0

# Or track latest
ollama run sopu175/sopu-coder-fast:latest
```

## 🛠️ Build Locally

```bash
# Navigate to this directory and build with Modelfile
ollama create sopu-coder-fast -f Modelfile

# Run interactive session
ollama run sopu-coder-fast
```

---

## 💻 IDE Tab Autocomplete Configuration (Continue for VS Code / Cursor)

Add to `~/.continue/config.json`:

```json
{
  "tabAutocompleteModel": {
    "title": "SopuCoder Fast",
    "provider": "ollama",
    "model": "sopu175/sopu-coder-fast:v1.1.0"
  }
}
```

---

## 📄 License & Attribution
- **Creator Attribution:** Created and maintained by Md. Saiful Islam (Saif).
- **Foundation Model:** Alibaba / Qwen Team (Apache 2.0).
- **SopuCoder Engine:** Apache 2.0.
