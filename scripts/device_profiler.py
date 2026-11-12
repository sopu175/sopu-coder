#!/usr/bin/env python3
"""
SopuCoder Device Profiler & Runtime Optimizer
Author: Md. Saiful Islam (Saif)
Project: SopuCoder

Zero-dependency hardware analyzer: works out-of-the-box on Mac, Linux, Windows,
Android (Termux), and Raspberry Pi without requiring any pip packages.
"""

import os
import sys
import platform
import subprocess

def get_ram_gb():
    system = platform.system()
    try:
        if system == "Darwin":
            out = subprocess.check_output(["sysctl", "-n", "hw.memsize"], text=True).strip()
            return round(int(out) / (1024 ** 3), 1)
        elif system == "Linux":
            with open("/proc/meminfo", "r") as f:
                for line in f:
                    if line.startswith("MemTotal:"):
                        kb = int(line.split()[1])
                        return round(kb / (1024 ** 2), 1)
        elif system == "Windows":
            out = subprocess.check_output(["wmic", "computersystem", "get", "totalphysicalmemory"], text=True)
            lines = [l.strip() for l in out.splitlines() if l.strip().isdigit()]
            if lines:
                return round(int(lines[0]) / (1024 ** 3), 1)
    except Exception:
        pass
    return 8.0  # safe fallback assumption

def get_system_specs():
    system = platform.system()
    arch = platform.machine()
    ram_gb = get_ram_gb()
    cpu_count = os.cpu_count() or 4
    gpu = "None (CPU only)"
    backend = "CPU"

    # Detect Apple Silicon Metal
    if system == "Darwin" and arch in ["arm64", "aarch64"]:
        gpu = "Apple Silicon Unified Memory (Metal accelerated)"
        backend = "Metal"
    elif system == "Darwin":
        gpu = "Intel Mac (Metal available)"
        backend = "Metal"
    else:
        # Check NVIDIA CUDA
        try:
            res = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
                                 capture_output=True, text=True, timeout=2)
            if res.returncode == 0 and res.stdout.strip():
                gpu = res.stdout.strip().replace("\n", "; ")
                backend = "CUDA"
        except Exception:
            pass

    return {
        "os": system,
        "arch": arch,
        "ram_gb": ram_gb,
        "cpu_count": cpu_count,
        "gpu": gpu,
        "backend": backend
    }

def recommend_tier(specs):
    ram = specs["ram_gb"]
    backend = specs["backend"]

    if ram < 4.0:
        tier = "Tier 1: Ultra-Light / Edge"
        model = "sopu175/sopu-coder-nano (0.5B / 1.5B)"
        quant = "Q4_K_M or Q3_K_L"
        context = 4096
        advice = "Ideal for Android/Termux, Raspberry Pi, or 2GB-4GB laptops. Use llama.cpp CPU threads or WebLLM."
        ollama_cmd = "ollama run sopu175/sopu-coder-nano:latest"
    elif ram <= 8.5:
        tier = "Tier 2: Fast & Lightweight"
        model = "sopu175/sopu-coder-fast:latest (4B)"
        quant = "Q4_K_M"
        context = 16384
        advice = "Ideal for 8GB Mac/Windows laptops. Delivers 30-50+ tok/s autocomplete and rapid debugging."
        ollama_cmd = "ollama run sopu175/sopu-coder-fast:latest"
    elif ram <= 24.0:
        tier = "Tier 3: Flagship Full-Stack"
        model = "sopu175/sopu-coder:latest (7B)"
        quant = "Q4_K_M or Q5_K_M"
        context = 32768
        advice = "Ideal for 16GB Apple Silicon & NVIDIA RTX 3060/4060. Full agentic reasoning and complex coding."
        ollama_cmd = "ollama run sopu175/sopu-coder:latest"
    else:
        tier = "Tier 4: Workstation / Pro"
        model = "sopu175/sopu-coder-pro:latest (14B / 32B)"
        quant = "Q4_K_M or Q8_0"
        context = 65536
        advice = "Ideal for 32GB-64GB workstations and cloud servers. Maximum algorithmic depth and repo comprehension."
        ollama_cmd = "ollama run sopu175/sopu-coder-pro:latest"

    return {
        "tier": tier,
        "model": model,
        "quant": quant,
        "context": context,
        "advice": advice,
        "ollama_cmd": ollama_cmd
    }

def main():
    print("==================================================")
    print("  SopuCoder Hardware Profiler & Tier Recommender  ")
    print("  Creator: Md. Saiful Islam (Saif)                ")
    print("==================================================")
    specs = get_system_specs()
    print(f"OS:            {specs['os']} ({specs['arch']})")
    print(f"CPU Threads:   {specs['cpu_count']}")
    print(f"Total RAM:     {specs['ram_gb']} GB")
    print(f"GPU / Engine:  {specs['gpu']}")
    print(f"Acceleration:  {specs['backend']}")
    print("--------------------------------------------------")
    rec = recommend_tier(specs)
    print(f"Recommended Tier:   {rec['tier']}")
    print(f"Optimal Model:      {rec['model']}")
    print(f"Quantization:       {rec['quant']}")
    print(f"Max Context Limit:  {rec['context']} tokens")
    print(f"Strategy:           {rec['advice']}")
    print("--------------------------------------------------")
    print(f"Quick Launch Command:")
    print(f"  {rec['ollama_cmd']}")
    print("==================================================")

if __name__ == "__main__":
    main()
