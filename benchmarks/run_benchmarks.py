"""SopuCoder 18-Domain Baseline Benchmark Runner.

Executes baseline tests across all 18 domains against specified Ollama models,
recording latency, tokens/sec, and code output.
"""
from __future__ import annotations

import argparse
import json
import time
import urllib.request
from pathlib import Path
from typing import Any, Dict, List

ROOT_DIR = Path(__file__).resolve().parent.parent
SUITE_PATH = ROOT_DIR / "benchmarks" / "baseline_suite.json"
RESULTS_DIR = ROOT_DIR / "benchmarks" / "results"


def run_single_test(model: str, test: Dict[str, Any], ollama_url: str) -> Dict[str, Any]:
    """Execute a single benchmark test case."""
    prompt = test["prompt"]
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "top_p": 0.95,
        },
    }

    url = f"{ollama_url.rstrip('/')}/api/generate"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )

    start_time = time.time()
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            duration = time.time() - start_time
    except Exception as e:
        return {
            "id": test["id"],
            "category": test["category"],
            "title": test["title"],
            "error": str(e),
            "status": "FAILED",
        }

    eval_count = data.get("eval_count", 0)
    eval_duration = data.get("eval_duration", 0)
    tokens_per_sec = (eval_count / (eval_duration / 1e9)) if eval_duration > 0 else 0.0

    return {
        "id": test["id"],
        "category": test["category"],
        "title": test["title"],
        "duration_seconds": round(duration, 2),
        "eval_count": eval_count,
        "tokens_per_sec": round(tokens_per_sec, 2),
        "status": "COMPLETED",
        "response_preview": data.get("response", "")[:300].strip(),
        "full_response": data.get("response", ""),
    }


def run_suite(model: str, sample_only: bool = False, ollama_url: str = "http://127.0.0.1:11434") -> Dict[str, Any]:
    """Execute the full 18-domain benchmark suite."""
    with open(SUITE_PATH, "r", encoding="utf-8") as f:
        suite = json.load(f)

    tests_to_run = suite["tests"][:3] if sample_only else suite["tests"]
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"🚀 Running SopuCoder Baseline Benchmark ({len(tests_to_run)} tests) on `{model}`...")
    test_results: List[Dict[str, Any]] = []

    for i, t in enumerate(tests_to_run, 1):
        print(f"[{i}/{len(tests_to_run)}] Evaluating {t['category']} - {t['title']}...", end="", flush=True)
        res = run_single_test(model, t, ollama_url)
        if res.get("status") == "COMPLETED":
            print(f" ✅ ({res['tokens_per_sec']} t/s, {res['duration_seconds']}s)")
        else:
            print(f" ❌ ({res.get('error')})")
        test_results.append(res)

    completed = [r for r in test_results if r.get("status") == "COMPLETED"]
    avg_speed = sum(r["tokens_per_sec"] for r in completed) / len(completed) if completed else 0
    total_tokens = sum(r["eval_count"] for r in completed)
    total_time = sum(r["duration_seconds"] for r in completed)

    summary = {
        "model": model,
        "suite_name": suite["suite_name"],
        "tests_total": len(tests_to_run),
        "tests_passed": len(completed),
        "average_tokens_per_sec": round(avg_speed, 2),
        "total_tokens_generated": total_tokens,
        "total_duration_sec": round(total_time, 2),
        "results": test_results,
    }

    clean_name = model.replace(":", "-").replace("/", "-")
    output_path = RESULTS_DIR / f"{clean_name}_benchmark.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"\n📊 Benchmark Complete! Average Speed: {round(avg_speed, 2)} t/s")
    print(f"Results saved to: {output_path}")
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="sopu-coder:v1-candidate", help="Model to evaluate")
    parser.add_argument("--sample", action="store_true", help="Run only first 3 tests for fast check")
    args = parser.parse_args()

    run_suite(args.model, sample_only=args.sample)
