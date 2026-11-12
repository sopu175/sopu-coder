# SopuCoder-R1: Hybrid Model Architecture & Merging Blueprint

**Project:** SopuCoder  
**Creator & Maintainer:** Md. Saiful Islam (Saif)  
**Document:** Advanced Model Merging & Hybrid Reasoning Guide  

---

## 1. Overview

Rather than relying solely on a single architecture, **SopuCoder** introduces a **Dual-Pillar Hybrid Strategy**:

1. **Syntax & Full-Stack Specialist:** `Qwen2.5-Coder-7B-Instruct` (Trained on 5.5T code tokens across 18 specialized stacks).
2. **Deep Algorithmic Reasoner:** `DeepSeek-R1-Distill-Qwen-7B` (Trained with large-scale RL for step-by-step mathematical reasoning and self-correction).

Because both models share the identical **Qwen2.5 28-layer Transformer backbone**, they can be fused mathematically using **SLERP (Spherical Linear Interpolation)** with zero tensor distortion and **zero extra RAM overhead**!

---

## 2. SLERP (Spherical Linear Interpolation) Formula

For attention and feed-forward weight tensors $W_{\text{coder}}$ and $W_{\text{R1}}$:

$$\theta = \arccos \left( \frac{\langle W_{\text{coder}}, W_{\text{R1}} \rangle}{\|W_{\text{coder}}\| \|W_{\text{R1}}\|} \right)$$

$$W_{\text{merged}} = \frac{\sin((1-t)\theta)}{\sin(\theta)} W_{\text{coder}} + \frac{\sin(t\theta)}{\sin(\theta)} W_{\text{R1}}$$

Where $t \in [0, 1]$ controls the interpolation ratio across layers:
* **Early Layers (0–10):** Higher weight on Qwen2.5-Coder ($t = 0.35$) for syntax representation and grammar.
* **Middle Layers (11–20):** 50/50 balanced blend ($t = 0.50$) to merge logical reasoning into programming semantics.
* **Late Layers (21–28):** Higher weight on DeepSeek-R1 ($t = 0.65$) for coherent final completion and edge-case verification.

The ready-to-run recipe is provided in `training/merges/slerp_r1_coder_7b.yaml`.

---

## 3. How to Run SopuCoder-R1 Locally (Ollama)

```bash
# Pull the base R1 reasoning weights (4.7 GB)
ollama pull deepseek-r1:7b

# Build SopuCoder-R1 with production software engineering parameters
ollama create sopu-coder-r1 -f sopu-coder-r1/Modelfile

# Run and test live reasoning
ollama run sopu-coder-r1 "Design a distributed rate-limiter using Redis token bucket in TypeScript"
```

---

## 4. Hardware Impact: RAM & Speed Comparison

| Model | Foundation | Disk / RAM Size | Speed (M1 16GB) | Reasoning (<think>) | Best Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`sopu-coder`** | Qwen2.5-Coder 7B | 4.7 GB / ~5.2 GB | ~15-18 tok/s | Implicit | High-volume daily coding, Next.js 15, Laravel 11 |
| **`sopu-coder-r1`** | DeepSeek-R1 + Qwen 7B | 4.7 GB / ~5.2 GB | ~15-17 tok/s | Explicit (<think>) | Hard algorithmic logic, bug root-cause analysis |
| **`sopu-coder-fast`** | Qwen3.5 4B / Qwen 1.5B | 3.3 GB / ~2.1 GB | ~30-50+ tok/s | Minimal | Real-time inline tab-completions & quick edits |
