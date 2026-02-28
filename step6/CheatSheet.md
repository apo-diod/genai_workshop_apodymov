# Step 6: Model Parameters & Architectures

Under the hood, LLMs are just probability engines predicting the next piece of text. To get the best results, you need to understand how to tune the valves and structure your agents.

## 1. Tokens and Context

**Tokens**

LLMs don't read words or characters; they read **tokens**. It's just a piece of a string. One token is roughly 3/4 of an English word (or one syllable). 
*   *Analogy:* The word `Hamburger` might be split into three tokens: `[Ham]`, `[bur]`, `[ger]`. When you pay an API provider, you are paying per token.

**Context**

LLMs are completely stateless. They have no memory. To have a "conversation," the framework (like OpenWebUI or ADK) sends the *entire chat history* to the model on every single request. 
*   The **Context Window** (e.g., 128k tokens) is the maximum array size of tokens the model can process in a single request. If your chat history exceeds this, the framework must truncate or summarize older messages.

## 2. The Probability Engine

When an LLM generates text, it assigns a probability score to every single token in its vocabulary.

**Top K**

Before picking a token, the model looks at the sorted array of probabilities. **Top K** means *"Only keep the top K most likely tokens, and disregard the rest."*
*   This prevents the model from ever hallucinating completely absurd words.

**Temperature**

After slicing the array via Top K, **Temperature** controls the remaining probabilities.
*   `Temperature = 0.0`: Acts like `max()`. It *always* picks the #1 most probable next token. It is deterministic.
*   `Temperature = 0.8`: Introduces randomness, allowing the model to occasionally pick the 2nd or 3rd most likely token.

## 3. Penalties

Penalties stop the model from looping or sounding robotic.
*   **Frequency Penalty:** It mathematically penalizes tokens based on *how many times* they've already appeared in the output.
*   **Presence Penalty:** A flat penalty applied if a token has appeared at all.

## 4. Agentic Mode & Native Function Calling

**Native Function Calling**

In the past, you had to write massive prompts for LLM to *"ALWAYS output valid JSON with keys X and Y. NEVER OUTPUT ANYTHING ELSE PLEASE I BEG YOU, YOU WILL DIE IF YOU'RE NOT GOING TO OUTPUT A JSON"* (This is actually what I was writing before discovering native function calling, I'm not kidding...)

Modern models are fine-tuned to natively support functions. You pass a JSON Schema of your Python function to the API. If the model decides it needs that tool, it will natively halt text generation and output a perfectly formatted JSON payload matching your schema.

**Agentic Mode**

This is the loop around the LLM. When the LLM outputs a tool-call JSON payload, the framework (ADK/OpenWebUI) intercepts it, executes the local Python function, and feeds the result back to the LLM so it can summarize the answer for the user.

## 5. Reasoning Models

Models like DeepSeek R1 or OpenAI's o1/o3 have **Chain of Thought (CoT)** baked in. They "think" in a hidden manner before they output the final answer.
*   **How to tweak them:** DO NOT over-prompt them. Do not include phrases like *"Let's think step by step."* Give them the raw problem, the constraints, and get out of their way. 
*   *Note:* Always leave Temperature at `1.0` for reasoning models, as their internal logic relies on the default probability distribution.

## 6. AgentTools vs Subagents (Multi-Agent Architecture)

In frameworks like Google ADK, you can build multi-agent systems. It's crucial to understand how context (memory) is handled between them.

*   **AgentTools (Stateless):** 
    You wrap a secondary LLM as a Tool. The main agent treats it like a dumb function. It passes specific arguments to the AgentTool, waits for a string response, and continues. The AgentTool **does not** see the user's full chat history. 
    *   *Use case:* A specific data-processing or data-retrieving task.
*   **Subagents (Context Preservation):** 
    This is a full handoff. The main agent routes the **entire conversation history** to the Subagent. The Subagent takes over the chat and has full awareness of everything the user has said previously.
    *   *Use case:* A `TriageAgent` chatting with a user to figure out their problem, which then hands the entire chat state over to a specialized `DatabaseExpertAgent` to write the SQL.