# 🧠 SopuCoder (Flagship 7B Model)

**Model:** `sopu-coder`  
**Creator & Maintainer:** Md. Saiful Islam (Saif)  
**Base Architecture:** Alibaba Cloud Qwen2.5-Coder 7B  
**License:** Apache 2.0  
**Ollama Registry:** [`sopu175/sopu-coder`](https://ollama.com/sopu175/sopu-coder)  
**Hugging Face:** [`saif24565/sopu-coder`](https://huggingface.co/saif24565/sopu-coder)  

---

## 🚀 Overview

**SopuCoder** is the primary coding and software engineering engine of the SopuCoder suite. It is tailored for developers and engineering teams requiring deep architectural reasoning, multi-file refactoring, defensive security checks, and modern full-stack implementation across TypeScript, React 19, Next.js, Python FastAPI, PHP 8.3 Laravel, and database migrations.

---

## ⚙️ Specifications

| Parameter | Value |
| :--- | :--- |
| **Base Model** | `qwen2.5-coder:7b` |
| **Context Window** | 16,384 tokens |
| **Quantization** | Q4_K_M (Ollama default) / 16-bit Safetensors |
| **Memory Footprint** | ~4.7 GB RAM |
| **Generation Speed** | ~17.03 tokens/second on Apple Silicon M1 |
| **Temperature** | 0 (deterministic, low hallucination) |
| **Top P / Repeat Penalty** | 0.90 / 1.10 |
| **Language Support** | Bilingual (English & Bengali / বাংলা) |
| **Architecture** | Dual-Mode Template (Clean conversational chat in terminal, structured tools when invoked) |

---

## 🦙 Quickstart

```bash
# Pull and run directly from Ollama Registry
ollama run sopu175/sopu-coder:v1.1.0

# Or track latest
ollama run sopu175/sopu-coder:latest
```

## 🛠️ Build Locally

```bash
# Navigate to this directory and build with Modelfile
ollama create sopu-coder -f Modelfile

# Run interactive session
ollama run sopu-coder
```

---

## 🤖 Coding Agent & IDE Configurations

### Continue (VS Code / Cursor)
Add to `~/.continue/config.json`:

```json
{
  "models": [
    {
      "title": "SopuCoder (Flagship 7B)",
      "provider": "ollama",
      "model": "sopu175/sopu-coder:latest"
    }
  ]
}
```

### Coding Agents (OpenCode, Claude Code, Hermes Agent)
For autonomous multi-file edits and terminal coding tasks, we recommend `sopu175/sopu-coder-fast`:
```bash
ollama launch opencode --model sopu175/sopu-coder-fast
ollama launch claude --model sopu175/sopu-coder-fast
```

---

## 📄 License & Attribution
- **Creator Attribution:** Created and maintained by Md. Saiful Islam (Saif).
- **Foundation Model:** Alibaba Cloud / Qwen Team (Apache 2.0).
- **SopuCoder Engine:** Apache 2.0.
