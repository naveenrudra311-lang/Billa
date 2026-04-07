from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.post("/generate-answer")
def generate_answer(question: str):

    prompt = f"""
You are an expert software engineer.

Explain clearly and provide coding example.

Question:
{question}
"""

    result = subprocess.run(
        ["ollama", "run", "codellama", prompt],
        capture_output=True,
        text=True
    )

    return {"answer": result.stdout}