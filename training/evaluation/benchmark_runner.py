#!/usr/bin/env python3
"""
SopuCoder Automated Benchmark Runner
Executes evaluation test suites against Ollama models (candidate vs base),
measuring code quality criteria and inference latency metrics.
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


def query_ollama(model: str, prompt: str, system: str = None, host: str = "http://localhost:11434"):
    url = f"{host}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "top_p": 0.95
        }
    }
    if system:
        payload["system"] = system

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    
    start_time = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            res_data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"Error querying Ollama ({model}): {e}", file=sys.stderr)
        return None

    elapsed = time.perf_counter() - start_time
    
    eval_count = res_data.get("eval_count", 0)
    eval_duration_ns = res_data.get("eval_duration", 0)
    eval_rate = (eval_count / (eval_duration_ns / 1e9)) if eval_duration_ns > 0 else (eval_count / elapsed)
    prompt_eval_count = res_data.get("prompt_eval_count", 0)
    prompt_eval_duration_ns = res_data.get("prompt_eval_duration", 0)
    prompt_rate = (prompt_eval_count / (prompt_eval_duration_ns / 1e9)) if prompt_eval_duration_ns > 0 else 0

    return {
        "response": res_data.get("response", ""),
        "total_duration_sec": round(elapsed, 3),
        "eval_count": eval_count,
        "tokens_per_sec": round(eval_rate, 2),
        "prompt_tokens": prompt_eval_count,
        "prompt_tokens_per_sec": round(prompt_rate, 2),
    }


def run_benchmark(model: str, benchmarks_file: Path, output_dir: Path):
    with open(benchmarks_file, "r", encoding="utf-8") as f:
        benchmarks = json.load(f)

    output_dir.mkdir(parents=True, exist_ok=True)
    results = {
        "model": model,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "suite_version": benchmarks.get("version", "1.0.0"),
        "tests": []
    }

    print(f"\n=======================================================")
    print(f" Running Benchmark Suite on: {model}")
    print(f" Total Tests: {len(benchmarks['tests'])}")
    print(f"=======================================================\n")

    for i, test in enumerate(benchmarks["tests"], 1):
        test_id = test["id"]
        category = test["category"]
        title = test["title"]
        print(f"[{i}/{len(benchmarks['tests'])}] ({category}) {title} ...", end="", flush=True)

        res = query_ollama(model=model, prompt=test["prompt"])
        if not res:
            print(" [FAILED]")
            continue

        print(f" [DONE] ({res['total_duration_sec']}s, {res['tokens_per_sec']} t/s, {res['eval_count']} tokens)")

        test_result = {
            "id": test_id,
            "category": category,
            "title": title,
            "language": test["language"],
            "eval_criteria": test["eval_criteria"],
            "metrics": {
                "total_duration_sec": res["total_duration_sec"],
                "eval_count": res["eval_count"],
                "tokens_per_sec": res["tokens_per_sec"],
                "prompt_tokens": res["prompt_tokens"]
            },
            "output_preview": res["response"][:300] + ("..." if len(res["response"]) > 300 else ""),
            "full_response": res["response"]
        }
        results["tests"].append(test_result)

    # Calculate aggregate metrics
    avg_speed = sum(t["metrics"]["tokens_per_sec"] for t in results["tests"]) / len(results["tests"]) if results["tests"] else 0
    total_tokens = sum(t["metrics"]["eval_count"] for t in results["tests"])
    total_time = sum(t["metrics"]["total_duration_sec"] for t in results["tests"])

    results["summary"] = {
        "average_tokens_per_sec": round(avg_speed, 2),
        "total_generated_tokens": total_tokens,
        "total_duration_sec": round(total_time, 2),
        "tests_completed": len(results["tests"])
    }

    # Save JSON results
    clean_model_name = model.replace(":", "-").replace("/", "-")
    json_path = output_dir / f"{clean_model_name}-benchmark-results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # Save Markdown Summary
    md_path = output_dir / f"{clean_model_name}-benchmark-results.md"
    generate_markdown_report(results, md_path)

    print(f"\nBenchmark completed successfully!")
    print(f"Results saved to:\n  - {json_path}\n  - {md_path}\n")
    return results


def generate_markdown_report(results: dict, output_file: Path):
    model = results["model"]
    summary = results["summary"]

    lines = [
        f"# 📊 Benchmark Results: `{model}`",
        f"",
        f"- **Timestamp:** {results['timestamp']}",
        f"- **Suite Version:** {results['suite_version']}",
        f"- **Average Speed:** **{summary['average_tokens_per_sec']} tokens/sec**",
        f"- **Total Tokens Generated:** {summary['total_generated_tokens']}",
        f"- **Total Execution Time:** {summary['total_duration_sec']} seconds",
        f"",
        f"## 📋 Category-Wise Performance",
        f"",
        f"| Category | Test Title | Duration (s) | Speed (tokens/s) | Output Tokens |",
        f"| :--- | :--- | :--- | :--- | :--- |"
    ]

    for t in results["tests"]:
        m = t["metrics"]
        lines.append(f"| **{t['category']}** | {t['title']} | {m['total_duration_sec']}s | {m['tokens_per_sec']} t/s | {m['eval_count']} |")

    lines.extend([
        f"",
        f"## 🧪 Detailed Test Outputs & Analysis",
        f""
    ])

    for t in results["tests"]:
        lines.extend([
            f"### {t['category']}: {t['title']}",
            f"- **Language:** {t['language']}",
            f"- **Evaluation Criteria:** {t['eval_criteria']}",
            f"- **Duration:** {t['metrics']['total_duration_sec']}s ({t['metrics']['tokens_per_sec']} tokens/s)",
            f"",
            f"**Model Response:**",
            f"```text",
            f"{t['full_response'].strip()}",
            f"```",
            f"",
            f"---",
            f""
        ])

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description="SopuCoder Benchmark Evaluation")
    parser.add_argument("--model", type=str, required=True, help="Model name (e.g. sopu-coder:v1-candidate)")
    parser.add_argument("--benchmarks", type=Path, default=Path("training/evaluation/benchmarks.json"))
    parser.add_argument("--output", type=Path, default=Path("training/evaluation/results"))
    args = parser.parse_args()

    run_benchmark(args.model, args.benchmarks, args.output)


if __name__ == "__main__":
    main()

