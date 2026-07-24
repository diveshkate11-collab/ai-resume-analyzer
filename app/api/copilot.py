from fastapi import APIRouter

from app.schemas.copilot_schema import (
    ResumeRequest,
    JobMatchRequest,
    CoverLetterRequest,
    ExplanationRequest,
)
from app.services.copilot_service import CopilotService

router = APIRouter(
    prefix="/copilot",
    tags=["AI Copilot"],
)


@router.post("/improve")
def improve_resume(request: ResumeRequest):
    return CopilotService.improve_resume(
        request.resume
    )


@router.post("/rewrite")
def rewrite_resume(request: ResumeRequest):
    return CopilotService.rewrite_resume(
        request.resume
    )


@router.post("/job-match")
def job_match(request: JobMatchRequest):
    return CopilotService.match_job(
        request.resume,
        request.job_description,
    )


@router.post("/career-advice")
def career_advice(request: ResumeRequest):
    return CopilotService.career_advice(
        request.resume
    )


@router.post("/cover-letter")
def cover_letter(request: CoverLetterRequest):
    return CopilotService.generate_cover_letter(
        request.resume,
        request.company,
        request.role,
    )


@router.post("/explain")
def explain(request: ExplanationRequest):
    return CopilotService.explain(
        request.content
    )