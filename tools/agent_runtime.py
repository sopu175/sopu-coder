"""SopuCoder Tool-Calling & Agent Runtime Engine.

Connects to Ollama's /api/chat endpoint, handles native and content-embedded
tool calls, executes registered tools (e.g. Open-Meteo weather, web fetching),
and dispatches synthesized tool responses back to SopuCoder.
"""
from __future__ import annotations

import json
import re
import urllib.request
import urllib.error
from typing import Any, Dict, List, Optional, Tuple

from tools.registry import ToolRegistry, default_registry


class SopuCoderAgent:
    """Agent runtime managing conversation state, tool calls, and execution."""

    def __init__(
        self,
        model: str = "sopu-coder:v1-candidate",
        registry: Optional[ToolRegistry] = None,
        ollama_url: str = "http://127.0.0.1:11434",
        system_prompt: Optional[str] = None,
        timeout: int = 60,
    ) -> None:
        self.model = model
        self.registry = registry or default_registry
        self.ollama_url = ollama_url.rstrip("/")
        self.system_prompt = system_prompt
        self.timeout = timeout
        self.history: List[Dict[str, Any]] = []

    def reset(self) -> None:
        """Reset conversation history."""
        self.history = []

    def _call_ollama(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:
        """Send HTTP POST request to Ollama /api/chat."""
        url = f"{self.ollama_url}/api/chat"
        payload: Dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "stream": False,
        }
        if tools:
            payload["tools"] = tools

        data_bytes = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data_bytes,
            headers={"Content-Type": "application/json", "User-Agent": "SopuCoder-Agent/1.0"},
        )

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.URLError as e:
            return {"error": f"Failed to connect to Ollama at {url}: {str(e)}"}
        except Exception as e:
            return {"error": f"Ollama communication error: {str(e)}"}

    def _extract_tool_calls(self, message: Dict[str, Any]) -> List[Tuple[str, Dict[str, Any]]]:
        """Extract tool calls from native message.tool_calls or JSON content."""
        calls: List[Tuple[str, Dict[str, Any]]] = []

        # 1. Native Ollama tool_calls
        if "tool_calls" in message and message["tool_calls"]:
            for tc in message["tool_calls"]:
                func = tc.get("function", {})
                name = func.get("name")
                args = func.get("arguments", {})
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except json.JSONDecodeError:
                        args = {}
                if name:
                    calls.append((name, args))
            return calls

        # 2. Check content for tool call markers or JSON object
        content = (message.get("content") or "").strip()
        if not content:
            return calls

        # Pattern: <tool_call>{"name": ..., "arguments": ...}</tool_call>
        match_tc = re.search(r"<tool_call>\s*(\{.*?\})\s*</tool_call>", content, re.DOTALL)
        if match_tc:
            try:
                parsed = json.loads(match_tc.group(1))
                if "name" in parsed:
                    return [(parsed["name"], parsed.get("arguments", {}))]
            except json.JSONDecodeError:
                pass

        # Pattern: ```json {"name": "...", "arguments": {...}} ``` or bare JSON
        clean_content = content
        if clean_content.startswith("```json"):
            clean_content = clean_content[7:]
        if clean_content.startswith("```"):
            clean_content = clean_content[3:]
        if clean_content.endswith("```"):
            clean_content = clean_content[:-3]
        clean_content = clean_content.strip()

        if clean_content.startswith("{") and clean_content.endswith("}"):
            try:
                parsed = json.loads(clean_content)
                if isinstance(parsed, dict) and "name" in parsed and "arguments" in parsed:
                    return [(parsed["name"], parsed.get("arguments", {}))]
            except json.JSONDecodeError:
                pass

        return calls

    @staticmethod
    def _clean_response(content: str) -> str:
        """Strip internal thinking/reasoning tokens if exposed by model."""
        if not content:
            return ""
        # Strip <think>...</think>
        cleaned = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL)
        # Strip Thinking... ...done thinking.
        cleaned = re.sub(r"Thinking\.\.\..*?\.\.\.done thinking\.", "", cleaned, flags=re.DOTALL)
        return cleaned.strip()

    def chat(self, user_prompt: str, max_turns: int = 5) -> Dict[str, Any]:
        """Execute a user query through the full agent tool-calling loop."""
        if not self.history and self.system_prompt:
            self.history.append({"role": "system", "content": self.system_prompt})

        self.history.append({"role": "user", "content": user_prompt})

        tools_schema = self.registry.get_ollama_tools_schema()
        executed_tool_calls: List[Dict[str, Any]] = []

        for turn in range(max_turns):
            response = self._call_ollama(self.history, tools=tools_schema)

            if "error" in response:
                return {
                    "success": False,
                    "response": f"Ollama Error: {response['error']}",
                    "executed_tools": executed_tool_calls,
                }

            msg = response.get("message", {})
            tool_calls = self._extract_tool_calls(msg)

            if not tool_calls:
                # No tool called, we have final answer
                final_text = self._clean_response(msg.get("content", ""))
                self.history.append({"role": "assistant", "content": final_text})
                return {
                    "success": True,
                    "response": final_text,
                    "executed_tools": executed_tool_calls,
                    "turns": turn + 1,
                }

            # We have tool calls to execute
            self.history.append(msg)

            for tool_name, tool_args in tool_calls:
                # Execute tool
                execution_result = self.registry.execute(tool_name, tool_args)
                executed_tool_calls.append({
                    "name": tool_name,
                    "arguments": tool_args,
                    "output": execution_result,
                })

                # Append tool response
                tool_msg = {
                    "role": "tool",
                    "content": json.dumps(execution_result),
                }
                self.history.append(tool_msg)

        # Max turns reached without final text
        return {
            "success": False,
            "response": "Exceeded maximum tool-calling turns.",
            "executed_tools": executed_tool_calls,
        }
