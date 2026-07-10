from fastapi import APIRouter, File, UploadFile

from app.schemas.resume_schema import ResumeResponse
from app.services.resume_service import ResumeService


router = APIRouter(
    prefix="/api/resume",
    tags=["Resume"],
)


@router.post(
    "/upload",
    response_model=ResumeResponse,
)
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload and analyze a resume.
    """
    return ResumeService.upload_and_analyze(file)