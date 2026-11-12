#!/usr/bin/env python3
"""
SopuCoder QLoRA / LoRA Fine-Tuning Pipeline
Fine-tunes Qwen2.5-Coder base models on SopuCoder curated datasets using PEFT & TRL SFTTrainer.
"""

import argparse
import json
import os
import sys
from pathlib import Path
import yaml

import torch
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from trl import SFTTrainer

SYSTEM_PROMPT = """You are SopuCoder, an elite, production-grade AI software engineer and coding assistant.
Your mission is to provide clean, bug-free, idiomatic, and highly maintainable code adhering to strict types, security, and modern full-stack standards."""


def format_chatml(sample: dict) -> str:
    """Formats an instruction sample into ChatML template format."""
    instruction = sample["instruction"]
    if sample.get("input"):
        instruction += f"\n\nContext:\n{sample['input']}"
    output = sample["output"]

    text = f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n"
    text += f"<|im_start|>user\n{instruction}<|im_end|>\n"
    text += f"<|im_start|>assistant\n{output}<|im_end|>"
    return {"text": text}


def load_config(config_path: Path) -> dict:
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="SopuCoder LoRA / QLoRA Fine-Tuning")
    parser.add_argument("--config", type=Path, default=Path("training/fine-tuning/config.yaml"))
    args = parser.parse_args()

    cfg = load_config(args.config)
    print("=======================================================")
    print(f" Starting SopuCoder Fine-Tuning: {cfg['project_name']}")
    print(f" Base Model: {cfg['model_name_or_path']}")
    print("=======================================================")

    # 1. Quantization Configuration (4-bit QLoRA)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16 if cfg.get("bf16", True) else torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    # 2. Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        cfg["model_name_or_path"],
        trust_remote_code=True,
        padding_side="right"
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # 3. Model Loading
    device_map = "auto" if torch.cuda.is_available() else "cpu"
    model = AutoModelForCausalLM.from_pretrained(
        cfg["model_name_or_path"],
        quantization_config=bnb_config if torch.cuda.is_available() else None,
        device_map=device_map,
        trust_remote_code=True,
    )

    if torch.cuda.is_available():
        model = prepare_model_for_kbit_training(model)

    # 4. LoRA Setup
    peft_config = LoraConfig(
        r=cfg.get("lora_r", 16),
        lora_alpha=cfg.get("lora_alpha", 32),
        lora_dropout=cfg.get("lora_dropout", 0.05),
        target_modules=cfg.get("target_modules", ["q_proj", "v_proj"]),
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    # 5. Load and Format Datasets
    data_files = {"train": cfg["train_file"]}
    if cfg.get("validation_file") and Path(cfg["validation_file"]).exists():
        data_files["validation"] = cfg["validation_file"]

    raw_datasets = load_dataset("json", data_files=data_files)
    formatted_train = raw_datasets["train"].map(format_chatml)
    formatted_eval = raw_datasets["validation"].map(format_chatml) if "validation" in raw_datasets else None

    # 6. Training Arguments
    training_args = TrainingArguments(
        output_dir=cfg["output_dir"],
        per_device_train_batch_size=cfg.get("per_device_train_batch_size", 2),
        gradient_accumulation_steps=cfg.get("gradient_accumulation_steps", 8),
        learning_rate=float(cfg.get("learning_rate", 2e-4)),
        lr_scheduler_type=cfg.get("lr_scheduler_type", "cosine"),
        warmup_ratio=cfg.get("warmup_ratio", 0.05),
        num_train_epochs=cfg.get("num_train_epochs", 3),
        logging_steps=cfg.get("logging_steps", 10),
        save_strategy=cfg.get("save_strategy", "epoch"),
        eval_strategy=cfg.get("evaluation_strategy", "epoch") if formatted_eval else "no",
        bf16=cfg.get("bf16", False) and torch.cuda.is_bf16_supported(),
        fp16=cfg.get("fp16", False) or (not torch.cuda.is_bf16_supported() and torch.cuda.is_available()),
        gradient_checkpointing=cfg.get("gradient_checkpointing", True),
        optim=cfg.get("optim", "paged_adamw_8bit") if torch.cuda.is_available() else "adamw_torch",
        seed=cfg.get("seed", 42),
        report_to="none",
    )

    # 7. SFT Trainer
    trainer = SFTTrainer(
        model=model,
        train_dataset=formatted_train,
        eval_dataset=formatted_eval,
        peft_config=peft_config,
        dataset_text_field="text",
        max_seq_length=cfg.get("max_seq_length", 4096),
        tokenizer=tokenizer,
        args=training_args,
    )

    print("\nStarting training loop...")
    trainer.train()

    # 8. Save Trained Adapter
    final_output = Path(cfg["output_dir"]) / "final_adapter"
    trainer.model.save_pretrained(final_output)
    tokenizer.save_pretrained(final_output)
    print(f"\nTraining completed! LoRA adapter saved to: {final_output}")


if __name__ == "__main__":
    main()

