#!/usr/bin/env python3
"""
SopuCoder In-Depth Stress Test Suite
====================================
Tests multi-tool calling, negative constraints, diff generation,
complex architectural reasoning, and Bengali technical comprehension.
"""

import time
import json
import ollama

client = ollama.Client()
model = "sopu-coder:latest"

tests = []

def run_test(name, fn):
    print(f"\n--- Running: {name} ---")
    t0 = time.time()
    try:
        res = fn()
        elapsed = time.time() - t0
        print(f"Status: COMPLETED ({elapsed:.2f}s)")
        tests.append({"name": name, "status": "COMPLETED", "elapsed": elapsed, "result": res})
    except Exception as e:
        elapsed = time.time() - t0
        print(f"Status: FAILED ({elapsed:.2f}s) - {e}")
        tests.append({"name": name, "status": "FAILED", "elapsed": elapsed, "result": str(e)})

# 1. Multi-Tool (Parallel Tool Calling)
def test_parallel_tools():
    tools = [
        {"type": "function", "function": {"name": "read_file", "parameters": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}}},
        {"type": "function", "function": {"name": "run_bash", "parameters": {"type": "object", "properties": {"command": {"type": "string"}}, "required": ["command"]}}}
    ]
    prompt = "Read both 'package.json' and 'README.md' simultaneously to understand the project dependencies and overview."
    resp = client.chat(model=model, messages=[{"role": "user", "content": prompt}], tools=tools)
    calls = resp.message.tool_calls
    return {"tool_calls_count": len(calls) if calls else 0, "calls": [c.function.name for c in calls] if calls else [], "content": resp.message.content[:100]}

# 2. Negative Constraint (Do NOT use X)
def test_negative_constraint():
    prompt = "Write a function in Python to fetch data from an HTTP API. CRITICAL CONSTRAINT: Do NOT use the 'requests' library, do NOT use 'urllib', and do NOT use 'aiohttp'."
    resp = client.chat(model=model, messages=[{"role": "user", "content": prompt}])
    content = resp.message.content
    violations = [lib for lib in ["import requests", "import urllib", "import aiohttp", "from requests", "from urllib"] if lib in content]
    return {"violations": violations, "passed": len(violations) == 0, "preview": content[:200]}

# 3. Code Diff (Search and Replace format)
def test_code_diff():
    prompt = """Here is a file:
```python
def calculate_tax(subtotal):
    tax_rate = 0.05
    return subtotal * tax_rate
```
Update the tax rate to 0.08 using a unified diff or search/replace block. Do NOT rewrite the entire function."""
    resp = client.chat(model=model, messages=[{"role": "user", "content": prompt}])
    content = resp.message.content
    has_diff = ("<<<" in content and ">>>" in content) or ("---" in content and "+++" in content) or ("SEARCH" in content and "REPLACE" in content)
    return {"has_diff": has_diff, "preview": content[:250]}

# 4. Complex Bengali Technical Explanation (Race conditions & Mutex)
def test_bengali_concurrency():
    prompt = "Node.js e race condition ebong asynchronous event loop e shared resource conflict kivabe hoi? Eta kivabe prevent kora jai shobuj/shundor banglay bujhiye bolo."
    resp = client.chat(model=model, messages=[{"role": "user", "content": prompt}])
    content = resp.message.content
    # Check if response is actually in Bengali or if it fell back to English
    bengali_chars = sum(1 for c in content if '\u0980' <= c <= '\u09FF')
    total_chars = len(content.strip())
    bengali_ratio = (bengali_chars / total_chars) if total_chars > 0 else 0
    return {"bengali_ratio": f"{bengali_ratio * 100:.1f}%", "preview": content[:200]}

# 5. Hallucination / Edge-Case Framework
def test_hallucination():
    prompt = "How do I configure Server Actions in Next.js 11 Pages Router?"
    resp = client.chat(model=model, messages=[{"role": "user", "content": prompt}])
    content = resp.message.content
    # Server Actions did not exist in Next.js 11 Pages Router (introduced in Next 13.4 App Router).
    # A smart model should flag that Server Actions do not exist in Next.js 11 Pages Router!
    correctly_flagged = any(phrase in content.lower() for phrase in ["not supported", "introduced in", "next.js 13", "next.js 14", "does not exist", "app router", "only in"])
    return {"correctly_flagged": correctly_flagged, "preview": content[:200]}

run_test("Parallel Tool Calling", test_parallel_tools)
run_test("Negative Constraints", test_negative_constraint)
run_test("Code Diff / Search-Replace", test_code_diff)
run_test("Bengali Technical Depth", test_bengali_concurrency)
run_test("Framework Hallucination Check", test_hallucination)

print("\n" + "=" * 60)
print("FINAL SUMMARY REPORT:")
print("=" * 60)
for t in tests:
    print(f"\n* {t['name']}:")
    print(json.dumps(t['result'], indent=2, ensure_ascii=False))

