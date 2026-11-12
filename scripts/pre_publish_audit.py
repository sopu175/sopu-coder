"""SopuCoder Pre-Publish File and Security Audit.

Mandatory security and artifact integrity scanner executed prior to git pushes
or remote model/dataset publications.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Set

ROOT_DIR = Path(__file__).resolve().parent.parent

# Explicit Allowlist extensions & directories
ALLOWED_EXTENSIONS: Set[str] = {
    ".py", ".md", ".json", ".jsonl", ".yaml", ".yml", ".txt", ".sh",
    ".gitignore", ".gitattributes", ".jinja", "Modelfile", "LICENSE"
}

FORBIDDEN_EXTENSIONS: Set[str] = {
    ".pem", ".key", ".pkcs12", ".p12", ".id_rsa", ".id_ed25519",
    ".env", ".env.local", ".env.production",
    ".gguf", ".safetensors", ".bin", ".pt", ".pth", ".ckpt"
}

# Regex patterns for sensitive keys or tokens
SECRET_PATTERNS = [
    (re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"]([^'\"]{10,})['\"]"), "API Key"),
    (re.compile(r"(?i)secret[_-]?key\s*[:=]\s*['\"]([^'\"]{10,})['\"]"), "Secret Key"),
    (re.compile(r"(?i)password\s*[:=]\s*['\"]([^'\"]{6,})['\"]"), "Password"),
    (re.compile(r"ghp_[0-9a-zA-Z]{36}"), "GitHub Personal Access Token"),
    (re.compile(r"hf_[0-9a-zA-Z]{34,}"), "Hugging Face Access Token"),
    (re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"), "Private Key Block"),
]


def get_git_status() -> Dict[str, List[str]]:
    """Retrieve untracked and modified files from git status."""
    res = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT_DIR, capture_output=True, text=True)
    lines = res.stdout.strip().splitlines()
    staged: List[str] = []
    unstaged: List[str] = []
    untracked: List[str] = []

    for line in lines:
        if not line:
            continue
        code = line[:2]
        path = line[3:].strip()
        if code.startswith("?"):
            untracked.append(path)
        else:
            if code[0] != " ":
                staged.append(path)
            if code[1] != " ":
                unstaged.append(path)

    return {"staged": staged, "unstaged": unstaged, "untracked": untracked}


def scan_file_for_secrets(file_path: Path) -> List[str]:
    """Scan file text for known credential patterns."""
    findings: List[str] = []
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return [f"Unable to read file: {e}"]

    for pattern, label in SECRET_PATTERNS:
        match = pattern.search(content)
        if match:
            # Mask secret
            findings.append(f"Potential {label} detected (line match redacted)")

    return findings


def calculate_hash(file_path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def run_audit() -> Dict[str, Any]:
    """Run comprehensive repository and pre-publish audit."""
    git_files = get_git_status()
    all_target_files = set(git_files["staged"] + git_files["unstaged"] + git_files["untracked"])

    manifest: List[Dict[str, Any]] = []
    violations: List[str] = []

    for rel_path in sorted(all_target_files):
        # Ignore .venv, .git, and checkpoints handled by gitignore
        if rel_path.startswith(".venv") or rel_path.startswith(".git"):
            continue

        p = ROOT_DIR / rel_path
        if not p.is_file():
            continue

        ext = p.suffix or p.name
        size = p.stat().st_size
        sha256 = calculate_hash(p)

        # Check forbidden extensions
        if ext in FORBIDDEN_EXTENSIONS:
            violations.append(f"Prohibited file type {ext} in {rel_path} (size: {size} bytes)")

        # Scan for secrets
        secret_findings = scan_file_for_secrets(p)
        if secret_findings:
            violations.extend([f"{rel_path}: {f}" for f in secret_findings])

        manifest.append({
            "path": rel_path,
            "extension": ext,
            "size_bytes": size,
            "sha256": sha256,
        })

    report = {
        "status": "PASSED" if not violations else "BLOCKED",
        "total_files_scanned": len(manifest),
        "violations_count": len(violations),
        "violations": violations,
    }

    # Write release-manifest.json and release-audit-report.json
    manifest_path = ROOT_DIR / "release-manifest.json"
    report_path = ROOT_DIR / "release-audit-report.json"

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    return report


if __name__ == "__main__":
    report = run_audit()
    print(f"Audit Status: {report['status']}")
    print(f"Files Scanned: {report['total_files_scanned']}")
    if report["violations"]:
        print("\n❌ Violations Detected:")
        for v in report["violations"]:
            print(f"  - {v}")
        sys.exit(1)
    else:
        print("✅ Pre-Publish Audit Passed cleanly. Manifest generated.")
        sys.exit(0)

