from fastapi import APIRouter, UploadFile, File
from .database import resume_collection

router = APIRouter()

MAX_RESUMES = 100

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...), user_id: str = "default_user"):
    count = resume_collection.count_documents({"user": user_id})

    if count >= MAX_RESUMES:
        return {"error": "Maximum 100 resumes allowed"}

    content = await file.read()

    resume_collection.insert_one({
        "user": user_id,
        "filename": file.filename,
        "content": content.decode("latin1")
    })

    return {"message": "Resume uploaded successfully"}
