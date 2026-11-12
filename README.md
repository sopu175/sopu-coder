<div align="center">

# 🚀 SopuCoder

**Next-Generation Open-Source AI Coding Assistant Ecosystem**

*Created & Maintained by **Md. Saiful Islam (Saif)***  
*Built upon Alibaba Cloud's **Qwen** Foundation Models*

[![GitHub Release](https://img.shields.io/github/v/release/sopu175/sopu-coder?color=blue&logo=github)](https://github.com/sopu175/sopu-coder/releases)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Ollama Registry](https://img.shields.io/badge/Ollama%20Registry-sopu175-black?logo=ollama)](https://ollama.com/sopu175/sopu-coder)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-saif24565-yellow)](https://huggingface.co/saif24565)
[![Apple Silicon Metal](https://img.shields.io/badge/Apple%20Silicon-MLX%20Metal%20Native-orange?logo=apple)](https://github.com/ml-explore/mlx)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](documentation/contributing.md)

[Overview](#-overview) •
[Creator & Attribution](#-creator--foundation-attribution) •
[Model Family](#-model-family) •
[Quickstart](#-quickstart-with-ollama) •
[Tool Calling](#-native-tool-calling--agent-runtime) •
[Benchmarks](#-18-domain-baseline-benchmarks) •
[Fine-Tuning on Apple Silicon](#-fine-tuning-on-apple-silicon-mlx) •
[IDE Integration](#-ide--editor-integrations) •
[Device Profiler & Compatibility](#-hardware-profiler--cross-device-compatibility) •
[Repository Structure](#-repository-structure)

</div>

---

## 🌟 Overview

**SopuCoder** is an open-source, privacy-first AI coding model ecosystem designed to bridge the gap between cloud-dependent proprietary coding assistants and local-first software engineering. 

Running locally on developer workstations (Apple Silicon, Linux, and Windows) with zero data leakage, SopuCoder delivers state-of-the-art coding assistance across **18 specialized software engineering domains**—including modern TypeScript/React 19, Next.js App Router, Python FastAPI/SQLAlchemy 2.0, PHP 8.3/Laravel 11, Three.js, GSAP motion choreography, multi-tenant PostgreSQL RLS, and native tool execution.

---

## 👤 Creator & Foundation Attribution

- **Project Creator & Maintainer:** **Md. Saiful Islam (Saif)**
- **Foundation Architectures:** Built upon Alibaba Cloud's world-class **Qwen** foundation series:
  - **SopuCoder (Flagship 7B):** Built on `Qwen2.5-Coder 7B`
  - **SopuCoder Fast (Lightweight):** Built on `Qwen3.5 4B` & fine-tuned `Qwen2.5-Coder 1.5B`
- **Attribution Policy:** SopuCoder transparently acknowledges Alibaba Cloud / Qwen Team as the foundation creators and maintains full Apache 2.0 open-source licensing compliance.

---

## 🧠 Model Family

| Model | Base Architecture | Role & Target Workflows | Context Window | Throughput (Apple M1) | RAM Footprint | Distribution Channels |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`sopu-coder`** | `Qwen2.5-Coder 7B` | Primary software architect, complex refactoring, multi-file code review, security defense | 32,768 tokens | ~17.03 tokens/sec | ~4.7 GB RAM | Ollama (`sopu175/sopu-coder`), GitHub, Hugging Face |
| **`sopu-coder-fast`** | `Qwen3.5 4B` | Real-time inline tab-completions, syntax checks, instant single-function generation | 16,384 tokens | ~22.38 tokens/sec | ~3.3 GB RAM | Ollama (`sopu175/sopu-coder-fast`), GitHub, Hugging Face |
| **`sopu-coder-fast-fused`** | `Qwen2.5-Coder 1.5B` (MLX LoRA) | Ultra-high velocity edge execution, zero reasoning delay, lightweight laptops | 8,192 tokens | **68.71 tokens/sec** | **1.09 GB RAM** | Hugging Face (`saif24565/sopu-coder-fast-mlx-adapters`), MLX Standalone |

---

## 🦙 Quickstart with Ollama

SopuCoder is published directly to the [Ollama Registry](https://ollama.com/sopu175).

### 1. Run Flagship SopuCoder (7B)
```bash
# Pull and run SopuCoder v1.1.0 (Full-stack architecture)
ollama run sopu175/sopu-coder:v1.1.0

# Or track latest
ollama run sopu175/sopu-coder:latest
```

### 2. Run SopuCoder Fast (Low-Latency)
```bash
# Pull and run SopuCoder Fast v1.1.0 (Real-time completion)
ollama run sopu175/sopu-coder-fast:v1.1.0

# Or track latest
ollama run sopu175/sopu-coder-fast:latest
```

### 3. Build Locally from Modelfiles
```bash
# Clone the repository
git clone https://github.com/sopu175/sopu-coder.git
cd SopuCoder

# Build Flagship
ollama create sopu-coder -f sopu-coder/Modelfile

# Build Fast
ollama create sopu-coder-fast -f sopu-coder-fast/Modelfile
```

---

## 🛠️ Native Tool-Calling & Agent Runtime

SopuCoder includes a native, keyless tool execution engine in `tools/` that eliminates raw JSON leaks and fake API keys:

- **Keyless Live Weather:** Integrates with **Open-Meteo** (`api.open-meteo.com`) for worldwide real-time geocoding and weather without requiring any API keys.
- **Safe Web Fetch:** Validates URLs, blocks SSRF/loopback attacks, and respects timeouts.
- **Natural Language Synthesis:** Dispatches tool results back to SopuCoder for a clean, human-readable response.

```bash
# Ask a real-time question with live tool execution
python -m tools.cli "What is the weather today in Dhaka?"

# Verbose mode (inspect executed tool calls)
python -m tools.cli -v "What is the weather today in Tokyo?"

# Interactive agent session
python -m tools.cli --interactive
```

---

## 📊 18-Domain Baseline Benchmarks

SopuCoder v1.1.0 has been evaluated across 18 software engineering domains in [benchmarks/baseline_suite.json](benchmarks/baseline_suite.json).

| Category | Benchmark Test Title | SopuCoder 7B Speed | Fine-Tuned 1.5B Speed | Maturity Level |
| :--- | :--- | :--- | :--- | :--- |
| **JavaScript & TypeScript** | Nominal Type-Safe Generic Event Bus | 16.75 t/s | **68.71 t/s** | Level 5 (Production) |
| **React** | Compound Modal with ARIA & Context | 17.67 t/s | **64.20 t/s** | Level 5 (Production) |
| **Next.js App Router** | Server Action with Zod & Revalidation | 16.34 t/s | **60.55 t/s** | Level 5 (Production) |
| **Node.js** | Backpressure-Managed NDJSON Stream | 17.10 t/s | 65.00 t/s | Level 5 (Production) |
| **PHP & Laravel 11** | Idempotent Queued Job with Enums | 16.90 t/s | 61.20 t/s | Level 5 (Production) |
| **Yii2 & WordPress** | REST API Nonces & `$wpdb->prepare` | 17.20 t/s | 59.80 t/s | Level 4 (Advanced) |
| **Python Backend** | SQLAlchemy 2.0 Async Generic Repository | 17.00 t/s | 62.40 t/s | Level 5 (Production) |
| **Three.js** | Procedural ShaderMaterial Swarm | 16.80 t/s | 58.10 t/s | Level 4 (Advanced) |
| **React Three Fiber** | Interactive Mesh Viewer with Drei | 17.10 t/s | 60.10 t/s | Level 4 (Advanced) |
| **GSAP Motion** | ScrollTrigger Pinning with `@gsap/react` | 16.90 t/s | 59.50 t/s | Level 4 (Advanced) |
| **SaaS Architecture** | PostgreSQL Row-Level Security (RLS) | 17.40 t/s | 63.00 t/s | Level 5 (Production) |
| **Database Migrations** | Zero-Downtime Column Rename Plan | 17.50 t/s | 61.80 t/s | Level 5 (Production) |
| **Technical SEO** | Dynamic JSON-LD Structured Data & OG | 16.80 t/s | 64.00 t/s | Level 5 (Production) |
| **Testing** | Vitest Hook Suite with Fake Timers | 17.20 t/s | 66.50 t/s | Level 5 (Production) |
| **Debugging** | Concurrency Lock Race Condition Fix | 17.00 t/s | 67.00 t/s | Level 5 (Production) |
| **Refactoring** | Imperative to Modern PSR-12 OOP | 16.80 t/s | 63.50 t/s | Level 5 (Production) |
| **Multi-File Sync** | FastAPI Schema + TypeScript Client Parity | 17.10 t/s | 61.00 t/s | Level 5 (Production) |
| **Tool Calling** | Structured Open-Meteo Tool Invocation | 17.30 t/s | **Native Engine** | Level 5 (Production) |

👉 *Full analysis available in [documentation/BASELINE_BENCHMARKS.md](documentation/BASELINE_BENCHMARKS.md) and [documentation/CAPABILITY_MATRIX.md](documentation/CAPABILITY_MATRIX.md).*

---

## ⚡ Fine-Tuning on Apple Silicon (MLX)

SopuCoder features native, reproducible Low-Rank Adaptation (LoRA) fine-tuning pipelines optimized for Apple Silicon Metal Unified Memory:

- **Run ID:** `EXP-004`
- **Framework:** `mlx-lm` (Metal native)
- **Training Throughput:** **385 - 402 tokens/second**
- **Loss Reduction:** Training loss dropped from 0.878 to **0.118**; Validation loss dropped from 1.560 to **0.502**.
- **Adapter Checkpoints:** Published on Hugging Face at [`saif24565/sopu-coder-fast-mlx-adapters`](https://huggingface.co/saif24565/sopu-coder-fast-mlx-adapters).

```bash
# Run inference with LoRA adapters via MLX
pip install mlx-lm
python -m mlx_lm generate \
  --model mlx-community/Qwen2.5-Coder-1.5B-Instruct-4bit \
  --adapter-path training/checkpoints/sopu-coder-mlx-adapters \
  --prompt "<|im_start|>system\nYou are SopuCoder Fast.<|im_end|>\n<|im_start|>user\nWrite a React useOptimisticMutation hook.<|im_end|>\n<|im_start|>assistant\n"
```

---

## 💻 IDE & Editor Integrations

### Coding Agent Platforms (OpenCode, Claude Code, Hermes Agent, OpenClaw)

SopuCoder Fast features native support for automated coding agents and agentic CLI workflows:

```bash
# OpenCode (Autonomous terminal coding agent)
ollama launch opencode --model sopu175/sopu-coder-fast

# Claude Code
ollama launch claude --model sopu175/sopu-coder-fast

# Hermes Agent
ollama launch hermes --model sopu175/sopu-coder-fast

# OpenClaw
ollama launch openclaw --model sopu175/sopu-coder-fast
```

For OpenCode configuration (`~/.config/opencode/opencode.json`):
```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "ollama/sopu175/sopu-coder-fast:latest",
  "small_model": "ollama/sopu175/sopu-coder-fast:latest",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "http://127.0.0.1:11434/v1"
      }
    }
  }
}
```

### VS Code & Cursor (via Continue)
Add SopuCoder to `~/.continue/config.json`:
```json
{
  "models": [
    {
      "title": "SopuCoder (Flagship 7B)",
      "provider": "ollama",
      "model": "sopu175/sopu-coder:v1.1.0"
    }
  ],
  "tabAutocompleteModel": {
    "title": "SopuCoder Fast (Autocomplete)",
    "provider": "ollama",
    "model": "sopu175/sopu-coder-fast:v1.1.0"
  }
}
```

### Figma MCP Design-to-Code Workflow
SopuCoder is architected for official Figma MCP (`https://mcp.figma.com/mcp`). Read the complete setup in [documentation/AGENT_LIMITATION_AUDIT.md](documentation/AGENT_LIMITATION_AUDIT.md).

---

## 📱 Hardware Profiler & Cross-Device Compatibility

SopuCoder is designed to run anywhere — from low-end 2GB/4GB edge devices and Raspberry Pi, to 8GB/16GB everyday laptops, up to high-memory workstations and in-browser WebGPU environments.

For in-depth architectural research and scaling plans, see [RESEARCH_CAPACITY_AND_DEVICE_EXPANSION.md](documentation/RESEARCH_CAPACITY_AND_DEVICE_EXPANSION.md).

### Automatic Hardware Profiling
Run the built-in zero-dependency hardware profiler on your machine to automatically discover the best SopuCoder tier for your hardware:

```bash
python3 scripts/device_profiler.py
```

### Multi-Tier Device Support Matrix

| Tier | Model Variant | Disk Size (Q4_K_M) | Minimum RAM | Target Devices | Ideal Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1 (Edge / Nano)** | `sopu-coder-nano` (0.5B / 1.5B) | **400 MB - 1.1 GB** | **2 GB - 4 GB** | Android (Termux), Raspberry Pi 4/5, Old Core-i3 PCs, WebGPU | Offline inline autocomplete, basic script fixing |
| **Tier 2 (Fast)** | `sopu-coder-fast` (4B) | **2.2 GB - 3.3 GB** | **4 GB - 8 GB** | 8GB M1/M2/M3 Mac, Budget Windows/Linux laptops | Rapid code reviews, fast tab completion |
| **Tier 3 (Flagship)** | `sopu-coder` (7B) | **4.7 GB** | **12 GB - 16 GB** | 16GB Apple Silicon, RTX 3060/4060, Dev Desktops | Full-stack software architecture, agent loop |
| **Tier 4 (Pro / Max)** | `sopu-coder-pro` (14B / 32B) | **9.0 GB - 19.5 GB** | **24 GB - 64 GB** | M-series Max/Ultra, RTX 3090/4090, Cloud V100/A100 | Enterprise repos, deep algorithmic synthesis |

---

## 📁 Repository Structure

```text
SopuCoder/
├── README.md                           # Main documentation & quickstart
├── LICENSE                             # Apache 2.0 Open-Source License
├── CHANGELOG.md                        # Version release changelog
├── release-manifest.json               # Pre-publish verified file manifest
├── release-audit-report.json           # Pre-publish security scan report
├── sopu-coder/                         # SopuCoder Flagship 7B Modelfile & docs
│   ├── Modelfile                       # Ollama configuration
│   └── README.md                       # Model specifications
├── sopu-coder-fast/                    # SopuCoder Fast Modelfile & docs
│   ├── Modelfile                       # Ollama configuration
│   └── README.md                       # Model specifications
├── tools/                              # Native Tool Calling & Agent Runtime
│   ├── agent_runtime.py                # Multi-turn Ollama dispatch loop
│   ├── registry.py                     # Tool registry with Open-Meteo & Web Fetch
│   └── cli.py                          # Command-line interface with tool execution
├── benchmarks/                         # 18-Domain Baseline Benchmark Suite
│   ├── baseline_suite.json             # 18-domain prompt & evaluation criteria
│   └── run_benchmarks.py               # Automated benchmark execution engine
├── datasets/                           # Curated training & evaluation datasets
│   ├── v1.1/                           # Versioned datasets (Train: 26, Val: 5, Test: 5)
│   ├── DATASET_SOURCE_REGISTRY.md      # Approved & rejected dataset sources
│   └── DATASET_SELECTION_REPORT.md     # Ingestion strategy for v1.2.0
├── training/                           # Continuous fine-tuning pipelines
│   ├── checkpoints/                    # MLX LoRA adapters & fused weights
│   ├── evaluation/                     # Detailed evaluation reports
│   └── EXPERIMENT_LOG.md               # Empirical training loss logs
├── documentation/                      # Architectural audits and guides
│   ├── BASELINE_BENCHMARKS.md          # 18-domain evaluation analysis
│   ├── CAPABILITY_MATRIX.md            # Maturity matrix across 18 domains
│   ├── AGENT_LIMITATION_AUDIT.md       # Figma MCP & IDE integration audit
│   └── MODEL_IMPROVEMENT_ROADMAP.md    # Multi-version roadmap (v1.0 -> v2.0)
└── scripts/
    └── pre_publish_audit.py            # Mandatory pre-push credential & license scanner
```

---

## 🤝 Community & Governance

We welcome open-source contributions!
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for code and dataset contribution guidelines.
- Review [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards.
- Check [MODEL_IMPROVEMENT_ROADMAP.md](documentation/MODEL_IMPROVEMENT_ROADMAP.md) for planned features.

---

## 📄 License

SopuCoder is open-source software licensed under the **[Apache License 2.0](LICENSE)**.  
Base foundation models are developed by the **Alibaba Cloud / Qwen Team** under the Apache License 2.0.

<div align="center">
  <sub>Built with ❤️ by <b>Md. Saiful Islam (Saif)</b> and the SopuCoder Open-Source Contributors.</sub>
</div>
