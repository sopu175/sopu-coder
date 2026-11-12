# 🗺️ SopuCoder 18-Domain Capability Matrix (Phase 2)

**Maintainer:** Md. Saiful Islam (Saif)  
**Version:** 1.0.0  
**Last Updated:** 2026-11-12  

---

## 🎯 Capability Maturity Levels

- **Level 5 (Production-Ready):** Flawless syntax, strict type checking, robust error handling, security defensive checks, idiomatic modern standards.
- **Level 4 (Advanced):** Fully functional, adheres to modern framework idioms, minor manual refinement for edge cases.
- **Level 3 (Competent):** Syntactically correct, handles standard scenarios, may require prompt specificity for advanced architecture.
- **Level 2 (Developing):** Functional logic, but requires curated dataset expansion to avoid legacy conventions.
- **Level 1 (Experimental):** Emerging capability, needs targeted fine-tuning data.

---

## 📊 Comprehensive Matrix

| # | Domain / Technology | Maturity Level | Primary Strengths | Identified Weakness / Action Item |
| :- | :--- | :---: | :--- | :--- |
| **1** | **JavaScript & TypeScript** | **Level 5** | Nominal branded types, strict generics, async iterators, type-safe builders. | None. Production-ready. |
| **2** | **React** | **Level 5** | Compound components, Context, clean state isolation, memoization. | Prevent over-memoization with `useCallback` on trivial functions. |
| **3** | **Next.js App Router** | **Level 5** | Server Actions, Zod parsing, streaming metadata, parallel routes. | Ensure strict cookie-based auth handling in middleware. |
| **4** | **Node.js** | **Level 5** | Transform streams, backpressure management, AES-256-GCM crypto. | Memory profiling under extreme event emitter loops. |
| **5** | **PHP & Laravel 11** | **Level 5** | PSR-12, Backed Enums, Queued jobs with exponential backoff, DTOs. | Keep Laravel 10 vs 11 directory conventions distinct. |
| **6** | **Yii2 & WordPress** | **Level 4** | Active Record behaviors, WordPress REST nonces, `$wpdb->prepare`. | Expand Gutenberg custom block block.json dataset samples. |
| **7** | **Python Backend** | **Level 5** | FastAPI async endpoints, SQLAlchemy 2.0 AsyncSession, Pydantic v2. | Enforce strict pytest-asyncio event loop scope in tests. |
| **8** | **Three.js** | **Level 4** | BufferGeometry, custom ShaderMaterial, animation loop lifecycle. | Add advanced GLSL noise and post-processing passes. |
| **9** | **React Three Fiber (R3F)** | **Level 4** | Drei hooks, OrbitControls, useFrame animation, Suspense. | Expand physics integrations (`@react-three/rapier`). |
| **10** | **GSAP & ScrollTrigger** | **Level 4** | Horizontal pinning, timelines, `@gsap/react` `useGSAP` cleanup. | Ensure hot-reload cleanup via `ctx.revert()`. |
| **11** | **SaaS Architecture** | **Level 5** | Multi-tenant tenant-isolation, PostgreSQL Row-Level Security (RLS). | Add Stripe webhook HMAC signature verification patterns. |
| **12** | **Database Migrations** | **Level 5** | Zero-downtime expand-and-contract, online index creation. | Emphasize foreign key locking considerations in high-load tables. |
| **13** | **Technical SEO** | **Level 5** | Dynamic JSON-LD (Schema.org), OpenGraph/Twitter cards, sitemap. | Validate nested BreadcrumbList JSON-LD schemas. |
| **14** | **Testing** | **Level 5** | Vitest, Jest, React Testing Library, fake timers, async acts. | Ensure mocking isolation between parallel test files. |
| **15** | **Debugging** | **Level 5** | Race condition detection, deadlock resolution, memory leak fixes. | Provide memory heap snapshot diagnostics tips. |
| **16** | **Refactoring** | **Level 5** | Procedural to clean OOP, match expressions, SRP, design patterns. | Maintain backwards compatibility during major signature refactoring. |
| **17** | **Multi-File Sync** | **Level 5** | Parity between backend schemas (Pydantic) and frontend types (TS). | Automated contract generation via OpenAPI. |
| **18** | **Tool Calling** | **Level 5** | Native Ollama tool execution, Open-Meteo keyless weather, web fetch. | Add Figma MCP and Playwright browser execution tools. |

---

## 🚀 Priority Targets for Next Continuous Fine-Tuning Cycle
1. **Interactive 3D / Creative Frontend:** Ingest 50+ curated Three.js, R3F, and GSAP examples into `datasets/v1.2/`.
2. **SaaS Billing & Security:** Ingest Stripe Webhook idempotency, RBAC JWT token refresh, and multi-tenant isolation samples.
3. **Figma MCP Integration:** Ingest design-token-to-Tailwind and Figma component translation patterns.

