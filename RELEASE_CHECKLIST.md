# 📋 SopuCoder Release Checklist

Use this checklist for every new release or version bump of SopuCoder.

---

## 🔍 1. Pre-Release Technical Audit
- [ ] Both Modelfiles build cleanly without syntax warnings (`ollama create <name> -f Modelfile`).
- [ ] Local inference tested on both models with standard coding prompt.
- [ ] No temporary files, credentials, secrets, or `~/.ollama/models/blobs` in Git staging.
- [ ] All datasets validated using `python3 training/scripts/validate_datasets.py`.
- [ ] Benchmark suite executed and results documented in `training/evaluation/BENCHMARK_REPORT.md`.

## 📜 2. Licensing & Governance Check
- [ ] License notices preserved (Apache 2.0).
- [ ] Upstream foundation model licenses verified and attributed.
- [ ] All dataset samples confirmed under permissive licenses (Apache 2.0, MIT, BSD, ISC).
- [ ] `CODE_OF_CONDUCT.md` and `CONTRIBUTING.md` up to date.

## 🏷️ 3. Versioning & Documentation
- [ ] Version numbers synchronized across:
  - `documentation/model-roadmap.md`
  - `CHANGELOG.md`
  - `RELEASE_NOTES.md`
  - Model tags (`vX.Y.Z`)
- [ ] Modelfiles updated with correct base model references.

## 🚀 4. Distribution Gates
- [ ] **GitHub:** Commit, tag (`git tag -a vX.Y.Z`), push (`git push origin main --tags`), and draft GitHub Release.
- [ ] **Ollama Registry:** Model tagged with namespace (`ollama cp ... <namespace>/<model>:<tag>`) and pushed (`ollama push ...`).
- [ ] **Hugging Face Hub:** Model card metadata updated and verified on web interface.

## 🧪 5. Post-Release Verification
- [ ] Pull and execute model from clean environment (`ollama run <namespace>/<model>:<tag>`).
- [ ] Verify GitHub release assets and links.
- [ ] Verify Hugging Face model cards render properly.

