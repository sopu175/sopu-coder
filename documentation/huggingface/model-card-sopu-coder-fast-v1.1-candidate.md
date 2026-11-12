---
language:
- en
license: apache-2.0
tags:
- code
- coding
- text-generation
- qwen2.5-coder
- mlx
- lora
- apple-silicon
- python
- typescript
- react
- nextjs
- yii2
- wordpress
- php
pipeline_tag: text-generation
inference: false
---

# 🚀 SopuCoder Fast (v1.1-candidate) — Fine-Tuned Edition

**SopuCoder Fast (v1.1-candidate)** is a candidate release of SopuCoder Fast featuring actual parameter adaptations fine-tuned on Apple Silicon Metal using MLX-LM.

---

## 🔬 Training & Architecture Details

- **Base Model:** `Qwen/Qwen2.5-Coder-1.5B-Instruct` / `mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit`
- **Method:** Low-Rank Adaptation (LoRA)
- **Trainable Layers:** 16 transformer layers
- **LoRA Hyperparameters:** Rank: 8, Scale: 20.0, Dropout: 0.0
- **Optimizer:** Adam (Learning Rate: `5e-5`, Batch Size: 1)
- **Training Steps:** 60 iterations (Loss reduced from 1.560 to 0.118 train / 0.502 validation)
- **Training Throughput:** ~395 tokens/second during training on Apple Silicon M1 (Metal Unified Memory)

---

## ⚡ Performance Benchmarks (Apple M1 16GB)

| Metric | Upstream Base (1.5B) | SopuCoder Fast (v1.0.0 4B) | SopuCoder Fast (v1.1-candidate) |
| :--- | :--- | :--- | :--- |
| **Inference Velocity** | ~35 tokens/sec | ~22.38 tokens/sec | **60.55 - 68.71 tokens/sec** |
| **Peak Memory Footprint** | ~1.5 GB | ~3.30 GB | **1.09 GB** |
| **Context Window** | 8,192 tokens | 16,384 tokens | 8,192 tokens |
| **Repetition Artifacts** | Low | None | **None** |

---

## 🛠️ Usage Instructions

### 1. Running with MLX-LM (Python / Apple Silicon)

```bash
# Install MLX-LM
pip install mlx-lm

# Run inference with LoRA adapters
python -m mlx_lm generate \
  --model mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit \
  --adapter-path training/checkpoints/sopu-coder-mlx-adapters \
  --prompt "<|im_start|>system\nYou are SopuCoder Fast.<|im_end|>\n<|im_start|>user\nWrite a React useOptimisticMutation hook.<|im_end|>\n<|im_start|>assistant\n"
```

### 2. Testing Locally with Ollama

```bash
# Build candidate model
ollama create sopu-coder-fast:v1.1-candidate -f sopu-coder-fast/Modelfile.v1.1-candidate

# Run candidate model
ollama run sopu-coder-fast:v1.1-candidate
```

---

## 📜 Provenance & Attribution

- **Base Weights:** Alibaba Cloud Qwen Team (`Qwen/Qwen2.5-Coder-1.5B-Instruct`), licensed under Apache 2.0.
- **Fine-Tuning Dataset:** `datasets/v1.1/` curated by SopuCoder open-source contributors (Apache 2.0).
- **LoRA Adapter Weights:** SopuCoder Project (Apache 2.0).

