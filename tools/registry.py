"""SopuCoder Tool Registry & Built-in Tools.

Provides a centralized registry of executable tools compatible with Ollama's
native tool-calling JSON schema format.
"""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from typing import Any, Callable, Dict, List, Optional


class ToolRegistry:
    """Manages tool registration, schema generation, and execution."""

    def __init__(self) -> None:
        self._tools: Dict[str, Dict[str, Any]] = {}

    def register(
        self,
        name: str,
        description: str,
        parameters: Dict[str, Any],
        func: Callable[..., Any],
    ) -> None:
        """Register a new tool."""
        self._tools[name] = {
            "name": name,
            "description": description,
            "parameters": parameters,
            "func": func,
        }

    def get_ollama_tools_schema(self) -> List[Dict[str, Any]]:
        """Return tool definitions in Ollama / OpenAI function format."""
        schema = []
        for name, tool in self._tools.items():
            schema.append(
                {
                    "type": "function",
                    "function": {
                        "name": tool["name"],
                        "description": tool["description"],
                        "parameters": tool["parameters"],
                    },
                }
            )
        return schema

    def has_tool(self, name: str) -> bool:
        """Check if tool is registered."""
        return name in self._tools

    def execute(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a registered tool with provided arguments."""
        if not self.has_tool(name):
            return {
                "success": False,
                "error": f"Tool '{name}' is not registered or unavailable.",
                "available_tools": list(self._tools.keys()),
            }

        tool = self._tools[name]
        try:
            result = tool["func"](**arguments)
            return {"success": True, "result": result}
        except TypeError as te:
            return {
                "success": False,
                "error": f"Invalid arguments for tool '{name}': {str(te)}",
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error executing tool '{name}': {str(e)}",
            }


# Global default registry
default_registry = ToolRegistry()


def register_tool(
    name: str,
    description: str,
    parameters: Dict[str, Any],
    registry: Optional[ToolRegistry] = None,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator to register a tool."""
    target_registry = registry or default_registry

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        target_registry.register(name, description, parameters, func)
        return func

    return decorator


# ==============================================================================
# Built-in Standard Tools
# ==============================================================================

WMO_WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


@register_tool(
    name="get_current_weather",
    description="Retrieve live, real-time weather conditions for any city or location using Open-Meteo. Requires no API keys.",
    parameters={
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City name, province, or country (e.g. 'Dhaka', 'Tokyo', 'London').",
            }
        },
        "required": ["location"],
    },
)
def get_current_weather(location: str) -> Dict[str, Any]:
    """Fetch real-time weather via Open-Meteo without requiring any API keys."""
    # Step 1: Geocoding lookup
    clean_location = location.strip()
    encoded_loc = urllib.parse.quote(clean_location)
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={encoded_loc}&count=1&language=en&format=json"

    req_geo = urllib.request.Request(
        geo_url,
        headers={"User-Agent": "SopuCoder-Agent/1.0 (https://github.com/sopu175/sopu-coder)"},
    )

    try:
        with urllib.request.urlopen(req_geo, timeout=5) as response:
            geo_data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        return {"error": f"Failed to connect to geocoding service: {str(e)}"}

    if not geo_data.get("results"):
        return {"error": f"Location '{location}' could not be resolved to geographic coordinates."}

    loc_info = geo_data["results"][0]
    lat = loc_info["latitude"]
    lon = loc_info["longitude"]
    resolved_name = loc_info.get("name", location)
    country = loc_info.get("country", "")

    # Step 2: Weather forecast query
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,"
        f"apparent_temperature,precipitation,weather_code,wind_speed_10m"
    )

    req_weather = urllib.request.Request(
        weather_url,
        headers={"User-Agent": "SopuCoder-Agent/1.0 (https://github.com/sopu175/sopu-coder)"},
    )

    try:
        with urllib.request.urlopen(req_weather, timeout=5) as response:
            weather_data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        return {"error": f"Failed to retrieve weather data from Open-Meteo: {str(e)}"}

    curr = weather_data.get("current", {})
    w_code = curr.get("weather_code", 0)
    condition_desc = WMO_WEATHER_CODES.get(w_code, "Unknown condition")

    return {
        "location": resolved_name,
        "country": country,
        "latitude": lat,
        "longitude": lon,
        "timestamp_utc": curr.get("time"),
        "temperature_celsius": curr.get("temperature_2m"),
        "apparent_temperature_celsius": curr.get("apparent_temperature"),
        "relative_humidity_percent": curr.get("relative_humidity_2m"),
        "wind_speed_kmh": curr.get("wind_speed_10m"),
        "precipitation_mm": curr.get("precipitation"),
        "condition": condition_desc,
        "provider": "Open-Meteo (open-source, keyless)",
    }


@register_tool(
    name="web_fetch",
    description="Securely fetch and read the plain-text content or JSON from an HTTP/HTTPS URL. Never use fake API keys.",
    parameters={
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The absolute HTTP or HTTPS URL to fetch.",
            },
            "max_length": {
                "type": "integer",
                "description": "Maximum characters to return (default: 4000).",
            },
        },
        "required": ["url"],
    },
)
def web_fetch(url: str, max_length: int = 4000) -> Dict[str, Any]:
    """Safely fetch public web content."""
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return {"error": f"Invalid scheme '{parsed.scheme}'. Only http and https URLs are allowed."}

    # Block localhost/internal endpoints for SSRF defense
    hostname = (parsed.hostname or "").lower()
    if hostname in ("localhost", "127.0.0.1", "0.0.0.0", "::1"):
        return {"error": "Access to local loopback addresses is restricted."}

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "SopuCoder-Agent/1.0"},
    )

    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            content_type = response.headers.get("Content-Type", "")
            raw_bytes = response.read(max_length * 2)
            text = raw_bytes.decode("utf-8", errors="replace")[:max_length]
            return {
                "url": url,
                "status_code": response.status,
                "content_type": content_type,
                "content": text,
            }
    except Exception as e:
        return {"error": f"Failed to fetch '{url}': {str(e)}"}

