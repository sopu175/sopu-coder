# 🛠️ SopuCoder Continuous Training Guide

This guide details the fine-tuning options, workflows, and best practices for training SopuCoder models across local Apple Silicon (M1) and cloud NVIDIA GPUs.

---

## 💻 Environment Assessment & Framework Matrix

| Framework | Platform | Supported Architectures | Memory Footprint (7B 4-bit) | Feasibility on Apple M1 (16GB) |
| :--- | :--- | :--- | :--- | :--- |
| **MLX-LM (`mlx_lm.lora`)** | Apple Silicon (Metal) | Qwen2.5-Coder (1.5B, 7B, 14B) | ~5.8 GB Unified Memory | ✅ **Highly Feasible & Native** |
| **PEFT / TRL (`train_lora.py`)** | NVIDIA GPU (CUDA) | Qwen2.5-Coder, DeepSeek | ~6.5 GB VRAM (via bitsandbytes NF4) | ❌ Requires NVIDIA GPU / Cloud |
| **PyTorch MPS** | Apple Silicon (Metal) | Standard CausalLM | ~14-16 GB (FP16 only) | ⚠️ High risk of OOM / swapping |

> [!WARNING]
> **Qwen3.5 Architecture Note:**
> The `qwen3.5:4b` model contains a multimodal vision/clip projector and MoE/hybrid components. Standard causal text fine-tuning harnesses do not support it without custom vision-language adaptations. **Fine-tuning must focus on the Qwen2.5-Coder series.**

---

## 🏃 Local Apple Silicon (M1) Fine-Tuning Workflow via MLX

### 1. Install MLX-LM in `.venv`

```bash
uv pip install mlx mlx-lm -p .venv
```

### 2. Prepare Training Dataset Format

MLX requires a directory with `train.jsonl` and `valid.jsonl` containing formatted text:

```bash
python3 training/scripts/prepare_mlx_data.py
```

### 3. Run LoRA Proof-of-Concept (PoC)

```bash
.venv/bin/python -m mlx_lm.lora \
  --model Qwen/Qwen2.5-Coder-7B-Instruct \
  --data datasets/v1.1/mlx_data \
  --batch-size 1 \
  --lora-layers 16 \
  --iters 100 \
  --learning-rate 1e-4 \
  --adapter-path training/checkpoints/sopu-coder-mlx-adapters
```

### 4. Merge Adapters and Export GGUF

```bash
.venv/bin/python -m mlx_lm.fuse \
  --model Qwen/Qwen2.5-Coder-7B-Instruct \
  --adapter-path training/checkpoints/sopu-coder-mlx-adapters \
  --save-path training/checkpoints/sopu-coder-v1-1-merged
```

---

## ☁️ Cloud GPU Training (NVIDIA A10G / RTX 4090)

For large-scale dataset training (>1,000 steps):

```bash
pip install -r training/fine-tuning/requirements.txt
python3 training/fine-tuning/train_lora.py --config training/fine-tuning/config.yaml
```
