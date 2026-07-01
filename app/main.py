from fastapi import FastAPI
from app.api.resume import router as resume_router

app = FastAPI(
    title="AI Resume Copilot",
    version="1.0.0",
    description="AI-powered Resume Analysis and Career Assistant"
)

app.include_router(resume_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Copilot",
        "status": "Running Successfully"
    }