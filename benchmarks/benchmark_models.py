#!/usr/bin/env python3
"""
SopuCoder Benchmark Suite
=========================
Compares base and custom models across accuracy, tool-calling success rate, and latency.
"""

import time
import json
import ollama

client = ollama.Client()

models = [
    "qwen2.5-coder:7b",
    "sopu-coder:latest",
    "sopu-coder-fast:latest"
]

tools = [{
    "type": "function",
    "function": {
        "name": "glob",
        "description": "Find files matching pattern in the workspace",
        "parameters": {
            "type": "object",
            "properties": {"pattern": {"type": "string"}},
            "required": ["pattern"]
        }
    }
}]

test_cases = [
    {
        "name": "Tool Call English ('index the codebase full')",
        "prompt": "index the codebase full",
        "has_tools": True,
        "expected_tool": "glob"
    },
    {
        "name": "Tool Call Bengali ('ei folder er shob file index koro')",
        "prompt": "ei folder er shob file index koro",
        "has_tools": True,
        "expected_tool": "glob"
    },
    {
        "name": "Coding Latency Test ('Write a binary search function in Python')",
        "prompt": "Write a binary search function in Python",
        "has_tools": False,
        "expected_tool": None
    }
]

print("=" * 80)
print(f"{'MODEL':<22} | {'TEST CASE':<35} | {'SUCCESS':<8} | {'LATENCY':<8} | {'OUTPUT / TOOL'}")
print("=" * 80)

results = {}

for model in models:
    results[model] = []
    # Warm up / unload
    client.generate(model=model, keep_alive=0)

    for tc in test_cases:
        t0 = time.time()
        kwargs = {
            "model": model,
            "messages": [{"role": "user", "content": tc["prompt"]}]
        }
        if tc["has_tools"]:
            kwargs["tools"] = tools

        try:
            resp = client.chat(**kwargs)
            elapsed = time.time() - t0
            msg = resp.message

            if tc["has_tools"]:
                # Success if structured tool_calls returned with correct tool name
                if msg.tool_calls and any(c.function.name == tc["expected_tool"] for c in msg.tool_calls):
                    success = "PASS"
                    detail = f"tool_calls[{msg.tool_calls[0].function.name}]"
                elif msg.tool_calls:
                    success = "FAIL (name)"
                    detail = f"tool_calls[{msg.tool_calls[0].function.name}]"
                else:
                    success = "FAIL (leak)"
                    detail = f"raw content: {repr(msg.content[:30])}"
            else:
                # Text coding test
                if "def binary_search" in msg.content or "def " in msg.content:
                    success = "PASS"
                    detail = f"{len(msg.content)} chars"
                else:
                    success = "WARN"
                    detail = repr(msg.content[:30])

            print(f"{model:<22} | {tc['name']:<35} | {success:<8} | {elapsed:>6.2f}s | {detail}")
            results[model].append({"test": tc["name"], "success": success, "latency": elapsed, "detail": detail})

        except Exception as e:
            elapsed = time.time() - t0
            print(f"{model:<22} | {tc['name']:<35} | ERROR    | {elapsed:>6.2f}s | {str(e)}")
            results[model].append({"test": tc["name"], "success": "ERROR", "latency": elapsed, "detail": str(e)})

print("=" * 80)

