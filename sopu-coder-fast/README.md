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
| **Base Architecture** | Qwen 3.5 4B & DeepSeek-R1 logic |
| **Context Window** | 16,384 tokens (default 8,192 ctx) |
| **Memory Footprint** | ~3.3 GB RAM |
| **Generation Speed** | ~22.38 tokens/second on Apple Silicon M1 |
| **Fine-Tuned Standalone (1.5B)** | **68.71 tokens/second** at **1.09 GB RAM** |
| **Temperature** | 0 (deterministic, high precision) |
| **Top P / Top K** | 0.85 / 25 |
| **Repeat Penalty** | 1.15 |
| **Language Support** | Bilingual (English & Bengali / বাংলা) |
| **Native Tool Calling** | 100% native OpenAI-compatible structured tool calls via dedicated streaming parser |

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

## 🤖 Coding Agent & IDE Configurations

### Autonomous Terminal Agents (OpenCode, Claude Code, Hermes Agent, OpenClaw)
`sopu175/sopu-coder-fast` has native streaming tool support, making it the premier local engine for coding agents:

```bash
# OpenCode
ollama launch opencode --model sopu175/sopu-coder-fast

# Claude Code
ollama launch claude --model sopu175/sopu-coder-fast

# Hermes Agent
ollama launch hermes --model sopu175/sopu-coder-fast

# OpenClaw
ollama launch openclaw --model sopu175/sopu-coder-fast
```

### IDE Tab Autocomplete (Continue for VS Code / Cursor)

Add to `~/.continue/config.json`:

```json
{
  "tabAutocompleteModel": {
    "title": "SopuCoder Fast",
    "provider": "ollama",
    "model": "sopu175/sopu-coder-fast:latest"
  }
}
```

---

## 📄 License & Attribution
- **Creator Attribution:** Created and maintained by Md. Saiful Islam (Saif).
- **Foundation Model:** Alibaba / Qwen Team (Apache 2.0).
- **SopuCoder Engine:** Apache 2.0.
