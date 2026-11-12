"""SopuCoder Command-Line Interface with Native Tool Execution.

Usage:
    python -m tools.cli --model sopu-coder "What is the weather today in Dhaka?"
    python -m tools.cli --interactive
"""
from __future__ import annotations

import argparse
import sys
from typing import Optional

from tools.agent_runtime import SopuCoderAgent


def run_single_query(model: str, prompt: str, verbose: bool = False) -> int:
    """Run a single prompt through SopuCoder with tool execution."""
    agent = SopuCoderAgent(model=model)
    if verbose:
        print(f"Connecting to SopuCoder ({model})...")

    result = agent.chat(prompt)

    if verbose and result.get("executed_tools"):
        print("\n--- 🛠️ Executed Tools ---")
        for t in result["executed_tools"]:
            print(f"- Tool: {t['name']}")
            print(f"  Arguments: {t['arguments']}")
            print(f"  Result: {t['output']}")
        print("-------------------------\n")

    if result["success"]:
        print(result["response"])
        return 0
    else:
        print(f"Error: {result['response']}", file=sys.stderr)
        return 1


def run_interactive(model: str) -> None:
    """Run interactive conversation loop."""
    agent = SopuCoderAgent(model=model)
    print(f"🤖 SopuCoder Interactive Session ({model})")
    print("Type 'exit', 'quit', or 'reset' to control the session.\n")

    while True:
        try:
            prompt = input("You > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSession ended.")
            break

        if not prompt:
            continue
        if prompt.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        if prompt.lower() == "reset":
            agent.reset()
            print("Conversation reset.")
            continue

        result = agent.chat(prompt)
        if result.get("executed_tools"):
            for t in result["executed_tools"]:
                print(f"[🛠️ Tool executed: {t['name']}({t['arguments']})]")

        print(f"\nSopuCoder > {result['response']}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="SopuCoder CLI with Live Tool Execution")
    parser.add_argument(
        "--model",
        default="sopu-coder:v1-candidate",
        help="Ollama model name (default: sopu-coder:v1-candidate)",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Start an interactive chat session",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Display executed tool calls and intermediate states",
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Prompt to send to SopuCoder",
    )

    args = parser.parse_args()

    if args.interactive:
        run_interactive(args.model)
    elif args.prompt:
        sys.exit(run_single_query(args.model, args.prompt, verbose=args.verbose))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

