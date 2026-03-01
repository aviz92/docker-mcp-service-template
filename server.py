from typing import Any

from custom_python_logger import build_logger
from dotenv import load_dotenv
from mcp.server import FastMCP
from requests.exceptions import HTTPError, RequestException

from mcp_services.ping_service import PingService
from mcp_services.weather_service import WeatherService

load_dotenv()

logger = build_logger(project_name="MCP Service")

# Create an MCP server
mcp = FastMCP(name="MCP Service")

ping_service = PingService()
weather_service = WeatherService()


@mcp.tool()
def ping() -> str:
    """Simple test tool to verify server stays running."""
    return ping_service.ping()


@mcp.tool()
def get_weather(city: str) -> dict[str, Any]:
    """Fetch current weather for a given city."""
    try:
        return weather_service.fetch_weather(city)
    except (HTTPError, RequestException) as e:
        logger.error("Failed to fetch weather for city '%s': %s", city, e)
        raise


# Run the server
if __name__ == "__main__":
    mcp.run()
