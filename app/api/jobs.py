from fastapi import APIRouter

from app.schemas.job_schema import (
    JobRecommendationRequest,
    JobRecommendationResponse,
)
from app.services.job_service import JobService


router = APIRouter(
    prefix="/api/jobs",
    tags=["Job Recommendation"],
)


@router.post(
    "/recommend",
    response_model=JobRecommendationResponse,
)
def recommend_jobs(request: JobRecommendationRequest):
    """
    Recommend job roles based on resume information.
    """

    resume_data = {
        "skills": request.skills,
        "education": request.education,
        "experience": request.experience,
    }

    return JobService.recommend(resume_data)