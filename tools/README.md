# 🛠️ SopuCoder Native Tool-Calling & Agent Engine

The `tools/` package provides native tool-calling, API dispatching, and agent execution capabilities for SopuCoder, resolving raw JSON leaks and preventing fake API key hallucinations.

---

## 🏗️ Architecture

```mermaid
flowchart LR
    User["User Query"] --> Agent["SopuCoderAgent (agent_runtime.py)"]
    Agent --> Ollama["Ollama /api/chat with tools schema"]
    Ollama --> ToolCall["Emits Tool Call (Function Name & Arguments)"]
    ToolCall --> Registry["ToolRegistry (registry.py)"]
    Registry --> ToolExec["Executes Tool (Open-Meteo, Web Fetch, etc.)"]
    ToolExec --> Synthesis["Feeds Output Back to SopuCoder"]
    Synthesis --> Response["Natural Language Final Response"]
```

---

## 📦 Built-in Tools

1. **`get_current_weather(location)`**:
   - Queries **Open-Meteo API** (`api.open-meteo.com`).
   - Geocoding and weather lookup with **zero API keys required**.
   - Worldwide coverage (temperature, apparent temperature, humidity, wind speed, weather code).
2. **`web_fetch(url, max_length=4000)`**:
   - Safe HTTP/HTTPS web fetcher for public documentation and APIs.
   - Strictly blocks SSRF and local loopback addresses (`127.0.0.1`, `localhost`).
   - Enforces timeout and content size bounds.

---

## 🚀 CLI Usage

```bash
# Run a single query with tool execution
python -m tools.cli "What is the weather today in Dhaka?"

# Verbose mode: inspect tool arguments and raw output
python -m tools.cli -v "What is the weather today in Tokyo?"

# Interactive chat session with continuous tool execution
python -m tools.cli --interactive
```

---

## 🧪 Integration Tests

Run the full integration test suite:

```bash
python3 -m unittest tests/test_tool_calling.py
```

