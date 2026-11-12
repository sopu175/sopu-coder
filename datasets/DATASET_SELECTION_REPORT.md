# 📑 SopuCoder Dataset Selection & Ingestion Report (Phase 3)

**Author:** SopuCoder Dataset Engineering Team  
**Maintainer:** Md. Saiful Islam (Saif)  
**Target Milestone:** Dataset v1.2.0 Expansion  
**Date:** 2026-11-12  

---

## 1. Selection Criteria & Quality Gates

To prepare SopuCoder for the next continuous training cycle while adhering to strict safety and open-source standards, candidate dataset subsets are evaluated against 6 gates:

1. **Permissive Licensing:** Must be `Apache-2.0`, `MIT`, or `BSD`. No non-commercial clauses (`CC-BY-NC`).
2. **Benchmark Decontamination:** No overlap with HumanEval, MBPP, or `benchmarks/baseline_suite.json`.
3. **Execution & Syntax Validation:** All code samples must pass language parsers (TypeScript compiler, Python AST, PHP linter).
4. **Secret Scanning:** Automatic regex scan for API tokens, passwords, private keys, and sensitive URLs.
5. **Quality Over Quantity:** Preference for 200-500 high-signal, production-grade architectural patterns over 50,000 low-quality trivial snippets.
6. **Domain Balancing:** Equal distribution across interactive frontend (Three.js/GSAP), modern full-stack (Next.js/React/Laravel/Yii2), and backend engineering (Python/Node.js/SQL RLS).

---

## 2. Ingestion Plan for Version v1.2.0

```
┌────────────────────────────────────────────────────────┐
│ Current Validated Dataset: v1.1.0 (36 curated records) │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ Target Dataset: v1.2.0 (150-250 curated records)       │
├────────────────────────────────────────────────────────┤
│ • +30 Three.js / R3F / Drei / GLSL Shaders             │
│ • +25 GSAP ScrollTrigger / Lenis Smooth Scroll         │
│ • +35 Next.js 15 Server Actions / Dynamic Metadata     │
│ • +30 Laravel 11 / PHP 8.3 Enums / Queues              │
│ • +30 PostgreSQL Row-Level Security / Zero-Downtime    │
│ • +25 Structured Tool Calling (Open-Meteo & Web Fetch) │
└────────────────────────────────────────────────────────┘
```

---

## 3. Data Governance & Attribution
- All included snippets carry an explicit metadata block:
  ```json
  "metadata": {
    "source": "curated_sopu",
    "license": "apache-2.0",
    "attribution": "SopuCoder Contributors (Md. Saiful Islam)",
    "quality_score": 0.99
  }
  ```
- Versioned independently under `datasets/v1.2/` to preserve reproducible historical training splits.
