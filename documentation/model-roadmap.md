# 🗺️ SopuCoder Model & Project Roadmap

This document outlines the progressive release milestones and architectural trajectory of the SopuCoder ecosystem.

## 🎯 Release Milestones

| Version | Milestone | Scope & Deliverables | Status |
| :--- | :--- | :--- | :--- |
| **v0.1.0** | Initial Project Foundation | Repository structure, root README, initial Modelfiles, gitkeep structure, licensing & attribution framework. | **Completed** |
| **v0.2.0** | Model Configurations & Benchmarks | Candidate model verification (`sopu-coder:v1-candidate`, `sopu-coder-fast:v1-candidate`), benchmark evaluation test suite (generation, debugging, refactoring, latency). | **Completed** |
| **v0.3.0** | Validated Datasets | Multi-language datasets (Python, TypeScript, React, JS, PHP), license audits, deduplication, and test/train splits. | Planned |
| **v0.5.0** | Fine-Tuning Pipeline | LoRA/QLoRA recipes, tokenization scripts, training configurations, and loss/accuracy logging. | Planned |
| **v1.0.0** | Public Multi-Channel Release | Validated weights on Hugging Face, versioned models on Ollama Registry, comprehensive documentation. | Target |

---

## 🔬 Benchmark Dimensions for v0.2.0

1. **Code Generation:** Evaluating accuracy on functional synthesis and clean syntax.
2. **Debugging & Bug Fixing:** Detecting and resolving subtle edge-case errors.
3. **Refactoring & Clean Architecture:** Assessing adherence to modularity, PEP 8, PSR-12, and modern React patterns.
4. **Multi-File Consistency:** Dependency imports, type sharing, and consistent interfaces.
5. **Inference Latency:** Time to first token (TTFT) and token generation speed on CPU and GPU.

