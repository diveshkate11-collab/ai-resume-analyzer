from fastapi import FastAPI

from app.api.interview import router as interview_router
from app.api.resume import router as resume_router


app = FastAPI(
    title="AI Resume Copilot",
    description="AI-powered Resume Analysis and Career Assistant",
    version="1.0.0",
)


# Register API Routes
app.include_router(resume_router)
app.include_router(interview_router)


@app.get("/", tags=["Home"])
def home():
    """
    Root endpoint.
    """

    return {
        "project": "AI Resume Copilot",
        "version": "1.0.0",
        "status": "Running Successfully",
    }