# 🏆 SopuCoder Candidate Models Comparative Benchmark Report

**Evaluation Date:** 2026-11-12  
**Suite Version:** 1.0.0  
**Environment:** Local Apple Silicon / Ollama  
**Categories Evaluated:** Code generation, Debugging, Refactoring, Multi-file consistency, Tool calling, Latency

---

## 📊 Summary Performance Comparison

| Metric | `sopu-coder:v1-candidate` (Flagship 7B) | `sopu-coder-fast:v1-candidate` (Fast 1.5B/3B) |
| :--- | :--- | :--- |
| **Model Footprint** | ~4.7 GB (Q4_K_M) | ~3.3 GB (Q4_K_M) |
| **Context Window** | 8,192 / 32,768 tokens | 8,192 / 16,384 tokens |
| **Average Generation Speed** | **17.03 tokens/sec** | **22.38 tokens/sec** (+31.4% faster) |
| **Total Test Execution Time** | **194.26 seconds** | **416.19 seconds** |
| **Total Generated Tokens** | 3,175 tokens | 8,825 tokens |
| **Conciseness & Code Focus** | Exceptional (stopped exactly at solution) | Highly verbose / detailed reasoning |

---

## 📋 Category Breakdown

### 1. Code Generation (React & TypeScript)
- **Prompt:** Complete `useDebouncedAsync` hook with AbortController and full TypeScript generics.
- **`sopu-coder:v1-candidate`:** Produced a clean 657-token complete implementation with perfect type definitions (`<T, Args extends any[]>`), correct cleanup on unmount, and zero boilerplate fluff.
- **`sopu-coder-fast:v1-candidate`:** Fully functional implementation, highly descriptive, generated 2,048 tokens.

### 2. Debugging (Python Concurrency)
- **Prompt:** Identify race condition in `TTLCache` (unsynchronized read/delete) and provide thread-safe fix.
- **`sopu-coder:v1-candidate`:** Pinpointed exact concurrency flaw in 386 tokens, providing clean synchronized `with self.lock:` blocks around read and write operations.
- **`sopu-coder-fast:v1-candidate`:** Accurately solved the race condition with comprehensive explanation and unit test examples.

### 3. Refactoring (PHP 8.2+ Modernization)
- **Prompt:** Legacy imperative function into modern PSR-12 class with `declare(strict_types=1)`, `match` expressions, and DTO.
- **`sopu-coder:v1-candidate`:** Clean `OrderProcessor` service class with readonly `OrderResult` DTO and modern `match ($type)` syntax (680 tokens).
- **`sopu-coder-fast:v1-candidate`:** High quality PSR-12 refactored structure with full comments.

### 4. Multi-File Consistency (Full-Stack Sync)
- **Prompt:** Synchronized FastAPI `PATCH /api/v1/users/me` endpoint and TypeScript fetch client.
- **`sopu-coder:v1-candidate`:** Exact matching field names (`displayName`, `bio`, `marketingOptIn`), correct HTTP PATCH method, and synchronized error interfaces (760 tokens).
- **`sopu-coder-fast:v1-candidate`:** Cleanly aligned frontend DTO and backend schema.

### 5. Tool Calling (Structured Output)
- **Prompt:** Pure JSON tool call for `execute_sql_query` finding top 5 customers in 2026.
- **`sopu-coder:v1-candidate`:** Generated valid, minimal JSON tool call with correct SQL syntax (5.56s, 82 tokens).
- **`sopu-coder-fast:v1-candidate`:** Clean JSON format returned (9.52s, 207 tokens).

### 6. Latency & Throughput (Algorithmic DP)
- **Prompt:** 0/1 Knapsack with space optimization O(W).
- **`sopu-coder:v1-candidate`:** 17.12 tokens/sec, completed in 36.0s.
- **`sopu-coder-fast:v1-candidate`:** 23.16 tokens/sec, completed in 43.0s.

---

## 💡 Recommendation for Release & IDE Configuration
- **SopuCoder (`sopu-coder`):** Best suited as primary chat assistant, refactoring engine, and multi-file architect in VS Code / Cursor (Continue plugin: `model: sopu-coder`).
- **SopuCoder Fast (`sopu-coder-fast`):** Best suited for instant tab-autocomplete and inline completions where raw token velocity is critical (`tabAutocompleteModel: sopu-coder-fast`).

