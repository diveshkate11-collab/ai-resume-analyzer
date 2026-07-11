from fastapi import APIRouter

from app.schemas.interview_schema import (
    InterviewRequest,
    InterviewResponse,
)
from app.services.interview_service import InterviewService


router = APIRouter(
    prefix="/api/interview",
    tags=["Interview"],
)


@router.post(
    "/questions",
    response_model=InterviewResponse,
)
def generate_questions(request: InterviewRequest):
    """
    Generate interview questions for a job role.
    """

    return InterviewService.generate_questions(request.role)