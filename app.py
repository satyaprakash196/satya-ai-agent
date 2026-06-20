# app.py
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests

# .env load karo
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def homepage():
    return FileResponse("index.html")

@app.post("/chat")
async def chat(req: ChatRequest):

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3.1-8b-instruct",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are Satya AI Agent. "
                            "Answer in Hindi and English when helpful. "
                            "Be friendly and professional."
                        )
                    },
                    {
                        "role": "user",
                        "content": req.message
                    }
                ]
            },
            timeout=60
        )

        data = response.json()

        if "choices" in data:
            return {
                "reply": data["choices"][0]["message"]["content"]
            }

        return {
            "reply": f"API Error: {data}"
        }

    except Exception as e:
        return {
            "reply": f"Server Error: {str(e)}"
        }

