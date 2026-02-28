# Step 1: Local LLM Setup

The easiest way to run Large Language Models locally is using **Ollama**. It acts as a lightweight wrapper around `llama.cpp` and exposes a local API that mimics OpenAI's standard.

## 1. Install Ollama

*   **Website:** [https://ollama.com/](https://ollama.com/)
*   Download the installer for macOS or Windows directly from the site.
*   **Linux / WSL:**
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```

## 2. Choosing & Downloading a Model

When choosing a model for local development, consider:
*   **RAM/VRAM:** A general rule is you need ~1GB of RAM per 1 Billion parameters (for 4-bit quantized models).
*   **Tool Calling:** Not all models are trained to output JSON for function calling. Look for models specifically tuned for it (like Qwen, Llama 3.1, or Hermes).
*   **Reasoning:** If you need logic over raw knowledge, look for reasoning models (like DeepSeek R1).

For this workshop, we are using a lightweight Qwen model. It's fast and handles tool-calling well.

Run this command in your terminal. If the model isn't downloaded yet, Ollama will pull it automatically:

```bash
ollama run qwen3:4b
```
(Note: Once downloaded, you can type directly in the terminal to chat with it. Type /bye to exit).

## 3. Running an API call
Ollama automatically starts a background server on port 11434. You don't have to use the terminal chat; you can hit it directly via REST.

Open a new terminal and run this curl command:

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "qwen3:4b",
  "messages": [
    { "role": "user", "content": "Explain APIs to a 5 year old in one sentence." }
  ],
  "stream": false
}'
```
