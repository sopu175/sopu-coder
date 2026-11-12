# 🚀 SopuCoder Fine-Tuning Pipeline

This directory contains the complete end-to-end Supervised Fine-Tuning (SFT) pipeline for SopuCoder models using QLoRA, PEFT, and TRL.

> [!IMPORTANT]
> **Modelfile vs. Weight Fine-Tuning:**
> Modelfiles define runtime inference parameters, sampling options, and system prompts on top of existing base weights.
> Weight fine-tuning (this pipeline) permanently adjusts the neural network weights on curated instruction corpora to learn new reasoning patterns, code conventions, and syntax structures.

---

## 🛠️ Hardware Requirements & Environment Setup

- **GPU:** 1x NVIDIA GPU with at least 12GB VRAM (T4, RTX 3060/4070/4090, A10G, A100) or Google Colab (T4 GPU).
- **CUDA:** Version 12.1+ recommended.
- **Python:** 3.10 - 3.12.

### Install Dependencies

```bash
pip install -r training/fine-tuning/requirements.txt
```

---

## 🏃 Fine-Tuning Workflow

### 1. Configure Hyperparameters
Inspect and adjust [config.yaml](config.yaml):
- Base model: `Qwen/Qwen2.5-Coder-7B-Instruct` (or `1.5B` for fast variant)
- Learning rate: `2e-4`
- LoRA rank (`r`): `16`, alpha: `32`
- Batch size and gradient accumulation

### 2. Run Training

```bash
python3 training/fine-tuning/train_lora.py --config training/fine-tuning/config.yaml
```

The script will:
- Load base model in 4-bit NormalFloat (NF4).
- Inject LoRA adapters into attention and MLP projection layers.
- Train on `datasets/splits/train.jsonl` with evaluation on `datasets/splits/test.jsonl`.
- Save adapter weights to `./training/checkpoints/sopu-coder-lora/final_adapter`.

---

## 📦 Weight Merging & GGUF Quantization

### 1. Merge LoRA Adapters into Base Model

```bash
python3 training/fine-tuning/export_gguf.py \
  --base_model Qwen/Qwen2.5-Coder-7B-Instruct \
  --adapter_dir ./training/checkpoints/sopu-coder-lora/final_adapter \
  --merged_output ./training/checkpoints/sopu-coder-merged
```

### 2. Convert to GGUF via `llama.cpp`

```bash
# Clone llama.cpp if not present
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && make -j

# Convert Hugging Face weights to GGUF
python3 convert_hf_to_gguf.py ../training/checkpoints/sopu-coder-merged --outfile ../sopu-coder.gguf --outtype f16

# Quantize to 4-bit K-Medium
./llama-quantize ../sopu-coder.gguf ../sopu-coder-Q4_K_M.gguf Q4_K_M
```

### 3. Register and Run with Ollama

```bash
ollama create sopu-coder -f sopu-coder/Modelfile.release
ollama run sopu-coder
```
