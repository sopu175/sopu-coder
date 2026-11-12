# ⏭️ SopuCoder Next Actions & Queue

**Current Milestone:** Phase 1 (Model Identity) & P0 (Tool Calling / Agent Runtime)

---

## 🎯 Immediate Priority Queue

1. **[P0] Model Identity & Creator Attribution:**
   - Update `sopu-coder/Modelfile` and `sopu-coder-fast/Modelfile` to include creator **Md. Saiful Islam (Saif)** and foundation acknowledgment **Alibaba Cloud / Qwen Team**.
   - Build candidate models in Ollama (`sopu-coder:v1-candidate`, `sopu-coder-fast:v1-candidate`).
   - Run automated identity tests ("Who are you?", "Who built you?", "Are you Qwen?").

2. **[P0] Tool Calling & External API Dispatch Runtime:**
   - Create `tools/agent_runtime.py` implementing the complete Ollama `/api/chat` tool loop.
   - Implement `get_current_weather` using **Open-Meteo API** (zero API keys required, geocoding for Dhaka).
   - Implement safe `web_fetch` with validation and rate limiting.
   - Implement missing tool interceptor (no raw JSON or fake API keys exposed).
   - Run integration tests in `tests/test_tool_calling.py`.
   - Test "What is the weather today in Dhaka?" live end-to-end.

3. **[P1] Coding Capability Baseline (Phase 2):**
   - Run benchmark runner across newly expanded domains (Three.js, GSAP, SaaS).
   - Generate `documentation/BASELINE_BENCHMARKS.md` and `documentation/CAPABILITY_MATRIX.md`.

4. **[P2] Pre-Publish Audit & Publishing (Phase 11 & 14):**
   - Implement `scripts/pre_publish_audit.py`.
   - Run audit, commit changes, and push to GitHub.
