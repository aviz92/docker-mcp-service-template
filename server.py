from custom_python_logger import build_logger
from dotenv import load_dotenv
from mcp.server import FastMCP

from service_example.ping_service import ServiceExample

load_dotenv()

logger = build_logger(project_name="MCP Service")

# Create an MCP server
mcp = FastMCP(name="MCP Service")

service_example = ServiceExample()


@mcp.tool()
def ping() -> str:
    """Simple test tool to verify server stays running."""
    return service_example.ping()


# Run the server
if __name__ == "__main__":
    mcp.run()
