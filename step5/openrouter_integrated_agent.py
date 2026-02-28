from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
import litellm
import os
from .config import LITELLM_PROXY_API_BASE, LITELLM_PROXY_API_KEY

power_capabilities = {
    'FREE/LITE': 'google/gemma-3n-e4b-it:free',
    'FREE/LITE+': 'z-ai/glm-4.5-air:free',
    'FREE/MEDIUM+': 'stepfun/step-3.5-flash:free',
    'LITE': 'mistralai/mistral-nemo', # Dirt-cheap, almost no agentic capabilities
    'LITE+': 'qwen/qwen3-coder-next', # Opensource, cheap, agentic capabilities over short context
    'MEDIUM': 'minimax/minimax-m2.1', # Moderate price, agentic and reasoning capabilities over short context
    'MEDIUM+': 'z-ai/glm-5', # Moderate price, agentic and reasoning capabilities over good context
    'POWER': 'anthropic/claude-haiku-4.5', # High price. Great agentic and reasoning capabilities over long context. USE ONLY FOR HIGH-END TESTING
    'POWER+': 'anthropic/claude-opus-4.6'
}

with open('core_prompt.md', 'r') as f:
    core_prompt = f.read()

os.environ['LITELLM_PROXY_API_KEY'] = LITELLM_PROXY_API_KEY
os.environ['LITELLM_PROXY_API_BASE'] = LITELLM_PROXY_API_BASE
litellm.use_litellm_proxy = True

root_agent = Agent(
    model=LiteLlm(model=power_capabilities['MEDIUM+']),
    name='coordinator',
    description="Coordinator agent",
    instruction=core_prompt,
)
