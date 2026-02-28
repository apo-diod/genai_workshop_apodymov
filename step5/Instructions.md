# Step 5: Powerful Models & OpenRouter

Local models are great for basic tasks. However, for complex coding or deep reasoning, you need frontier models (Claude 4.6 Sonnet, GPT-5, GLM-5, etc.). 

Instead of dealing with 10+ different API keys and SDKs and paying for their services, we'll use **OpenRouter**.

## 1. What is OpenRouter?

OpenRouter is a **Unified API Gateway** for LLMs. 
It aggregates almost every AI model in existence (OpenAI, Anthropic, Google, Meta, DeepSeek, etc.) behind a single, standardized, OpenAI-compatible REST API. You fund one account, use one API key, and can switch between hundreds of models just by changing a string in your code.

## 2. What is Modality?

When browsing models, you'll often see the term **Modality** (or Multimodal). This refers to the types of data a model can understand and generate:
*   **Text-to-Text:** Standard LLMs (input text, output text).
*   **Vision (Image-to-Text):** Models that can "see" images and describe or analyze them (e.g., GPT-4o, Claude 3.5).
*   **Audio / Video:** Models that can process or generate sound and video streams natively.


## 3. Integrating OpenRouter into OpenWebUI

Since OpenRouter uses the standard OpenAI API format, plugging it into OpenWebUI takes 30 seconds:

1. Open OpenWebUI in your browser (`http://localhost:8080`).
2. Go to **Admin Panel** (bottom left) -> **Settings** -> **Connections**.
3. Under the OpenAI API section, click the `+` to add a new connection.
4. Set the **API Base URL** to: `https://openrouter.ai/api/v1`
5. Set the **API Key** to your OpenRouter key (e.g., `sk-or-v1-...`).
6. Click Save. 

*Result: When you open a new chat, you will now see cloud models right next to your local Ollama models in the dropdown.*

## 4. Integrating OpenRouter into Google ADK

Because we installed **LiteLLM** in Step 2, integrating OpenRouter into our Python code is incredibly easy. LiteLLM natively supports openrouter.

In the workshop files, I've provided a snippet called `openrouter_integrated_agent.py`. It also contains a bunch of extras, give it a try!