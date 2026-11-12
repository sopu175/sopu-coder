# 📚 SopuCoder Dataset Changelog

All changes, extensions, splits, and schema validations of the SopuCoder training corpora are recorded here.

---

## [v1.1.0] - 2026-11-12

### Added
- **Next.js 14/15 App Router:** Added HMAC webhook signature verification and Zod-validated Server Action samples (`datasets/nextjs/data_v1_1.jsonl`).
- **Node.js Streams & Security:** Added Transform stream chunk parsing with backpressure and secure HTTP server utility (`datasets/nodejs/data_v1_1.jsonl`).
- **Yii2 Framework:** Added Active Record with `TimestampBehavior` / `SluggableBehavior` and authenticated RESTful controller (`datasets/yii2/data_v1_1.jsonl`).
- **WordPress Architecture:** Added secure custom REST API endpoints with nonces and Gutenberg-enabled Custom Post Types (`datasets/wordpress/data_v1_1.jsonl`).
- **Python SQLAlchemy 2.0 & Pytest:** Added generic async repository pattern and `pytest-asyncio` mock test suites (`datasets/python/data_v1_1.jsonl`).
- **TypeScript Advanced Types:** Added nominal Branded Types (`UserId`, `EmailAddress`) and concurrent async file processing (`datasets/typescript/data_v1_1.jsonl`).
- **React 18/19 & Vitest:** Added `useOptimisticMutation` custom hook and Vitest hook unit test suites (`datasets/react/data_v1_1.jsonl`).
- **JavaScript Asynchronous Bus:** Added async Pub/Sub event bus and closure-based polling memory leak analysis (`datasets/javascript/data_v1_1.jsonl`).
- **PHP 8.3 & Laravel 11:** Added Backed Enums with transition guards and Laravel queued jobs with exponential backoff (`datasets/php/data_v1_1.jsonl`).

### Dataset Statistics (v1.1.0)
- **Total Valid Records:** 27
- **Train Split (`datasets/v1.1/train.jsonl`):** 19 samples (70%)
- **Validation Split (`datasets/v1.1/val.jsonl`):** 4 samples (15%)
- **Held-Out Test Split (`datasets/v1.1/test.jsonl`):** 4 samples (15%)
- **Licensing Compliance:** 100% verified `Apache-2.0` / permissive.
- **Evaluation Isolation:** Completely distinct from `training/evaluation/benchmarks.json`.

---

## [v1.0.0] - 2026-11-12

### Initial Seed Corpus
- 9 initial seed examples across Python, TypeScript, React, JavaScript, and Core PHP.
- Staged in `datasets/splits/`.
