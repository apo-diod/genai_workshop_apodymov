# Step 2: Google ADK (Python) & LiteLLM

The **Google Agent Development Kit (ADK)** is a framework for building AI agents. Because we want to use our local Ollama model instead of a paid Google API, we will use **LiteLLM** as a proxy to translate the API calls.

## 1. Initial Setup

First, we need to set up an isolated Python environment and install our dependencies. We'll use `uv` for lightning-fast package installation.

```bash
# 1. Create a virtual environment
python -m venv ./.venv

# 2. Activate the virtual environment
# On Windows:
./.venv/Scripts/activate
# On Mac/Linux:
source ./.venv/bin/activate

# 3. Install 'uv' (a fast pip replacement)
pip install uv

# 4. Install dependencies
uv pip install -r requirements.txt
```
(Note: The requirements.txt contains google-adk, google-adk[extensions], and litellm).

## 2. Project Structure

Normally, to generate a new ADK project from scratch, you would run:
```bash
adk create <project_name>
```
However, for the purpose of this workshop, the project files (`main.py`, `tools/`, `my_first_agent/`) are provided as-is in this repository

## 3. Core concepts
Before we run it, let's look at the three main concepts in our code:
* LiteLLM Routing: ADK expects a Google model. LiteLLM lets us just use our local Ollama installation
* Tools: Standard Python functions that the LLM can decide to execute.
* Agents vs Subagents: 
    * Agent: The main LLM brain handling the user's request
    * Subagent: A secondary LLM specialized in a specific task. The main Agent can delegate work to it

## 4. Running the agent
You have two ways to run your ADK project:
### Option A. Standard execution
```bash
python main.py
```

### Option B. Interactive UI Mode
Google ADK comes with a built-in web interface for testing your agents and seeing the tool-calling traces in real-time
```bash
adk web
```
(This will start a local server, usually on http://localhost:8080, where you can chat with your agent)