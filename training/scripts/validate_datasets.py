#!/usr/bin/env python3
"""
SopuCoder Dataset Quality Validator & Splitter
Validates dataset schemas, verifies permissive licenses, detects duplicate samples,
checks syntax integrity, and generates deterministic train/val/test splits.
"""

import argparse
import ast
import hashlib
import json
import os
import re
import sys
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

    # If Python, check code syntax if code blocks exist
    if record["language"].lower() == "python":
        blocks = extract_code_blocks(record["output"])
        for block in blocks:
            if not validate_python_syntax(block):
                return False, "Python code block failed AST syntax validation"

    return True, "Valid"


def process_datasets(input_dirs: list[Path], output_dir: Path, split_ratios=(0.8, 0.1, 0.1)):
    all_records = []
    seen_hashes = set()
    duplicates_count = 0
    errors = []

    for d in input_dirs:
        for jsonl_file in d.glob("**/*.jsonl"):
            if "split" in jsonl_file.stem:
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

                    # Check duplicates on instruction + output
                    content_hash = compute_hash(record["instruction"] + " " + record["output"])
                    if content_hash in seen_hashes:
                        duplicates_count += 1
                        continue

                    seen_hashes.add(content_hash)
                    all_records.append(record)

    print(f"\n=======================================================")
    print(f" SopuCoder Dataset Validation Summary")
    print(f"=======================================================")
    print(f" Valid Records: {len(all_records)}")
    print(f" Duplicates Removed: {duplicates_count}")
    print(f" Errors/Rejected: {len(errors)}")

    if errors:
        print("\nErrors encountered:")
        for err in errors[:10]:
            print(f"  ❌ {err}")
        if len(errors) > 10:
            print(f"  ...and {len(errors) - 10} more.")

    if not all_records:
        print("No valid records found to split.")
        return

    # Deterministic shuffle & split
    import random
    rng = random.Random(42)
    rng.shuffle(all_records)

    n_total = len(all_records)
    n_train = int(n_total * split_ratios[0])
    n_val = int(n_total * split_ratios[1])

    train_set = all_records[:n_train]
    val_set = all_records[n_train:n_train + n_val]
    test_set = all_records[n_train + n_val:]

    output_dir.mkdir(parents=True, exist_ok=True)
    for name, dataset in [("train.jsonl", train_set), ("val.jsonl", val_set), ("test.jsonl", test_set)]:
        path = output_dir / name
        with open(path, "w", encoding="utf-8") as f:
            for item in dataset:
                f.write(json.dumps(item) + "\n")
        print(f" Exported: {path} ({len(dataset)} samples)")


def main():
    parser = argparse.ArgumentParser(description="Validate & split SopuCoder datasets")
    parser.add_argument("--inputs", nargs="+", default=["datasets/python", "datasets/typescript", "datasets/javascript", "datasets/react", "datasets/php"])
    parser.add_argument("--output", type=Path, default=Path("datasets/splits"))
    args = parser.parse_args()

    input_paths = [Path(p) for p in args.inputs if Path(p).exists()]
    process_datasets(input_paths, args.output)


if __name__ == "__main__":
    main()
