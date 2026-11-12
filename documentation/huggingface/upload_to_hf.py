#!/usr/bin/env python3
"""
SopuCoder Hugging Face Release Uploader
Uploads verified model weights, GGUF quantizations, and model cards to Hugging Face Hub.
"""

import argparse
import os
import sys
from pathlib import Path


def upload_artifact(repo_id: str, local_path: Path, repo_type: str = "model", token: str = None):
    try:
        from huggingface_hub import HfApi, create_repo
    except ImportError:
        print("Error: `huggingface_hub` package not installed.", file=sys.stderr)
        print("Install via: pip install huggingface_hub", file=sys.stderr)
        sys.exit(1)

    api = HfApi(token=token or os.environ.get("HF_TOKEN"))
    print(f"Ensuring repository exists: {repo_id} ({repo_type})...")
    create_repo(repo_id=repo_id, repo_type=repo_type, exist_ok=True, token=token)

    if local_path.is_file():
        print(f"Uploading file: {local_path} -> {repo_id}...")
        api.upload_file(
            path_or_fileobj=str(local_path),
            path_in_repo=local_path.name,
            repo_id=repo_id,
            repo_type=repo_type
        )
    elif local_path.is_dir():
        print(f"Uploading folder: {local_path} -> {repo_id}...")
        api.upload_folder(
            folder_path=str(local_path),
            repo_id=repo_id,
            repo_type=repo_type
        )
    print(f"Upload complete! Accessible at: https://huggingface.co/{repo_id}")


def main():
    parser = argparse.ArgumentParser(description="Upload SopuCoder artifacts to Hugging Face")
    parser.add_argument("--repo_id", type=str, required=True, help="HF Repo ID (e.g. sopu175/sopu-coder)")
    parser.add_argument("--path", type=Path, required=True, help="Local file or directory to upload")
    parser.add_argument("--type", type=str, choices=["model", "dataset"], default="model")
    parser.add_argument("--token", type=str, default=None, help="Hugging Face User Access Token")
    args = parser.parse_args()

    upload_artifact(args.repo_id, args.path, args.type, args.token)


if __name__ == "__main__":
    main()
