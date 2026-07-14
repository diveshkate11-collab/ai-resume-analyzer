from fastapi import FastAPI

from app.api.jobs import router as jobs_router
from app.api.improvement import router as improvement_router
from app.api.answer import router as answer_router
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
app.include_router(answer_router)
app.include_router(improvement_router)
app.include_router(jobs_router)


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