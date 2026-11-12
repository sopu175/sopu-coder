# 🌐 SopuCoder Online Dataset Source Registry (Phase 3)

**Registry Maintainer:** Md. Saiful Islam (Saif)  
**Version:** 1.0.0  
**License Verification Standard:** Permissive only (`Apache-2.0`, `MIT`, `BSD-3-Clause`, `CC-BY-4.0`). All restricted, non-commercial (`CC-BY-NC`), or unverified sources are strictly REJECTED.

---

## 📋 Verified & Approved Dataset Sources

### 1. BigCode Project: The Stack v2 (Permissive Subset)
- **Source URL:** `https://huggingface.co/datasets/bigcode/the-stack-v2`
- **Publisher:** BigCode Consortium (Hugging Face & ServiceNow)
- **License:** Permissive open-source licenses verified at repository root (MIT, Apache-2.0, BSD).
- **Target Coverage:** Python, TypeScript, JavaScript, PHP, Shell, SQL.
- **Provenance:** Curated GitHub public repositories with explicit opt-out filtering.
- **Redistribution Rights:** ✅ Permitted with license preservation.
- **Expected Benefit:** High-volume repository-level clean code snippets.

### 2. Glaive Code Assistant & Function Calling v2
- **Source URL:** `https://huggingface.co/datasets/glaiveai/glaive-code-assistant-v2`
- **Publisher:** Glaive AI
- **License:** Apache 2.0
- **Target Coverage:** Structured tool calling, function calling, API integration, debugging.
- **Provenance:** Synthetically generated and validated instruction pairs.
- **Redistribution Rights:** ✅ Permitted (Apache 2.0).
- **Expected Benefit:** Eliminates hallucinated tool calls and improves schema adherence.

### 3. StarCoder2 Self-Oss-Instruct
- **Source URL:** `https://huggingface.co/datasets/bigcode/self-oss-instruct-sc2-exec-filter-50k`
- **Publisher:** BigCode
- **License:** Apache 2.0
- **Target Coverage:** Algorithmic coding, unit tests, execution-verified Python/TypeScript.
- **Provenance:** Generated from real-world open-source seed functions and sandbox-executed.
- **Redistribution Rights:** ✅ Permitted (Apache 2.0).
- **Expected Benefit:** High test pass rate; zero compilation syntax errors.

### 4. SopuCoder Interactive 3D & Creative Web Corpora (Internal Curated)
- **Source URL:** `https://github.com/sopu175/sopu-coder/tree/main/datasets/`
- **Publisher:** SopuCoder Contributors (Md. Saiful Islam)
- **License:** Apache 2.0
- **Target Coverage:** Three.js, React Three Fiber, Drei, WebGL Shaders, GSAP ScrollTrigger, Lenis.
- **Provenance:** Handcrafted and AST-validated production patterns from official documentation and threejs.org examples.
- **Redistribution Rights:** ✅ Permitted (Apache 2.0).
- **Expected Benefit:** Directly addresses identified weakness in 3D creative web development.

### 5. SopuCoder Full-Stack SaaS & Framework Corpora (Internal Curated)
- **Source URL:** `https://github.com/sopu175/sopu-coder/tree/main/datasets/`
- **Publisher:** SopuCoder Contributors
- **License:** Apache 2.0
- **Target Coverage:** Next.js 15 App Router, React 19, Laravel 11, Yii2, WordPress, PostgreSQL RLS.
- **Provenance:** Production engineering patterns with strict type annotations.
- **Redistribution Rights:** ✅ Permitted (Apache 2.0).
- **Expected Benefit:** High-signal real-world full-stack development mastery.

---

## 🚫 Rejected / Disallowed Dataset Sources

| Dataset Name | Candidate Source | Rejection Reason | Action Taken |
| :--- | :--- | :--- | :--- |
| **ShareGPT (Raw / Filtered)** | Various HF Mirrors | Unverified provenance; contaminated with non-permissive terms of service. | ❌ Strictly Rejected |
| **CodeAlpaca (Original)** | Stanford Alpaca derivatives | Generated via non-commercial OpenAI Terms of Service clauses. | ❌ Strictly Rejected |
| **Web-Scraped Unattributed Code** | Raw Web Crawls | Missing repository-level license headers; copyright risk. | ❌ Strictly Rejected |
| **HumanEval / MBPP Benchmarks** | Benchmark Repositories | Direct contamination risk for evaluation suites. | ❌ Quarantined (Evaluation Only) |
