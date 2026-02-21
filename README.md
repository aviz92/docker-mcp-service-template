# 🧱 Docker MCP Service Template

A ready-to-use template for building and deploying MCP (Model Context Protocol) services with Docker and Claude Desktop integration.

---

## 🚀 Features

- **Dockerized** — fully containerized, ready to build and run anywhere
- **Claude Desktop ready** — pre-configured JSON integration out of the box
- **MCP-compatible** — structured for seamless integration with MCP-compatible tools
- **Extensible** — add your own tools, resources, and prompts with minimal boilerplate

---

## Connecting to Claude Desktop

1. Clone this repository and build the Docker image:
```bash
   docker build -t my-mcp-service .
```

2. Add the following configuration to your Claude Desktop setup:
```json
   {
     "mcpServers": {
       "my-mcp-service": {
         "command": "docker",
         "args": [
           "run", "--rm",
           "-e", "ENV_VAR=<value>",
           "-i", "my-mcp-service"
         ]
       }
     }
   }
```

---

## 🤝 Contributing

Fork the repo, create a new branch, and submit a pull request. Contributions that promote clean and maintainable development are welcome.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
