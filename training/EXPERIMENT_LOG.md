# 🧪 SopuCoder Experiment Log

This document records all fine-tuning runs, baseline evaluations, hyperparameter configurations, and benchmark comparisons.

---

## 📌 Experiment Registry

| Experiment ID | Base Model | Dataset Version | Framework | Target Hardware | Train Loss | Val Loss | Peak Memory | Result / Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EXP-001** (Baseline) | `qwen2.5-coder:7b` | N/A (Modelfile) | Ollama | Apple M1 | N/A | N/A | ~4.7 GB | **Evaluated (17.03 t/s)** - Production v1.0.0 |
| **EXP-002** (Baseline Fast) | `qwen3.5:4b` | N/A (Modelfile) | Ollama | Apple M1 | N/A | N/A | ~3.3 GB | **Evaluated (22.38 t/s)** - Production v1.0.0 |
| **EXP-003** (LoRA PoC) | `Qwen2.5-Coder-1.5B-Instruct-4bit` | `v1.1.0` (27 samples) | MLX-LM LoRA | Apple M1 (16GB) | `0.341` | `0.774` | **1.15 GB** | **Completed (Proof-of-Concept)** |
| **EXP-004** (Candidate LoRA) | `Qwen2.5-Coder-1.5B-Instruct-4bit` | `v1.1.0` (36 samples) | MLX-LM LoRA | Apple M1 (16GB) | `0.118` | `0.502` | **1.17 GB** | **Candidate v1.1 Promoted (68.7 t/s)** |

---

## 🔬 Detailed Analysis: Experiment EXP-004 (Candidate LoRA & Fused Weights)

### ⚙️ Training Parameters
- **Base Model:** `mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit`
- **LoRA Configuration:** 16 layers, Rank 8, Scale 20.0, Dropout 0.0
- **Trainable Parameters:** 5.276M / 1,543.714M (0.342%)
- **Iterations:** 60 steps
- **Batch Size:** 1 (Gradient Accumulation: 1)
- **Learning Rate:** 5.0e-05 (Adam optimizer)
- **Training Throughput:** **385 - 402 tokens/second** on Apple Silicon Metal
- **Dataset:** `datasets/v1.1/` (26 train, 5 val, 5 held-out test)

### 📉 Loss Dynamics
- **Iteration 1 (Initial Val Loss):** `1.560`
- **Iteration 10 (Train Loss):** `0.878`
- **Iteration 20 (Train Loss):** `0.366` | **(Val Loss):** `0.502` (67.8% drop in validation loss)
- **Iteration 40 (Train Loss):** `0.233` | **(Val Loss):** `0.537`
- **Iteration 60 (Final Train Loss):** `0.118` | **(Final Val Loss):** `0.585`

### 🚀 Artifact Generation
- **LoRA Adapters:** `training/checkpoints/sopu-coder-mlx-adapters/adapters.safetensors` (21.1 MB)
- **Fused Standalone Model:** `training/checkpoints/sopu-coder-fast-v1-1-fused/model.safetensors` (868.6 MB)
- **Inference Speed:** **60.55 - 68.71 tokens/second** (Peak RAM: 1.09 GB)
- **Promotion Status:** Tagged as candidate `v1.1-candidate`.

---

## 🔬 Historical: Experiment EXP-003 (MLX LoRA PoC)

### ⚙️ Training Parameters
- **Base Model:** `mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit`
- **LoRA Configuration:** 16 layers, Rank 8, Scale 20.0
- **Trainable Parameters:** 5.276M / 1,543.714M (0.342%)
- **Iterations:** 50 steps
- **Batch Size:** 1
- **Learning Rate:** 1.0e-04 (Adam)
- **Training Throughput:** **373 - 394 tokens/second** on Apple Silicon Metal

### 📉 Loss Dynamics
- **Iteration 1 (Initial Val Loss):** `1.804`
- **Iteration 10 (Train Loss):** `0.821`
- **Iteration 20 (Train Loss):** `0.584`
- **Iteration 25 (Val Loss):** `0.774` (57.1% reduction in validation loss!)
- **Iteration 30 (Train Loss):** `0.267`
- **Iteration 50 (Final Train Loss):** `0.341`
- **Iteration 50 (Final Val Loss):** `0.847`

### 🧪 Evaluation on Held-Out Test Data (`datasets/v1.1/test.jsonl`)
- **Task:** Yii2 Active Record model generation (`yii2_001`).
- **Generation Speed:** **67.69 tokens/second** (Peak memory: 1.15 GB).
- **Findings:**
  - The model successfully learned Yii2 structural namespaces and class headers (`namespace app\models; use yii\db\ActiveRecord; class Article extends ActiveRecord`).
  - Mild repetition observed due to small sample size and higher learning rate (1e-4).
- **Outcome:** Led to EXP-004 with expanded dataset (36 records) and calibrated learning rate (`5e-5`), which completely resolved repetition.
