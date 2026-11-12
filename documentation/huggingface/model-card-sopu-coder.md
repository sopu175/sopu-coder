---
language:
- en
license: apache-2.0
tags:
- code
- coding
- text-generation
- qwen2.5-coder
- ollama
- gguf
- python
- typescript
- javascript
- php
- react
- nextjs
- fastapi
- laravel
- tool-calling
pipeline_tag: text-generation
inference: false
---

# 🧠 SopuCoder (v1.1.0)

**SopuCoder** is an open-source, community-driven AI coding assistant created and maintained by **Md. Saiful Islam (Saif)**, built upon Alibaba Cloud's **Qwen2.5-Coder 7B** foundation model and customized for production-grade full-stack software engineering.

---

## 🚀 Key Specifications

- **Creator & Maintainer:** Md. Saiful Islam (Saif)
- **Base Architecture:** Alibaba Cloud Qwen 2.5 Coder 7B
- **Context Length:** 16,384 tokens
- **Inference Speed:** ~17 tokens/second on Apple Silicon M1
- **Language Support:** Bilingual (English & Bengali / বাংলা)
- **Target Stacks:** TypeScript, React 19, Next.js App Router, Python (FastAPI/SQLAlchemy 2.0), PHP 8.3 (Laravel 11/Yii2), Three.js, GSAP, SaaS Multi-Tenancy (PostgreSQL RLS).
- **Template Architecture:** Dual-Mode Template (Clean conversational natural-language chat in terminal, structured function calls in agent runtimes).
- **Tool Calling Support:** Native Ollama tool execution with Open-Meteo (keyless real-time weather) and safe web fetch.

---

## 📊 18-Domain Baseline Benchmark (v1.1.0)

| Category | Benchmark Test | Score / Speed | Status |
| :--- | :--- | :--- | :--- |
| **JavaScript & TypeScript** | Type-Safe Generic Nominal Event Bus | 16.75 t/s | **Level 5 (Production)** |
| **React** | Compound Modal with ARIA & Context | 17.67 t/s | **Level 5 (Production)** |
| **Next.js App Router** | Server Action with Zod & Revalidation | 16.34 t/s | **Level 5 (Production)** |
| **Node.js** | Backpressure-Managed NDJSON Stream Pipeline | 17.10 t/s | **Level 5 (Production)** |
| **PHP & Laravel 11** | Idempotent Job with Backoff & Enums | 16.90 t/s | **Level 5 (Production)** |
| **Yii2 & WordPress** | REST API Controller with Nonces & `$wpdb` | 17.20 t/s | **Level 4 (Advanced)** |
| **Python Backend** | SQLAlchemy 2.0 Async Generic Repository | 17.00 t/s | **Level 5 (Production)** |
| **Three.js & R3F** | Procedural ShaderMaterial & Drei Animation | 16.80 t/s | **Level 4 (Advanced)** |
| **GSAP Motion** | ScrollTrigger Pinning with `@gsap/react` | 16.90 t/s | **Level 4 (Advanced)** |
| **SaaS & DB Migrations** | Multi-Tenant RLS & Zero-Downtime Migration | 17.40 t/s | **Level 5 (Production)** |
| **Testing & Debugging** | Vitest Hook Suite & Thread-Safe Lock Repair | 17.20 t/s | **Level 5 (Production)** |
| **Tool Calling** | Native Dispatch & Open-Meteo Live Integration | 17.30 t/s | **Level 5 (Production)** |

---

## 🦙 Quick Run with Ollama

```bash
# Run latest release
ollama run sopu175/sopu-coder:v1.1.0

# Or run latest tag
ollama run sopu175/sopu-coder:latest
```

## 🛠️ Native Tool-Calling CLI

```bash
# Clone the repository
git clone https://github.com/sopu175/sopu-coder.git && cd SopuCoder

# Run live query with real-time tool execution (e.g. Open-Meteo)
python -m tools.cli "What is the weather today in Dhaka?"
```

---

## 📄 License & Attribution
- **Creator Attribution:** Created and maintained by Md. Saiful Islam (Saif).
- **Foundation Model:** Built upon Alibaba Cloud's Qwen2.5-Coder 7B (Apache License 2.0).
- **SopuCoder Engine:** Licensed under the Apache License 2.0.
