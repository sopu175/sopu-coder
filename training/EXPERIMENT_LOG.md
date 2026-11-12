# 🧪 SopuCoder Experiment Log

This document records all fine-tuning runs, baseline evaluations, hyperparameter configurations, and benchmark comparisons.

---

## 📌 Experiment Registry

| Experiment ID | Base Model | Dataset Version | Framework | Target Hardware | Train Loss | Val Loss | Peak Memory | Result / Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EXP-001** (Baseline) | `qwen2.5-coder:7b` | N/A (Modelfile) | Ollama | Apple M1 | N/A | N/A | ~4.7 GB | **Evaluated (17.03 t/s)** - Production v1.0.0 |
| **EXP-002** (Baseline Fast) | `qwen3.5:4b` | N/A (Modelfile) | Ollama | Apple M1 | N/A | N/A | ~3.3 GB | **Evaluated (22.38 t/s)** - Production v1.0.0 |
| **EXP-003** (LoRA PoC) | `Qwen2.5-Coder-1.5B-Instruct-4bit` | `v1.1.0` (27 samples) | MLX-LM LoRA | Apple M1 (16GB) | `0.341` | `0.774` | **1.15 GB** | **Completed (Proof-of-Concept)** |

---

## 🔬 Detailed Analysis: Experiment EXP-003 (MLX LoRA PoC)

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
  - However, due to the small sample size (19 training samples over 50 iterations), the adapter demonstrated mild overfitting/repetition in the `behaviors()` array.
- **Promotion Verdict:** ⚠️ **DO NOT PROMOTE TO PRODUCTION YET.**  
  While the technical training and inference pipeline on Apple Silicon M1 is 100% verified and functional, full model promotion requires expanding the training dataset to 100-500 diverse samples to prevent repetition and ensure generalized code quality.
