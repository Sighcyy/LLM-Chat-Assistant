# LLM-Chat-Assistant

# 🤖 LLM Chat Assistant

A conversational AI chat assistant built with a Gradio web interface, showcasing integration with large language models via the OpenAI-compatible API standard. Supports **Google Gemini** (cloud) and **Llama via Ollama** (local/offline).

---

## Features

- 💬 Real-time streaming chat responses
- 🌐 Clean Gradio web UI — no frontend coding required
- 🔁 Full conversation history passed on every request for context-aware replies
- 🧠 System prompt engineered for depth and conciseness
- ☁️ **Gemini** mode for cloud-based inference (fast, no local hardware needed)
- 🖥️ **Ollama** mode for fully local inference (private, offline-capable)

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| `gradio` | Web chat interface |
| `openai` Python SDK | Unified API client (works with both Gemini and Ollama) |
| `python-dotenv` | Secure API key loading from `.env` |
| Google Gemini API | Cloud LLM backend (`gemini-2.5-flash-lite`) |
| Ollama | Local LLM backend (`llama3.2`) |

Although these are main import, the lib folder has all the proper modules and packages and their related dependencies
---

### Choosing your backend

#### ☁️ Option A — Gemini (Cloud)

1. Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

3. Run the app:

```bash
python app.py
```

---

#### 🖥️ Option B — Ollama (Local)

> **Prefer to keep things local?** Use this option to run the model entirely on your own machine — no API key, no data leaving your computer.

1. Install [Ollama](https://ollama.com/download) for your OS
2. Pull the Llama model:

```bash
ollama pull llama3.2
```

3. In `app.py`, swap the chat function to use the Ollama client:

```python
# Change this line:
stream = gemini.chat.completions.create(model=MODEL_GEMINI, messages=messages, stream=True)

# To this:
stream = ollama.chat.completions.create(model=MODEL_LLAMA, messages=messages, stream=True)
```

4. Make sure Ollama is running, then start the app:

```bash
ollama serve   # if not already running
python app.py
```

The Ollama server runs locally at `http://localhost:11434` — no internet connection required after the initial model download.

---

## Project Structure

```
├── app.py          # Main application
├── .env            # API keys (never commit this)
├── .gitignore      # Should include .env
└── README.md
```

> ⚠️ **Never commit your `.env` file.** Add it to `.gitignore` to keep your API key safe.

```gitignore
.env
```

---

## How It Works

The app uses the OpenAI Python SDK pointed at different base URLs depending on the backend:

- **Gemini** → `https://generativelanguage.googleapis.com/v1beta/openai/`
- **Ollama** → `http://localhost:11434/v1`

This works because both APIs are OpenAI-compatible, meaning the same client code can talk to either backend with just a URL and model name change — a clean demonstration of the portability of the OpenAI API standard.

On each message, the full conversation history is included in the request so the model maintains context throughout the session. Responses are streamed token-by-token for a smooth, real-time feel.

---

## Demo

Once running, Gradio will print a local URL in your terminal:

```
Running on local URL: http://127.0.0.1:7860
```

Open it in your browser to start chatting.
