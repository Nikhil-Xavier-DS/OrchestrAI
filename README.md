# 🧠 OrchestrAI: Multi-Agent LLM System with MCP + LangGraph + Local LLM

A production-grade **AI Operating System** built with:

* 🧠 Local LLMs
* 🤖 Multi-agent orchestration using LangGraph
* 🔌 50+ integrations via Model Context Protocol (MCP)
* ⚙️ Async execution + retry + observability
* 🧩 Modular, config-driven architecture

---

## 🚀 Overview

This project transforms LLMs from simple chat interfaces into a **fully autonomous system** that can:

* Plan tasks dynamically
* Route work across specialized agents
* Execute actions via real-world tools
* Integrate with your entire digital ecosystem

---

## 🏗️ Architecture

```
User Task
   ↓
🧠 Planner Agent (Brain)
   ↓
📋 Execution Plan
   ↓
🤖 Specialized Agents
   ├── Comms Agent (Gmail, Slack, etc.)
   ├── Data Agent (Postgres, Snowflake, etc.)
   ├── Dev Agent (GitHub, AWS, etc.)
   └── Research Agent (Tavily, Web)
   ↓
🔌 MCP Tools Layer (50+ integrations)
   ↓
🧠 Memory + Observability
```

---

## ⚙️ Features

### 🧠 Intelligence Layer

* LLM-powered planning
* Dynamic task decomposition
* Tool selection via reasoning

### 🤖 Multi-Agent System

* Role-based agents (comms, data, dev, research)
* Extensible agent architecture

### 🔌 MCP Integration Layer

* Plug-and-play integrations
* Supports 50+ tools (Gmail, Slack, GitHub, etc.)
* No code changes required for new tools

### ⚡ Production Capabilities

* Fully async execution
* Retry logic (tenacity)
* Structured logging (loguru)
* Config-driven activation

---

## 🧰 Tech Stack

* Python 3.10+
* LangGraph
* Ollama (local LLM)
* HTTPX (async calls)
* Tenacity (retries)
* Loguru (logging)
* YAML (config)

---

## 🧠 LLM Setup (Ollama)

### Install Ollama

https://ollama.com

### Pull model

```
ollama pull llama3
```

### Run server

```
ollama serve
```

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ai-os.git
cd ai-os

pip install -r requirements.txt
```

---

## ⚙️ Configuration

### Enable tools

Edit:

```
config/tools.yaml
```

```yaml
enabled_tools:
  - gmail
  - slack
  - github
  - tavily

mcp_endpoints:
  gmail: "http://localhost:8001"
  slack: "http://localhost:8002"
```

---

## 🔌 MCP Servers

This project assumes MCP servers are running for each integration.

Examples:

* Gmail MCP
* Slack MCP
* GitHub MCP
* Tavily MCP

Each tool is accessed via HTTP endpoints.

---

## ▶️ Run the System

```bash
python main.py
```

Example task:

```
"Check emails and analyze sales data"
```

---

## 🧩 Adding New Tools

1. Start MCP server
2. Add endpoint to `tools.yaml`

```yaml
notion: "http://localhost:8010"
```

Done. No code changes required.

---

## 🤖 Adding New Agents

Create a new agent in:

```
agents/
```

Extend:

```python
class NewAgent(BaseAgent):
    async def run(self, state):
        ...
```

Register in orchestrator.

---

## 📊 Observability

Logs stored in:

```
logs/app.log
```

Supports:

* Debug tracing
* Tool execution tracking
* Error monitoring

---

## ⚠️ Limitations

* Local LLMs may struggle with structured outputs
* Requires MCP servers for full functionality
* Not all 50 integrations are active by default

---

## 🚀 Roadmap

* [ ] Dockerized MCP ecosystem
* [ ] UI dashboard
* [ ] Autonomous scheduling (cron agents)
* [ ] Memory persistence (vector DB)
* [ ] Self-improving agents

---

## 💡 Philosophy

This is not a chatbot.

This is an:

> **AI Operating System**

---

## 🧠 Author

Built for advanced AI workflows, agent systems, and real-world automation.

---

## 📜 License

Apache License
