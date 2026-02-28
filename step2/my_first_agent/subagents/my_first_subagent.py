from google.adk.agents.llm_agent import Agent
from tools.utilities import get_server_status
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams

toolset = MCPToolset(
    connection_params = StreamableHTTPConnectionParams(
        url = "http://127.0.0.1:9000/mcp"
    )
)

OLLAMA_API_BASE="http://localhost:11434"

server_status_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen3:4b"),
    name='server_status_agent',
    description='A helpful assistant for server status questions.',
    instruction='You are a helper sub agents for answering questions regarding server status issues',
    tools=[get_server_status],
    # tools=[toolset], # We'll use it to demonstrate working step 3
)
