## 🚀 MCP Server – Overview

The **Model Context Protocol (MCP) Server** is a lightweight, flexible bridge between large language models (like Claude or ChatGPT) and real-world applications or system operations. It allows AI models to perform tasks such as running terminal commands, accessing camera devices, or retrieving weather data — all through structured tool-calling interfaces.

By separating logic and execution layers, the MCP server ensures a safe and controllable way for models to interact with your machine, providing modularity, transparency, and extensibility.

---

## ⚙️ Installation Guide

This project uses **[uv](https://github.com/astral-sh/uv)** to manage the Python environment and dependencies.

### 1. Install `uv`

**MacOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Navigate to Your Project Folder

```bash
cd Project_Folder
```

### 3. Initialize the Project with `uv`

```bash
uv init
```

### 4. Add MCP as a Dependency

```bash
uv add "mcp[cli]"
```

---

## 🚧 Running Any MCP Server

Before running any MCP server file, you must activate the virtual environment:

**MacOS/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```powershell
venv\Scripts\activate
```

Then install and run the desired MCP module:

```bash
mcp install Python-Filename.py
```

Replace `Python-Filename.py` with the actual MCP file you want to run (e.g., `terminal.py`, `camera.py`, `weather.py`).

---

### ⚠️ Troubleshooting

If any MCP server does not work as expected, you may need to modify the **config file** used by the MCP server.

Open the `claude_desktop_config.json` (for claude) or the relevant configuration file and change 
```json
{
  "mcpServers": {
    "Name of the mcp server": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "Path to the mcp file"
      ]
    }
  }
}
```
to:
```json
{
  "mcpServers": {
    "Name of the mcp server": {
      "command": "mcp",
      "args": [
        "run",
        "Path to the mcp file"
      ]
    }
  }
}
```