#!/usr/bin/env python3
"""
SopuCoder Model Merger & GGUF Exporter
Merges trained LoRA adapter weights with base foundation model,
and prepares artifacts for llama.cpp GGUF quantization and Ollama publishing.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def merge_lora(base_model_name: str, adapter_dir: Path, output_dir: Path):
    print(f"Loading base model: {base_model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )

    print(f"Loading LoRA adapter: {adapter_dir}...")
    model = PeftModel.from_pretrained(base_model, adapter_dir)

    print("Merging weights (merge_and_unload)...")
    merged_model = model.merge_and_unload()

    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Saving merged 16-bit model to: {output_dir}...")
    merged_model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    print("Merged model successfully saved.")


def generate_ollama_modelfile(gguf_file: Path, output_modelfile: Path, model_variant: str = "sopu-coder"):
    content = f"""# ==============================================================================
# SopuCoder Fine-Tuned GGUF Model
# ==============================================================================

FROM {gguf_file.resolve()}

PARAMETER temperature 0.2
PARAMETER top_p 0.95
PARAMETER repeat_penalty 1.05
PARAMETER num_ctx 32768
PARAMETER stop "<|im_end|>"
PARAMETER stop "<|endoftext|>"

SYSTEM \"\"\"You are SopuCoder, an elite, production-grade AI software engineer and coding assistant fine-tuned on curated modern full-stack datasets.\"\"\"
"""
    with open(output_modelfile, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated Ollama Modelfile at: {output_modelfile}")


def main():
    parser = argparse.ArgumentParser(description="Merge LoRA and export for GGUF/Ollama")
    parser.add_argument("--base_model", type=str, default="Qwen/Qwen2.5-Coder-7B-Instruct")
    parser.add_argument("--adapter_dir", type=Path, default=Path("./training/checkpoints/sopu-coder-lora/final_adapter"))
    parser.add_argument("--merged_output", type=Path, default=Path("./training/checkpoints/sopu-coder-merged"))
    parser.add_argument("--modelfile_output", type=Path, default=Path("./sopu-coder/Modelfile.release"))
    args = parser.parse_args()

    if not args.adapter_dir.exists():
        print(f"Adapter directory not found: {args.adapter_dir}")
        print("Run `train_lora.py` first to produce trained adapter checkpoints.")
        sys.exit(1)

    merge_lora(args.base_model, args.adapter_dir, args.merged_output)
    generate_ollama_modelfile(args.merged_output / "sopu-coder-Q4_K_M.gguf", args.modelfile_output)


if __name__ == "__main__":
    main()

