from fastapi import APIRouter

from app.schemas.improvement_schema import (
    ImprovementRequest,
    ImprovementResponse,
)
from app.services.improvement_service import ImprovementService


router = APIRouter(
    prefix="/api/improvement",
    tags=["Resume Improvement"],
)


@router.post(
    "/analyze",
    response_model=ImprovementResponse,
)
def analyze_resume(request: ImprovementRequest):
    """
    Analyze resume strengths, weaknesses, and suggestions.
    """

    data = {
        "skills": request.skills,
        "education": request.education,
        "experience": request.experience,
    }

    return ImprovementService.analyze(data)