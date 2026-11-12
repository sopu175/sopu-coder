---
language:
- en
license: apache-2.0
tags:
- code
- coding
- text-generation
- qwen2.5
- ollama
- gguf
- python
- typescript
- javascript
- php
- react
- fastapi
- laravel
pipeline_tag: text-generation
inference: false
---

# 🧠 SopuCoder (v1.0.0)

**SopuCoder** is an open-source, community-driven AI coding assistant engineered for local-first software development, deep architectural refactoring, and multi-language web engineering.

## 🚀 Key Specifications

- **Base Architecture:** Qwen 2.5 Coder 7B
- **Context Length:** 32,768 tokens
- **Target Stacks:** Python (FastAPI/Django), TypeScript, React 18/19, JavaScript (ESNext/Node), Modern PHP 8.x (Laravel/PSR-12)
- **Quantization Formats:** GGUF (`Q4_K_M`, `Q8_0`), 16-bit Safetensors

---

## 📊 Benchmark Evaluation Summary (v1.0.0)

Evaluated across 6 rigorous software engineering dimensions:

| Test Dimension | Task Description | Result | Latency / Speed |
| :--- | :--- | :--- | :--- |
| **Code Generation** | `useDebouncedAsync` Hook with AbortController & generics | **Passed** | 17.08 tokens/s (44.3s) |
| **Debugging** | Concurrency race condition resolution in `TTLCache` | **Passed** | 16.35 tokens/s (24.5s) |
| **Refactoring** | Imperative order processor to modern PHP 8.2+ OOP service | **Passed** | 17.55 tokens/s (39.8s) |
| **Multi-File Sync** | FastAPI endpoint & TypeScript client synchrony | **Passed** | 17.61 tokens/s (43.9s) |
| **Tool Calling** | Structured JSON tool call (`execute_sql_query`) | **Passed** | 16.48 tokens/s (5.5s) |
| **Throughput** | Algorithmic DP 0/1 Knapsack with space optimization | **Passed** | 17.12 tokens/s (36.0s) |

---

## 🦙 Quick Run with Ollama

```bash
ollama run sopu175/sopu-coder:v1.0.0
```

## 🐍 Usage with Hugging Face `transformers`

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "saif24565/sopu-coder"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

messages = [
    {"role": "system", "content": "You are SopuCoder, an elite software engineer."},
    {"role": "user", "content": "Implement an async queue worker with backpressure in Python."}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.2)

print(tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

---

## 📄 License & Attribution
- SopuCoder configuration, prompts, and evaluation suite: Apache License 2.0.
- Base foundation model: Qwen 2.5 Coder (Alibaba Cloud).

