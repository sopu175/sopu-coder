#!/usr/bin/env python3
"""
SopuCoder Secure Agent Runtime
================================
Validates and executes native structured tool calls from Ollama models.
Enforces the security rule: NEVER execute raw JSON parsed from message.content.
"""

import json
import os
import glob as glob_module
import time
from typing import Callable, Dict, Any, List
import ollama

class SecureAgentRuntime:
    def __init__(self, model: str = "sopu-coder:latest", max_turns: int = 5):
        self.model = model
        self.max_turns = max_turns
        self.client = ollama.Client()
        self.tools: Dict[str, Dict[str, Any]] = {}

    def register_tool(self, name: str, description: str, parameters: Dict[str, Any], func: Callable):
        """Register a Python function as a tool with JSON Schema definition."""
        self.tools[name] = {
            "schema": {
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": parameters,
                }
            },
            "func": func,
        }

    def get_tool_definitions(self) -> List[Dict[str, Any]]:
        return [t["schema"] for t in self.tools.values()]

    def run(self, user_prompt: str, verbose: bool = True) -> str:
        messages = [{"role": "user", "content": user_prompt}]
        turn = 0
        total_latency = 0.0

        if verbose:
            print(f"\n[Agent Runtime] User Prompt: {user_prompt}")
            print(f"[Agent Runtime] Using Model: {self.model}")

        while turn < self.max_turns:
            turn += 1
            start_t = time.time()
            response = self.client.chat(
                model=self.model,
                messages=messages,
                tools=self.get_tool_definitions(),
            )
            elapsed = time.time() - start_t
            total_latency += elapsed

            msg = response.message
            tool_calls = msg.tool_calls

            # SECURITY GUARD: Never execute untrusted raw JSON from msg.content
            if not tool_calls:
                # Model returned a direct text answer
                if verbose:
                    print(f"[Agent Runtime] Final Answer produced in {elapsed:.2f}s (turn {turn}):")
                return msg.content

            # Tool calls exist and were structurally parsed by Ollama server
            if verbose:
                print(f"[Agent Runtime] Validated Structured Tool Call(s) received in {elapsed:.2f}s:")

            # Append the assistant's tool-calling message to history
            messages.append(msg)

            for call in tool_calls:
                fn_name = call.function.name
                fn_args = call.function.arguments or {}

                if verbose:
                    print(f"  -> Invoking tool '{fn_name}' with arguments: {fn_args}")

                if fn_name not in self.tools:
                    result = {"error": f"Tool '{fn_name}' is not registered."}
                else:
                    try:
                        result = self.tools[fn_name]["func"](**fn_args)
                    except Exception as e:
                        result = {"error": str(e)}

                if verbose:
                    print(f"  <- Tool Output: {result}")

                # Append tool result to conversation history for model to synthesize
                messages.append({
                    "role": "tool",
                    "content": json.dumps(result, ensure_ascii=False)
                })

        return "Agent reached maximum allowed turns without concluding."

# Standard tools for codebase exploration
def tool_glob(pattern: str = "*") -> Dict[str, Any]:
    matches = glob_module.glob(pattern, recursive=True)
    return {"matches": matches[:10], "total_matches": len(matches)}

def tool_read_file(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        return {"error": f"File '{path}' does not exist."}
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read(500)
    return {"path": path, "preview": content}

if __name__ == "__main__":
    runtime = SecureAgentRuntime(model="sopu-coder:latest")
    runtime.register_tool(
        name="glob",
        description="Find files matching pattern in current directory",
        parameters={
            "type": "object",
            "properties": {"pattern": {"type": "string"}},
            "required": ["pattern"]
        },
        func=tool_glob
    )
    runtime.register_tool(
        name="read_file",
        description="Read the beginning of a file",
        parameters={
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"]
        },
        func=tool_read_file
    )

    answer = runtime.run("index the codebase full and summarize what files exist")
    print("\nResult:\n", answer)

