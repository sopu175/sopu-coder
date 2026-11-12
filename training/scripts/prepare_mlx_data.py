#!/usr/bin/env python3
"""
Prepares SopuCoder JSONL datasets into MLX-LM compatible ChatML format.
"""

import json
from pathlib import Path

SYSTEM_PROMPT = """You are SopuCoder, an elite, production-grade AI software engineer and coding assistant.
Your mission is to provide clean, bug-free, idiomatic, and highly maintainable code adhering to strict types, security, and modern full-stack standards."""


def convert_file(input_file: Path, output_file: Path):
    output_file.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            prompt = rec["instruction"]
            if rec.get("input"):
                prompt += f"\n\nContext:\n{rec['input']}"
            output = rec["output"]

            text = f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n{output}<|im_end|>\n"
            fout.write(json.dumps({"text": text}) + "\n")
            count += 1
    print(f"Converted: {input_file} -> {output_file} ({count} lines)")


def main():
    base_in = Path("datasets/v1.1")
    base_out = Path("datasets/v1.1/mlx_data")

    convert_file(base_in / "train.jsonl", base_out / "train.jsonl")
    convert_file(base_in / "val.jsonl", base_out / "valid.jsonl")
    convert_file(base_in / "test.jsonl", base_out / "test.jsonl")
    print(f"All MLX datasets prepared at: {base_out}")


if __name__ == "__main__":
    main()

