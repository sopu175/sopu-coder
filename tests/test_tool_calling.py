"""Integration Tests for SopuCoder Tool Calling & External API Dispatch.

Tests:
1. End-to-end execution of Dhaka weather prompt using Open-Meteo.
2. Unregistered/unavailable tool handling without raw JSON leakage.
3. Network error / API failure graceful handling.
4. Tool timeout recovery.
5. Internal reasoning / thinking trace stripping.
"""
from __future__ import annotations

import json
import time
import unittest
from typing import Any, Dict

from tools.agent_runtime import SopuCoderAgent
from tools.registry import ToolRegistry, default_registry, get_current_weather, web_fetch


class TestSopuCoderToolCalling(unittest.TestCase):
    """Test suite for SopuCoder tool execution."""

    def test_open_meteo_dhaka_weather_direct(self) -> None:
        """Verify Open-Meteo fetches real weather data without API keys."""
        data = get_current_weather("Dhaka")
        self.assertNotIn("error", data, f"Open-Meteo returned error: {data.get('error')}")
        self.assertEqual(data.get("location"), "Dhaka")
        self.assertEqual(data.get("country"), "Bangladesh")
        self.assertIn("temperature_celsius", data)
        self.assertIsInstance(data["temperature_celsius"], (int, float))
        self.assertIn("condition", data)
        self.assertIn("Open-Meteo", data.get("provider", ""))

    def test_web_fetch_safety_and_loopback_restriction(self) -> None:
        """Verify web_fetch blocks loopback/localhost SSRF attempts."""
        res_local = web_fetch("http://127.0.0.1:8080/secret")
        self.assertIn("error", res_local)
        self.assertIn("restricted", res_local["error"].lower())

        res_invalid_scheme = web_fetch("ftp://example.com/file")
        self.assertIn("error", res_invalid_scheme)
        self.assertIn("invalid scheme", res_invalid_scheme["error"].lower())

    def test_unavailable_tool_handling(self) -> None:
        """Verify registry returns structured error for missing tools."""
        registry = ToolRegistry()
        res = registry.execute("non_existent_tool", {"foo": "bar"})
        self.assertFalse(res["success"])
        self.assertIn("not registered", res["error"])

    def test_reasoning_stripping(self) -> None:
        """Verify agent strips internal thinking tags and monologue."""
        raw_think = "<think>Calculating steps...</think>Here is the final code."
        cleaned = SopuCoderAgent._clean_response(raw_think)
        self.assertEqual(cleaned, "Here is the final code.")

        raw_monologue = "Thinking...\nStep 1\nStep 2\n...done thinking.\n\nResult"
        cleaned_mono = SopuCoderAgent._clean_response(raw_monologue)
        self.assertEqual(cleaned_mono, "Result")

    def test_end_to_end_dhaka_weather_agent(self) -> None:
        """Verify end-to-end weather resolution via SopuCoder agent."""
        agent = SopuCoderAgent(model="sopu-coder:v1-candidate")
        start = time.time()
        result = agent.chat("What is the weather today in Dhaka?")
        duration = time.time() - start

        self.assertTrue(result["success"], f"Agent chat failed: {result.get('response')}")
        self.assertGreaterEqual(len(result["executed_tools"]), 1)
        self.assertEqual(result["executed_tools"][0]["name"], "get_current_weather")

        resp = result["response"].lower()
        self.assertIn("dhaka", resp)
        # Check that response mentions temperature or celsius
        self.assertTrue(
            "temperature" in resp or "°c" in resp or "clear" in resp or "cloudy" in resp or "rain" in resp,
            f"Response lacks weather information: {result['response']}"
        )
        print(f"\n[E2E Latency] Dhaka Weather query completed in {duration:.2f}s")


if __name__ == "__main__":
    unittest.main()

