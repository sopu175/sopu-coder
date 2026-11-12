<div align="center">

# 🚀 SopuCoder

**Next-Generation Open-Source AI Coding Assistant for Modern Developers**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Ollama](https://img.shields.io/badge/Ollama-Ready-black?logo=ollama)](https://ollama.com)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-yellow)](https://huggingface.co)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](documentation/contributing.md)

[Vision](#-vision) •
[Key Goals](#-key-goals) •
[Available Models](#-available-models) •
[Ollama Setup](#-quick-start-with-ollama) •
[Hugging Face](#-hugging-face-distribution) •
[Repository Structure](#-repository-structure) •
[Contributing](#-community--contribution)

</div>

---

## 🌟 Vision

**SopuCoder** is built to bridge the gap between heavy cloud-dependent coding assistants and privacy-focused local development. Our vision is to provide developers, teams, and open-source contributors with **accessible, high-performance, and privacy-first coding models** optimized to run seamlessly on consumer hardware and local developer workstations.

Whether you are writing full-stack web applications, refactoring complex codebases, or seeking ultra-fast inline code completions, SopuCoder delivers state-of-the-art coding capabilities directly on your local machine.

---

## 🎯 Key Goals

- 💻 **Local-First & Private:** Run locally without sending proprietary code or sensitive intellectual property to external cloud APIs.
- ⚡ **Ultra-Low Latency:** Engineered for both fast inline code completion (instant feedback) and deep reasoning / architectural refactoring.
- 🌐 **Modern Full-Stack Specialization:** Native fluency in contemporary tech stacks including **TypeScript, React, Python, JavaScript, and PHP**.
- 🛠️ **Open Source & Extensible:** Open weights, fully documented dataset preparation pipelines, and reproducible fine-tuning recipes.
- 🔌 **Seamless Tooling Integration:** Native compatibility with Ollama, llama.cpp, vLLM, Hugging Face Transformers, and popular IDE extensions (VS Code, Cursor, Neovim).

---

## 🧠 Available Models

SopuCoder offers tailored variants designed for distinct workflows and hardware constraints:

| Model | Target Use Case | Recommended Hardware | Context Window | Formats |
| :--- | :--- | :--- | :--- | :--- |
| **`sopu-coder`** | Architectural design, multi-file reasoning, deep refactoring, code explanation | 16GB+ RAM / Apple Silicon (M1/M2/M3) / 8GB+ VRAM | 16k - 32k tokens | GGUF (Q4/Q8), Safetensors |
| **`sopu-coder-fast`** | Instant inline tab-completion, syntax checks, quick function generation | 8GB RAM / Low-spec laptops / Edge devices | 8k - 16k tokens | GGUF (Q4/Q5), Safetensors |

---

## 🦙 Quick Start with Ollama

SopuCoder is fully integrated with [Ollama](https://ollama.com) for effortless local deployment.

### 1. Run via Ollama Registry (Once Published)

```bash
# Run standard SopuCoder for general programming & reasoning
ollama run sopucoder/sopu-coder

# Run lightweight SopuCoder Fast for ultra-fast completions
ollama run sopucoder/sopu-coder-fast
```

### 2. Build Locally with Modelfile

You can easily build custom quantizations or local builds from the source repository:

```bash
# Clone the repository
git clone https://github.com/saifdc-dev/SopuCoder.git
cd SopuCoder

# Build standard SopuCoder
cd sopu-coder
ollama create sopu-coder -f Modelfile
ollama run sopu-coder

# Or build SopuCoder Fast
cd ../sopu-coder-fast
ollama create sopu-coder-fast -f Modelfile
ollama run sopu-coder-fast
```

### 3. Integrate with IDEs
Configure your IDE extension (e.g., **Continue**, **Twinny**, or **CodeGPT**) to point to your local Ollama endpoint:
- **Base URL:** `http://localhost:11434`
- **Model:** `sopu-coder` (for Chat) or `sopu-coder-fast` (for Autocomplete)

---

## 🤗 Hugging Face Distribution

Pre-trained weights, quantized GGUF checkpoints, and dataset artifacts are distributed through Hugging Face.

### Model Hub Repositories
- **Base & Fine-Tuned Weights:** `https://huggingface.co/sopucoder/sopu-coder`
- **GGUF Quantizations:** `https://huggingface.co/sopucoder/sopu-coder-GGUF`
- **Fast Variant:** `https://huggingface.co/sopucoder/sopu-coder-fast-GGUF`

### Usage with Python (`transformers`)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "sopucoder/sopu-coder"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

prompt = "Write a React hook for debouncing an input field value with TypeScript types."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.2)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## 📁 Repository Structure

```text
SopuCoder/
├── README.md                   # Project overview and quick start guide
├── documentation/             # Project governance, roadmap, and guides
│   ├── model-roadmap.md        # Architecture roadmap and release milestones
│   ├── contributing.md         # Community contribution guidelines
│   └── governance.md           # Project governance and RFC process
├── sopu-coder/                 # Standard model configuration and Modelfile
│   ├── Modelfile               # Ollama configuration
│   ├── README.md               # Model-specific documentation
│   └── benchmarks/             # Benchmark evaluations
├── sopu-coder-fast/            # Fast model configuration and Modelfile
│   ├── Modelfile               # Ollama configuration for fast variant
│   ├── README.md               # Fast model documentation
│   └── benchmarks/             # Latency and throughput benchmarks
├── datasets/                   # Training and evaluation datasets
│   ├── python/                 # Python dataset curation
│   ├── typescript/             # TypeScript dataset curation
│   ├── javascript/             # JavaScript dataset curation
│   ├── react/                  # React component & hook datasets
│   └── php/                    # Modern PHP (Laravel, Symfony, Core) datasets
└── training/                   # Model training and fine-tuning pipelines
    ├── fine-tuning/            # Unsloth, LoRA, and QLoRA recipes
    ├── scripts/                # Data preprocessing, filtering, and tokenization
    └── evaluation/             # Automated evaluation suites (HumanEval, etc.)
```

---

## 📊 Datasets & Training Philosophy

SopuCoder adheres to strict data curation standards:
- **High-Quality Code Extraction:** Strict filtering for modern idioms, clean syntax, comprehensive type annotations, and unit tests.
- **Deduplication & Sanitization:** Removal of benchmark test leaks, license-violating code, sensitive credentials, and boilerplate.
- **Targeted Domain Coverage:**
  - **Python:** Modern asynchronous patterns, FastAPI, data pipelines, standard library mastery.
  - **TypeScript & React:** Modern React 18/19 patterns (Hooks, Context, Server Components), robust typing, state management.
  - **PHP:** Modern PHP 8.x features, Laravel, type declarations, clean MVC architecture.
  - **JavaScript:** ESNext standards, Node.js runtimes, clean modular architecture.

---

## 🤝 Community & Contribution

We welcome contributions from developers, researchers, and AI enthusiasts worldwide! Here is how you can get involved:

1. **Contribute Datasets:** Share clean, high-quality code snippets and instruction pairs under `datasets/`.
2. **Improve Prompts & Modelfiles:** Test and refine system prompts and parameters under `sopu-coder/` and `sopu-coder-fast/`.
3. **Enhance Training Recipes:** Optimize LoRA/QLoRA training configurations and evaluation benchmarks in `training/`.
4. **Report Bugs & Suggest Features:** Open an issue or join our community discussions.

Please review our [Contributing Guidelines](documentation/contributing.md) and [Model Roadmap](documentation/model-roadmap.md) before submitting a Pull Request.

---

## 📄 License

SopuCoder is open-source software licensed under the [Apache License 2.0](LICENSE).

---

<div align="center">
  <sub>Built with ❤️ by the SopuCoder Community. Empowering developers everywhere with local AI.</sub>
</div>
