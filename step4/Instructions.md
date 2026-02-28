# Step 4: UI for Chatbots (OpenWebUI)

While terminal outputs and raw API responses are great for development, eventually, we'll want a ChatGPT-style interface. **OpenWebUI** is a user-friendly frontend for local and cloud LLMs.

## 1. What is OpenWebUI?

OpenWebUI is a self-hosted web application that provides a chat interface for LLMs.

## 2. Installation and Setup

We will install OpenWebUI directly via Python. *(Note: It can also be run via Docker, but running it via pip keeps everything in our local environment for this workshop).*

```bash
# 1. Create and activate a new virtual environment
python -m venv ./.venv
source ./.venv/bin/activate  # Mac/Linux
# .\.venv\Scripts\activate   # Windows

# 2. Install 'uv' for fast dependency resolution
pip install uv

# 3. Install OpenWebUI
uv pip install open-webui

# 4. Start the server
open-webui serve
```

*Note: The first time you run open-webui serve, it might take a little while to start up as it initializes its local database and applies migrations. Once it says "Application startup complete", open http://localhost:8080 in your browser*

## 3. Ollama Integration
Because we already have Ollama running in the background on its default port (`http://localhost:11434`), OpenWebUI will automatically detect it.

You don't need to configure any API keys or endpoints. When you open the UI, you will immediately see your local `qwen3:4b` model available in the model dropdown at the top of the screen.

## 4. OpenWebUI "Models"

In OpenWebUI, when you create a custom "Workspace Model" or "Agent", you aren't training a new AI. It's an additional brick placed on top of a base provider model (like our local Qwen or a cloud model).

It acts as a configuration wrapper that bundles together:

* A specific Base Model (e.g., qwen3:4b)
* A custom System Prompt (e.g., "You are a senior DevOps engineer...")
* Specific Tools or Knowledge bases (RAG) attached to it.

## 5. Functions, Tools, and Filters
OpenWebUI is highly extensible through Python scripts. It's important to understand the difference between these three concepts:

* Tools: Actions the LLM chooses to execute. (e.g., The LLM decides it needs to call get_server_status() to answer the user's question).
* Filters (Middleware): Code that intercepts the request or response. It runs every time.
    * Inlet Filter: Modifies the user's prompt before the LLM sees it.
    * Outlet Filter: Modifies the LLM's response before the user sees it.
* Functions: Custom execution pipelines. Instead of just passing a message to an LLM, a Function can completely hijack the request to do custom RAG, chain multiple model calls together, or query an external API directly.

## 6. MCP Server Integration
While we built an MCP Server in Step 3, connecting it directly to OpenWebUI is out of scope of this specific workshop.

However, OpenWebUI has support for FastMCP. If you want to connect the FastMCP server we built to OpenWebUI later, you can find great documentation and the official integration tool in the `mcpo` repository:
https://github.com/open-webui/mcpo
