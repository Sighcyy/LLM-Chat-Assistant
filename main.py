import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display
import gradio as gr


load_dotenv(override=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
ollama_api_key = "ollama"

MODEL_GEMINI = 'gemini-2.5-flash-lite'
MODEL_LLAMA = 'llama3.2'

ollama_url = "http://localhost:11434/v1"
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

ollama = OpenAI(api_key = ollama_api_key, base_url = ollama_url)
gemini = OpenAI(api_key = gemini_api_key, base_url = gemini_url)



system_messages = "You are an expert in the every field who will explain answer in great depth, while also being concise. You have a helpful attitude"

def chat(message, history):
    messages = [{"role": "system", "content": system_messages}]
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        messages.append({"role": "assistant", "content": h[1]})
    messages.append({"role": "user", "content": message})
    stream = gemini.chat.completions.create(model=MODEL_GEMINI, messages=messages, stream=True)
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response

gr.ChatInterface(fn=chat).launch()
