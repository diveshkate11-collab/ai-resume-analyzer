from pydantic import BaseModel


class JobRecommendationRequest(BaseModel):
    skills: list[str]
    education: bool = False
    experience: bool = False


class JobRecommendationResponse(BaseModel):
    recommended_role: str
    skill_gap: list[str]
    recommendations: list[str]
    matched_jobs: list[str]