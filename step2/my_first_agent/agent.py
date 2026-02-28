from google.adk.agents.llm_agent import Agent
from .subagents.my_first_subagent import server_status_agent
from google.adk.models.lite_llm import LiteLlm

OLLAMA_API_BASE="http://localhost:11434"

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen3:4b"),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    sub_agents=[server_status_agent]
)
