from fastapi import FastAPI, UploadFile, File
import shutil
import os

from backend.services.resume_parser import extract_text
from backend.services.ai_analyzer import analyze_resume

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Career Copilot AI Running"}


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text(file_path)

    analysis = analyze_resume(resume_text)

    return {
        "filename": file.filename,
        "text": resume_text,
        "analysis": analysis
    }