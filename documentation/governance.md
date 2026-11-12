# 🏛️ SopuCoder Community Governance & RFC Process

This document defines how decisions are made, how contributors participate, and the standards governing the SopuCoder open-source ecosystem.

---

## 🎯 Guiding Principles

1. **Local-First & Developer Privacy:** We prioritize models that can run independently on local developer machines without leaking data.
2. **Transparent Benchmarking:** We evaluate models against objective, reproducible benchmarks covering code generation, debugging, and latency.
3. **Open Weight Provenance:** All training datasets and fine-tuning recipes must be strictly permissively licensed and reproducible.

---

## 📜 Request for Comments (RFC) Process

Major architectural changes, new model additions, or large dataset shifts follow an RFC process:

1. **Proposal:** Open a GitHub Issue labeled `proposal` using the Feature Request template.
2. **Community Feedback:** Maintainers and contributors discuss trade-offs, compute constraints, and license implications.
3. **Prototype & Benchmark:** The author or maintainer provides benchmark evaluation numbers.
4. **Resolution:** Maintainers accept, modify, or decline the proposal based on community consensus and project goals.

---

## 👥 Roles & Decision Rights

- **Maintainers:** Hold merge permissions, manage GitHub release tags, verify licenses, and oversee model uploads to Ollama Registry and Hugging Face.
- **Reviewers & Contributors:** Review pull requests, contribute benchmark scripts, suggest prompt improvements, and curate datasets.
- **Community:** File bug reports, propose language improvements, and participate in GitHub Discussions.
