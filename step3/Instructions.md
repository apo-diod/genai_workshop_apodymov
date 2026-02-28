# Step 3: MCP Server (Model Context Protocol)

Up until now, we gave our LLM tools by writing native Python functions directly in our code. But what happens when we want to use those exact same tools in a different framework, a visual chatbot UI, or Claude Desktop? 

## 1. What is it and Why do we need it?

**What is it?**
MCP (Model Context Protocol) is an open standard created by Anthropic. It standardizes how AI models connect to external data sources and tools.

**Why not just use Python functions?**
If you write a `get_server_status()` function in Google ADK, it is locked inside that specific Python project. 
By wrapping that function in an **MCP Server**, you decouple the tool from the LLM. The MCP server hosts your tools as a standardized API, meaning **any** MCP-compatible client (Google ADK, OpenWebUI, Cursor, Claude) can connect to it and use your tools.

## 2. FastMCP Server Setup

We will use `fastmcp`, a framework that makes building MCP servers in Python easy.

```bash
# 1. Create and activate a new virtual environment
python -m venv ./.venv
source ./.venv/bin/activate  # Mac/Linux
# .\.venv\Scripts\activate   # Windows

# 2. Install 'uv' and 'fastmcp'
pip install uv
uv pip install fastmcp
```

## 3. Running the MCP Server
In the provided repository, you have a file named `my_mcp_server.py` (which contains our Server Status Checker tool wrapped in `@mcp.tool`).
Run the server:
```bash
python my_mcp_server.py
```
This will host an HTTP MCP server accessible at: `http://localhost:9000/mcp`

## 4. Testing with MCP Inspector
Before connecting an LLM to our server, we want to test that the tools actually work. Anthropic provides an official web-based inspector.

*(Note: You must have Node.js installed on your system to run this).*

Open a new terminal window and run:

```bash
npx @modelcontextprotocol/inspector
```
This will open a local web page where you can see a list of exposed tools and manually execute them with test payloads, completely independent of an LLM

## 5. Integrating into Google ADK

Integrating an external MCP server into Google ADK is incredibly simple. Instead of passing a local Python function to your agent, you configure an MCP connection.

For this workshop, the integration is already written for you in the provided files. You can find it located here:
`my_first_agent/subagents/my_first_subagent.py`

