# 📚 SopuCoder Dataset Changelog

All changes, extensions, splits, and schema validations of the SopuCoder training corpora are recorded here.

---

## [v1.1.0] - 2026-11-12

### Added
- **Next.js 14/15 App Router:** Added HMAC webhook signature verification, Zod-validated Server Action samples, and dynamic metadata streaming (`datasets/nextjs/data_v1_1.jsonl`).
- **Node.js Streams & Security:** Added Transform stream chunk parsing with backpressure, secure HTTP server utility, and AES-256-GCM authenticated payload encryption (`datasets/nodejs/data_v1_1.jsonl`).
- **Yii2 Framework:** Added Active Record with `TimestampBehavior` / `SluggableBehavior`, authenticated RESTful controller, and multi-model transactional checkout service (`datasets/yii2/data_v1_1.jsonl`).
- **WordPress Architecture:** Added secure custom REST API endpoints with nonces, Gutenberg-enabled Custom Post Types, and `$wpdb->prepare` analytics repository (`datasets/wordpress/data_v1_1.jsonl`).
- **Python SQLAlchemy 2.0 & Pytest:** Added generic async repository pattern, `pytest-asyncio` mock test suites, and token bucket rate limiter (`datasets/python/data_v1_1.jsonl`).
- **TypeScript Advanced Types:** Added nominal Branded Types (`UserId`, `EmailAddress`), concurrent async file processing, and type-safe Query Builder (`datasets/typescript/data_v1_1.jsonl`).
- **React 18/19 & Vitest:** Added `useOptimisticMutation` custom hook, Vitest hook unit test suites, and compound Accordion pattern (`datasets/react/data_v1_1.jsonl`).
- **JavaScript Asynchronous Bus:** Added async Pub/Sub event bus, closure-based polling memory leak analysis, and O(1) LRU Cache (`datasets/javascript/data_v1_1.jsonl`).
- **PHP 8.3 & Laravel 11:** Added Backed Enums with transition guards, Laravel queued jobs with exponential backoff, and PSR-15 Middleware Pipeline (`datasets/php/data_v1_1.jsonl`).

### Dataset Statistics (v1.1.0)
- **Total Valid Records:** 36 records (across 10 targeted software development technologies)
- **Train Split (`datasets/v1.1/train.jsonl`):** 26 samples (72.2%)
- **Validation Split (`datasets/v1.1/val.jsonl`):** 5 samples (13.9%)
- **Held-Out Test Split (`datasets/v1.1/test.jsonl`):** 5 samples (13.9%)
- **Licensing Compliance:** 100% verified `Apache-2.0` / permissive.
- **Evaluation Isolation:** Completely distinct from `training/evaluation/benchmarks.json`.
- **Formatting:** Dual export in standard JSONL instruction format and MLX Chat template text format (`datasets/v1.1/mlx_data/`).

---

## [v1.0.0] - 2026-11-12

### Initial Seed Corpus
- 9 initial seed examples across Python, TypeScript, React, JavaScript, and Core PHP.
- Staged in `datasets/splits/`.
