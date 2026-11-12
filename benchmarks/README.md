# 📊 SopuCoder 18-Domain Baseline Benchmark Suite

This directory contains the reproducible benchmark suite evaluating SopuCoder across 18 core software engineering domains.

---

## 📋 Evaluated Domains (`baseline_suite.json`)

1. **JavaScript & TypeScript:** Type-safe nominal generic EventBus.
2. **React:** Compound Modal pattern with Context, Portals, and ARIA.
3. **Next.js App Router:** Server Actions with Zod validation and revalidation.
4. **Node.js Streams:** Backpressure-managed NDJSON stream pipeline.
5. **PHP & Laravel 11:** Idempotent Queued Job with exponential backoff & PHP 8.3 Enums.
6. **Yii2 & WordPress:** Secure REST API controller with nonces & `$wpdb->prepare`.
7. **Python Backend:** Generic async repository pattern with SQLAlchemy 2.0.
8. **Three.js:** Procedural particle swarm with custom ShaderMaterial.
9. **React Three Fiber (R3F):** Interactive 3D mesh with Drei and useFrame.
10. **GSAP Motion:** ScrollTrigger horizontal pinning and `@gsap/react` cleanup.
11. **SaaS Architecture:** PostgreSQL Row-Level Security (RLS) tenant isolation.
12. **Database Migrations:** Zero-downtime expand-and-contract column rename.
13. **Technical SEO:** Dynamic Next.js JSON-LD and OpenGraph metadata.
14. **Testing:** Vitest custom hook unit test suite with fake timers.
15. **Debugging:** Concurrency lock race condition detection and repair.
16. **Refactoring:** Legacy procedural calculator to modern PSR-12 OOP.
17. **Multi-File Parity:** FastAPI endpoint and TypeScript client field parity.
18. **Tool Calling:** Structured tool invocation using Open-Meteo schema.

---

## 🚀 Running the Benchmarks

```bash
# Run full suite (18 domains) on SopuCoder
python3 benchmarks/run_benchmarks.py --model sopu-coder:v1-candidate

# Run fast 3-test sample check
python3 benchmarks/run_benchmarks.py --sample --model sopu-coder:v1-candidate

# Run on SopuCoder Fast
python3 benchmarks/run_benchmarks.py --model sopu-coder-fast:v1-candidate
```

Results are automatically saved to `benchmarks/results/<model>_benchmark.json`.

