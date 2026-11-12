---
language:
- en
license: apache-2.0
tags:
- code
- coding
- text-generation
- qwen3.5
- ollama
- gguf
- python
- typescript
- javascript
- autocomplete
- low-latency
- tool-calling
pipeline_tag: text-generation
inference: false
---

# ⚡ SopuCoder Fast (v1.1.0)

**SopuCoder Fast** is an ultra-low-latency coding model created and maintained by **Md. Saiful Islam (Saif)**, utilizing Alibaba's **Qwen3.5 4B** foundation model, optimized for real-time IDE inline completions, instant syntax diagnostics, and low-spec laptop execution.

---

## 🚀 Key Specifications

- **Creator & Maintainer:** Md. Saiful Islam (Saif)
- **Base Architecture:** Alibaba Qwen3.5 4B & DeepSeek-R1 logic
- **Context Length:** 16,384 tokens
- **Inference Speed:** ~22.4 - 25+ tokens/second on Apple Silicon
- **Fine-Tuned Standalone Candidate (1.5B):** **68.7 tokens/second** at **1.09 GB RAM**
- **Language Support:** Bilingual (English & Bengali / বাংলা)
- **Target Stacks:** Autonomous coding agents (OpenCode, Claude Code, Hermes Agent, OpenClaw), real-time IDE inline completions, quick function generation, lint fixes.
- **Native Tool Calling:** 100% native OpenAI-compatible structured tool calls via dedicated streaming parser.

---

## 🤖 Coding Agent & IDE Quickstart

### Autonomous Coding Agents
```bash
# OpenCode
ollama launch opencode --model sopu175/sopu-coder-fast

# Claude Code
ollama launch claude --model sopu175/sopu-coder-fast

# Hermes Agent
ollama launch hermes --model sopu175/sopu-coder-fast
```

---

## 🦙 Quick Run with Ollama

```bash
# Run latest release
ollama run sopu175/sopu-coder-fast:v1.1.0

# Or run latest tag
ollama run sopu175/sopu-coder-fast:latest
```

## 🛠️ VS Code & Cursor IDE Autocomplete Configuration

Using the [Continue](https://continue.dev) extension (`~/.continue/config.json`):

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
- **Foundation Model:** Built upon Alibaba's Qwen3.5 4B (Apache License 2.0).
- **SopuCoder Engine:** Licensed under the Apache License 2.0.
