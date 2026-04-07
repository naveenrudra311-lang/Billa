from .database import init_db
from .resume_routes import router as resume_router
from .ai_routes import router as ai_routerr
app = FastAPI()

app.include_router(resume_router)
app.include_router(ai_router)

@app.get("/")
def home():
    return {"message": "Interview AI Copilot running"}