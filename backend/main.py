from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .resume_routes import router as resume_router
from .ai_routes import router as ai_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router)
app.include_router(ai_router)

@app.get("/")
def home():
    return {"message": "Interview AI Copilot running"}
