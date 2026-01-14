import requests

Ollama_API_URL = "http://localhost:11434/api/generate"
model = "llama3.2"

def call_llm(prompt):
    response = requests.post(
        Ollama_API_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.7
        }
    )
    return response.json()["response"]