import os
import requests
from fastapi import APIRouter
from .database import db

router = APIRouter()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

@router.post("/generate-answer")
def generate_answer(question: str):
    prompt = f"""You are an expert software engineer.
Explain clearly and provide a coding example.

Question:
{question}
"""
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": "codellama", "prompt": prompt, "stream": False},
            timeout=60
        )
        answer = response.json().get("response", "No response from model.")
    except Exception as e:
        answer = f"AI service unavailable: {str(e)}"

    return {"answer": answer}
