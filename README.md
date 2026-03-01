![Python](https://img.shields.io/badge/python->=3.11-blue)
![Development Status](https://img.shields.io/badge/status-stable-green)
![Maintenance](https://img.shields.io/maintenance/yes/2026)
![License](https://img.shields.io/badge/license-MIT-blue)

---

# Docker MCP Service Template

A production-ready template for building [Model Context Protocol (MCP)](https://modelcontextprotocol.io) services in Python, containerized with Docker. Clone this repo, add your services, and connect them to Claude Desktop or any MCP-compatible client in minutes.

---

## 📦 Installation

```bash
git clone https://github.com/aviz92/docker-mcp-service-template.git
cd docker-mcp-service-template
uv sync
```

---

## 🚀 Features

- ✅ **FastMCP Server** — lightweight MCP server using the official `mcp[cli]` SDK
- ✅ **Docker-ready** — single `Dockerfile` for building and shipping your service
- ✅ **Service layer pattern** — clean separation between MCP tool definitions and business logic
- ✅ **Structured logging** — `custom-python-logger` integrated out of the box, no `print()` in production
- ✅ **Environment config** — `python-dotenv` for safe, local `.env`-based configuration
- ✅ **Extensible** — add new MCP tools by dropping a service class into `mcp_services/` and registering it in `server.py`

---

## ⚙️ Configuration

Create a `.env` file in the project root:

```env
WEATHER_API_KEY=your_openweathermap_api_key
```

> Get a free API key at [openweathermap.org](https://openweathermap.org/api)

---

## 🛠️ How to Use

1. **Add a service** — create a new class in `mcp_services/` (e.g. `mcp_services/my_service.py`)
2. **Register the tool** — import the service in `server.py` and decorate a function with `@mcp.tool()`
3. **Build the image** — run `docker build -t my-mcp-service .`
4. **Connect to Claude Desktop** — add the JSON config shown below to your Claude Desktop settings

---

## 🚀 Quick Start

```bash
# Build the Docker image
docker build -t docker-mcp-service .

# Run locally (outside Docker) for development
uv run server.py
```

---

## ▶️ Usage Examples

### Example 1: Ping tool — verify the server is alive

```python
# Registered in server.py
@mcp.tool()
def ping() -> str:
    """Simple test tool to verify server stays running."""
    return ping_service.ping()
```

Claude will call this tool and receive: `"pong"`

---

### Example 2: Weather tool — fetch live weather data

```python
@mcp.tool()
def get_weather(city: str) -> dict[str, Any]:
    """Fetch current weather for a given city."""
    return weather_service.fetch_weather(city)
```

Claude will call `get_weather(city="Tel Aviv")` and receive:

```json
{
  "city": "Tel Aviv",
  "temperature": 24.3,
  "description": "clear sky",
  "humidity": 58,
  "wind_speed": 4.1
}
```

---

### Example 3: Connecting to Claude Desktop

Add the following to your Claude Desktop MCP server config:

```json
{
  "mcpServers": {
    "docker-mcp-service": {
      "command": "docker",
      "args": [
        "run", "--rm",
        "-e", "WEATHER_API_KEY=<your_api_key>",
        "-i", "docker-mcp-service"
      ]
    }
  }
}
```

---

## 🤝 Contributing

If you have a helpful pattern or improvement to suggest:
1. Fork the repo
2. Create a new branch
3. Submit a pull request

Contributions that promote clean, maintainable, and production-ready MCP services are welcome.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Thanks

Thanks for exploring this repository!
Happy coding!
