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
---
## Installation

### 1. Clone the repo
```bash
git clone https://github.com/your-username/LLM-Chat-Assistant.git
cd LLM-Chat-Assistant
```

### 2. Install dependencies
```bash
pip install openai gradio python-dotenv requests ipython
```

> 💡 **Tip:** It's recommended to use a virtual environment:
> ```bash
> python -m venv venv
> source venv/bin/activate      # macOS/Linux
> venv\Scripts\activate         # Windows
> pip install openai gradio python-dotenv requests ipython
> ```

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
