# 🔍 SopuCoder Dataset Audit (Phase 1 Deliverable)

**Date of Audit:** 2026-11-12  
**Auditor:** Senior Machine Learning Engineer (Coding LLM Specialist)  
**Target Release:** v1.1.0 Dataset Improvement & Fine-Tuning  
**Scope:** `datasets/` repository, validation pipeline, and training coverage  

---

## 📊 1. Current Dataset Inventory & Language Distribution

| Directory | Valid Records | Blank/Corrupt Lines | Key Frameworks Present | Gaps Identified |
| :--- | :--- | :--- | :--- | :--- |
| **`datasets/python/`** | 2 | 1 (Trailing blank) | FastAPI, Asyncio Queue | Missing pytest, Pydantic v2, security sanitization, algorithms |
| **`datasets/typescript/`** | 2 | 1 (Trailing blank) | Generics (Result), Express | Missing interfaces, strict typing utilities, tsconfig patterns |
| **`datasets/javascript/`** | 1 | 1 (Trailing blank) | Vanilla ESNext (DeepClone) | Missing async iterators, event emitters, Node.js streams |
| **`datasets/react/`** | 2 | 1 (Trailing blank) | Custom Hook, Modal Portal | Missing Next.js App router, Server Components, Zustand/Redux |
| **`datasets/php/`** | 2 | 1 (Trailing blank) | Core PHP 8.2, Laravel Request | Missing Yii2, WordPress plugins/hooks, PHPUnit tests, Doctrine/Eloquent |
| **`datasets/splits/`** | 9 total | - | Train: 7, Val: 0, Test: 2 | Zero validation samples (`val.jsonl` is empty) |
| **TOTAL** | **9 records** | **5 blank lines** | Extremely minimal seed set | Severe under-representation across modern engineering stacks |

---

## 🚨 2. Critical Findings & Flaws

1. **Volume & Coverage Inadequacy:**
   - 9 seed examples are strictly illustrative; attempting fine-tuning with 9 samples will cause catastrophic overfitting or zero behavioral adaptation.
   - Missing major requested stacks: **Next.js (App Router), Node.js (Streams/Buffers), Yii2, WordPress (Hooks/Security), and Unit Testing (pytest, PHPUnit, Vitest)**.
2. **Empty Validation Split:**
   - `datasets/splits/val.jsonl` contains 0 records. Without a validation split, monitoring evaluation loss during training is impossible.
3. **Data Leakage Risk:**
   - The test set (`datasets/splits/test.jsonl`) contains `py_001` and `py_002`. While separated from `train.jsonl`, evaluation benchmark scenarios in `training/evaluation/benchmarks.json` must remain completely distinct from training corpora to avoid contamination.
4. **Blank Line Ingestion Bug:**
   - Datasets contain trailing blank lines that cause naive `json.loads()` parsers to throw exceptions unless stripped.
5. **Absence of 10 Core Software Engineering Dimensions:**
   - Existing records only cover basic snippet generation.
   - Missing: Refactoring pairs, Bug-fixing/Debugging pairs, Security audits (SQLi/XSS prevention), Multi-file contracts, and Unit testing suites.

---

## 🎯 3. Roadmap for Phase 2 Dataset Expansion

To prepare SopuCoder for genuine fine-tuning, the dataset must expand to high-quality, production-oriented samples across 10 targeted domains:

1. **JavaScript & Node.js:** Event-driven architectures, stream pipelines, buffer management, ESM modules.
2. **TypeScript:** Complex mapped types, conditional types, decorators, strict API contracts.
3. **React & Next.js:** Next.js 14/15 App Router (`route.ts`, Server Actions), React 18/19 custom hooks, state management, Vitest tests.
4. **PHP & Modern Frameworks:**
   - **Modern Core PHP 8.2/8.3:** Enums, Attributes, Readonly classes, Fibers.
   - **Laravel 11:** Service providers, queued jobs, custom middleware, policy authorization.
   - **Yii2:** Active Record, behaviors, custom action filters, data providers.
   - **WordPress:** Secure REST API endpoints, nonces/sanitization, custom post types, hook priority.
5. **Python:** Clean architecture, FastAPI dependency injection, async database repositories (SQLAlchemy 2.0), pytest fixtures, type narrowing.
6. **Software Engineering Tasks:**
   - Bug-to-fix pairs with rationale.
   - Legacy-to-clean refactoring pairs.
   - Multi-file interface consistency pairs.

---

## 🛡️ 4. Licensing & Attribution Standards
- Every added sample must explicitly specify:
  - `"license": "apache-2.0"` or `"mit"`
  - `"attribution": "SopuCoder Contributors"`
  - `"quality_score": >= 0.95`
  - Sanitized code (zero credentials, no private tokens, no hallucinated APIs).

