# 📊 SopuCoder 18-Domain Baseline Benchmark (Phase 2)

**Evaluation Date:** 2026-11-12  
**Maintainer:** Md. Saiful Islam (Saif)  
**Suite:** SopuCoder Comprehensive 18-Domain Baseline Suite (`benchmarks/baseline_suite.json`)  
**Hardware Baseline:** Apple Silicon M1 (16GB RAM, macOS)  
**Evaluated Models:**
- `sopu-coder:v1-candidate` (`qwen2.5-coder:7b`)
- `sopu-coder-fast:v1-candidate` (`qwen3.5:4b`)
- `sopu-coder-fast-fused` (`Qwen2.5-Coder-1.5B` fine-tuned standalone)

---

## 1. Executive Summary & Comparative Matrix

| Domain Category | Benchmark ID | Focus / Task | SopuCoder 7B (Flagship) | SopuCoder Fast (4B) | Fine-Tuned Candidate (1.5B) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. JS & TypeScript** | `dom_01_ts_js` | Type-Safe Generic Event Bus | **16.75 t/s** (Exceptional) | 22.1 t/s (Verbose) | **68.7 t/s** (Instant) |
| **2. React** | `dom_02_react` | Compound Modal with ARIA & Context | **17.67 t/s** (Strict ARIA) | 21.8 t/s (Solid) | **64.2 t/s** (Clean) |
| **3. Next.js App Router**| `dom_03_nextjs` | Server Actions + Zod Validation | **16.34 t/s** (Production) | 22.4 t/s (Good) | **60.5 t/s** (Fast) |
| **4. Node.js Streams** | `dom_04_nodejs` | NDJSON Pipeline with Backpressure | **17.1 t/s** (Stream API) | 23.0 t/s | 65.0 t/s |
| **5. PHP & Laravel 11** | `dom_05_php_laravel`| Idempotent Job with Enum & Backoff | **16.9 t/s** (PSR-12) | 22.5 t/s | 61.2 t/s |
| **6. Yii2 & WordPress** | `dom_06_yii2_wp` | REST Controller with Nonce & `$wpdb` | **17.2 t/s** (Secure) | 21.9 t/s | 59.8 t/s |
| **7. Python Backend** | `dom_07_python` | SQLAlchemy 2.0 Async Generic Repo | **17.0 t/s** (Type-hinted) | 22.8 t/s | 62.4 t/s |
| **8. Three.js** | `dom_08_threejs` | Procedural ShaderMaterial Swarm | **16.8 t/s** (GLSL Valid) | 20.5 t/s | 58.1 t/s |
| **9. React Three Fiber**| `dom_09_r3f` | Animated Icosahedron with Drei | **17.1 t/s** (R3F Clean) | 21.2 t/s | 60.1 t/s |
| **10. GSAP Motion** | `dom_10_gsap` | ScrollTrigger Horizontal Pinning | **16.9 t/s** (`useGSAP` safe) | 22.0 t/s | 59.5 t/s |
| **11. SaaS Architecture**| `dom_11_saas` | PostgreSQL Row-Level Security (RLS) | **17.4 t/s** (Clean DDL) | 23.1 t/s | 63.0 t/s |
| **12. Migrations** | `dom_12_migrations`| Zero-Downtime Column Rename | **17.5 t/s** (Expand-Contract)| 22.7 t/s | 61.8 t/s |
| **13. Technical SEO** | `dom_13_seo` | Next.js Dynamic JSON-LD & OG | **16.8 t/s** (Google Schema) | 21.9 t/s | 64.0 t/s |
| **14. Testing** | `dom_14_testing` | Vitest + RTL Fake Timers Hook Test | **17.2 t/s** (Deterministic) | 22.3 t/s | 66.5 t/s |
| **15. Debugging** | `dom_15_debugging`| Thread-Safe Cache Race Condition | **17.0 t/s** (Double-check) | 21.5 t/s | 67.0 t/s |
| **16. Refactoring** | `dom_16_refactor` | Procedural to PHP 8.3 Enum Strategy| **16.8 t/s** (Modern OOP) | 22.6 t/s | 63.5 t/s |
| **17. Multi-File Sync** | `dom_17_multifile`| FastAPI Schema + TypeScript Parity | **17.1 t/s** (100% Matching) | 22.4 t/s | 61.0 t/s |
| **18. Tool Calling** | `dom_18_tools` | Structured Tool Call (Open-Meteo) | **17.3 t/s** (Valid JSON) | 23.0 t/s | **Keyless Tool Engine** |

---

## 2. Key Findings & Weakness Identification

### Strengths
1. **Full-Stack Typing Parity:** SopuCoder 7B achieves 100% field naming alignment between backend (FastAPI / Pydantic) and frontend (TypeScript) interfaces.
2. **Modern Framework Idioms:** Adheres to Next.js 14/15 Server Actions, React 19 hooks, and PHP 8.3 Backed Enums without defaulting to legacy patterns.
3. **Keyless Tool Execution:** Seamlessly invokes registered tools (`get_current_weather` via Open-Meteo) and passes results back for natural-language synthesis.

### Highest-Impact Weaknesses & Gaps
1. **Interactive 3D / WebGL Density:** While basic Three.js geometry setups are generated cleanly, complex GLSL raymarching and custom post-processing shaders require larger prompt context and additional curated dataset examples.
2. **GSAP Cleanup in React 19:** Models must strictly use `@gsap/react` `useGSAP` or `ctx.revert()` inside `useEffect` to prevent memory leaks during hot-module reloading.
3. **Qwen3.5 Thinking Latency:** In `sopu-coder-fast` (4B), chain-of-thought tokens cause an initial latency delay of ~15-20 seconds before emitting simple inline code. Fine-tuned 1.5B standalone weights completely bypass this delay (~0.5s response).

