# 🦙 Ollama Registry Publishing & Distribution Guide

This guide details how to version, tag, and publish SopuCoder models to the official [Ollama Registry](https://ollama.com).

---

## ⚠️ Important Redistribution & Artifact Warning

> [!WARNING]
> **Never upload raw `~/.ollama/models/blobs/` to GitHub or Hugging Face.**
> Ollama blobs are platform-specific and contain local internal storage states. Instead:
> 1. Publish to the **Ollama Registry** using `ollama push <username>/<model>:<tag>`.
> 2. Publish to **Hugging Face** using standard standalone `.gguf` or Safetensors files with explicit model cards.

---

## 🔑 Step 1: Authenticate with Ollama

1. Create an account on [ollama.com](https://ollama.com).
2. Check your local Ollama public key:
   ```bash
   cat ~/.ollama/id_ed25519.pub
   ```
3. Copy the key and add it to your [Ollama Account Settings -> Keys](https://ollama.com/settings/keys).

---

## 🏷️ Step 2: Tag Models with Namespace & Version

Ollama requires models to be prefixed with your username namespace to push to the public registry.

```bash
# 1. Tag Flagship Model (sopu-coder)
ollama cp sopu-coder:v1-candidate sopu175/sopu-coder:v1.0.0
ollama cp sopu-coder:v1-candidate sopu175/sopu-coder:latest

# 2. Tag Fast Model (sopu-coder-fast)
ollama cp sopu-coder-fast:v1-candidate sopu175/sopu-coder-fast:v1.0.0
ollama cp sopu-coder-fast:v1-candidate sopu175/sopu-coder-fast:latest
```

---

## 🚀 Step 3: Push to Ollama Registry

```bash
# Push versioned and latest tags for standard model
ollama push sopu175/sopu-coder:v1.0.0
ollama push sopu175/sopu-coder:latest

# Push versioned and latest tags for fast model
ollama push sopu175/sopu-coder-fast:v1.0.0
ollama push sopu175/sopu-coder-fast:latest
```

---

## 👥 How Community Developers Pull & Run

Once published, any developer in the world can run SopuCoder with a single command:

```bash
# Chat & Architecture Model
ollama run sopu175/sopu-coder

# Low-Latency Tab Autocomplete Model
ollama run sopu175/sopu-coder-fast
```
