# 🤝 Contributing to SopuCoder

We are thrilled that you are interested in contributing to SopuCoder! As an open-source, community-driven local coding model ecosystem, your ideas, datasets, benchmarks, and feedback make SopuCoder better for developers worldwide.

---

## 🧭 Contribution Areas

You can contribute in several key areas:
1. **Curated Datasets (`datasets/`):** Submit clean instruction-code pairs with explicit permissive licenses (Apache 2.0, MIT).
2. **Prompts & Modelfiles (`sopu-coder/`, `sopu-coder-fast/`):** Improve system prompts, sampling parameters, and context management.
3. **Benchmarks (`training/evaluation/`):** Add real-world evaluation scenarios and benchmark scripts.
4. **Fine-Tuning & Scripts (`training/fine-tuning/`):** Enhance LoRA recipes, tokenizers, quantization pipelines, and evaluation automation.
5. **Documentation (`documentation/`, `README.md`):** Improve setup instructions, tutorials, and IDE integration guides.

---

## 🚦 Quick Contribution Workflow

1. **Fork & Branch:**
   ```bash
   git checkout -b feature/my-enhancement
   ```

2. **Validate Your Changes:**
   - If adding datasets: run `python3 training/scripts/validate_datasets.py`
   - If modifying benchmarks: run `python3 training/evaluation/benchmark_runner.py --model sopu-coder-fast:v1-candidate`

3. **Commit with Conventional Commits:**
   - `feat:` new features or models
   - `data:` dataset updates
   - `eval:` benchmark changes
   - `fix:` bug fixes
   - `docs:` documentation improvements

4. **Submit a Pull Request:** Open a PR referencing any relevant issue.

---

## 📖 Related Documents
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Project Governance](documentation/governance.md)
- [Model Roadmap](documentation/model-roadmap.md)
- [Dataset Guidelines](datasets/README.md)
