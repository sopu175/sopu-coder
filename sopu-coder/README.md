# 🧠 SopuCoder (Standard Model)

The flagship model of the SopuCoder suite, tailored for software engineers needing deep reasoning, complex architectural design, and full-stack development capability.

## Specifications
- **Base Model:** `qwen2.5-coder:7b` (Custom fine-tuned weights available)
- **Context Length:** 32,768 tokens
- **Target Hardware:** 16GB RAM / 8GB VRAM / Apple Silicon (M-series)
- **Key Stacks:** Python, TypeScript, React, JavaScript, Modern PHP 8.x

## Build & Run Locally with Ollama

```bash
# Build the model using the local Modelfile
ollama create sopu-coder -f Modelfile

# Run interactive session
ollama run sopu-coder
```

## Recommended VS Code / Cursor Settings (via Continue)

```json
{
  "models": [
    {
      "title": "SopuCoder",
      "provider": "ollama",
      "model": "sopu-coder"
    }
  ]
}
```

