#!/usr/bin/env python3
"""
SopuCoder Dataset Quality Validator & Splitter (v1.1)
Validates schemas, licenses, AST syntax, deduplicates content,
and deterministically generates train/val/test splits without overwriting previous versions.
"""

import argparse
import ast
import hashlib
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

PERMISSIBLE_LICENSES = {
    "apache-2.0",
    "mit",
    "bsd-2-clause",
    "bsd-3-clause",
    "isc",
    "cc0-1.0",
    "unlicense"
}


def compute_hash(text: str) -> str:
    normalized = re.sub(r"\s+", " ", text.strip().lower())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def validate_python_syntax(code_str: str) -> bool:
    try:
        ast.parse(code_str)
        return True
    except SyntaxError:
        return False


def extract_code_blocks(markdown_text: str) -> list:
    pattern = r"```(?:[a-zA-Z0-9_\-\+]+)?\n(.*?)```"
    return re.findall(pattern, markdown_text, re.DOTALL)


def validate_record(record: dict, line_num: int, filename: str) -> tuple[bool, str]:
    required_keys = ["id", "language", "instruction", "output", "metadata"]
    for key in required_keys:
        if key not in record:
            return False, f"Missing required key: '{key}'"

    meta = record.get("metadata", {})
    if not isinstance(meta, dict):
        return False, "'metadata' must be a JSON object"

    license_name = str(meta.get("license", "")).lower()
    if license_name not in PERMISSIBLE_LICENSES:
        return False, f"Impermissible or missing license: '{license_name}'. Allowed: {sorted(list(PERMISSIBLE_LICENSES))}"

    if not record["instruction"].strip():
        return False, "Empty instruction"

    if not record["output"].strip():
        return False, "Empty output"

    if record["language"].lower() == "python":
        blocks = extract_code_blocks(record["output"])
        for block in blocks:
            if not validate_python_syntax(block):
                return False, "Python code block failed AST syntax validation"

    return True, "Valid"


def process_datasets(input_dirs: list[Path], output_dir: Path, split_ratios=(0.7, 0.15, 0.15)):
    all_records = []
    seen_hashes = set()
    duplicates_count = 0
    errors = []
    lang_counter = Counter()
    framework_counter = Counter()

    for d in input_dirs:
        for jsonl_file in d.glob("**/*.jsonl"):
            # Exclude existing split directories to prevent self-ingestion
            if "splits" in jsonl_file.parts or "v1.1" in jsonl_file.parts:
                continue
            with open(jsonl_file, "r", encoding="utf-8") as f:
                for idx, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError as e:
                        errors.append(f"{jsonl_file.name}:{idx} JSON parse error: {e}")
                        continue

                    is_valid, reason = validate_record(record, idx, jsonl_file.name)
                    if not is_valid:
                        errors.append(f"{jsonl_file.name}:{idx} Invalid record ({reason})")
                        continue

                    content_hash = compute_hash(record["instruction"] + " " + record["output"])
                    if content_hash in seen_hashes:
                        duplicates_count += 1
                        continue

                    seen_hashes.add(content_hash)
                    all_records.append(record)
                    lang_counter[record["language"]] += 1
                    framework_counter[record.get("framework", "general")] += 1

    print("\n=======================================================")
    print(" SopuCoder Dataset Validation Summary (v1.1)")
    print("=======================================================")
    print(f" Total Valid Records:   {len(all_records)}")
    print(f" Duplicates Discarded: {duplicates_count}")
    print(f" Errors/Rejected:      {len(errors)}")

    print("\n📊 Records by Language:")
    for lang, count in sorted(lang_counter.items()):
        print(f"  - {lang:12}: {count}")

    print("\n📦 Records by Framework/Category:")
    for fw, count in sorted(framework_counter.items()):
        print(f"  - {fw:16}: {count}")

    if errors:
        print("\nErrors encountered:")
        for err in errors[:10]:
            print(f"  ❌ {err}")

    if not all_records:
        print("No valid records found.")
        return None

    # Deterministic train/val/test split
    import random
    rng = random.Random(42)
    rng.shuffle(all_records)

    n_total = len(all_records)
    n_val = max(2, int(n_total * split_ratios[1]))
    n_test = max(2, int(n_total * split_ratios[2]))
    n_train = n_total - n_val - n_test

    train_set = all_records[:n_train]
    val_set = all_records[n_train:n_train + n_val]
    test_set = all_records[n_train + n_val:]

    output_dir.mkdir(parents=True, exist_ok=True)
    stats = {
        "version": "v1.1.0",
        "total_records": n_total,
        "splits": {
            "train": len(train_set),
            "validation": len(val_set),
            "test": len(test_set)
        },
        "languages": dict(lang_counter),
        "frameworks": dict(framework_counter)
    }

    with open(output_dir / "dataset_stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)

    for name, dataset in [("train.jsonl", train_set), ("val.jsonl", val_set), ("test.jsonl", test_set)]:
        path = output_dir / name
        with open(path, "w", encoding="utf-8") as f:
            for item in dataset:
                f.write(json.dumps(item) + "\n")
        print(f" Exported: {path} ({len(dataset)} samples)")

    return stats


def main():
    parser = argparse.ArgumentParser(description="Validate & version SopuCoder datasets")
    parser.add_argument(
        "--inputs",
        nargs="+",
        default=[
            "datasets/python",
            "datasets/typescript",
            "datasets/javascript",
            "datasets/react",
            "datasets/php",
            "datasets/nextjs",
            "datasets/nodejs",
            "datasets/yii2",
            "datasets/wordpress"
        ]
    )
    parser.add_argument("--output", type=Path, default=Path("datasets/v1.1"))
    args = parser.parse_args()

    input_paths = [Path(p) for p in args.inputs if Path(p).exists()]
    process_datasets(input_paths, args.output)


if __name__ == "__main__":
    main()
