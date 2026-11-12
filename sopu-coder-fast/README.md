# ⚡ SopuCoder Fast (Lightweight Model)

An ultra-low-latency coding model optimized for inline tab completions, fast function writing, bug fixing, and execution on resource-constrained hardware.

## Specifications
- **Base Model:** `qwen3.5:4b`
- **Context Length:** 16,384 tokens
- **Target Hardware:** 8GB RAM / Entry-level Laptops / Edge Devices
- **Key Specialization:** Instant inline completions, boilerplate generation, syntax error fixes

## Build & Run Locally with Ollama

```bash
# Build the model using the local Modelfile
ollama create sopu-coder-fast -f Modelfile

# Run interactive session
ollama run sopu-coder-fast
```

## Recommended VS Code / Cursor Settings (for Tab Autocomplete)

```json
{
  "tabAutocompleteModel": {
    "title": "SopuCoder Fast",
    "provider": "ollama",
    "model": "sopu-coder-fast"
  }
}
```

