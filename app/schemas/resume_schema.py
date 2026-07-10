from typing import Any

from pydantic import BaseModel


class ContactSchema(BaseModel):
    name: str | None
    email: str | None
    phone: str | None


class EducationSchema(BaseModel):
    degree: str | None


class ExperienceSchema(BaseModel):
    experience: str | None


class RecommendationSchema(BaseModel):
    ats_score: int
    recommended_roles: list[str]
    suggestions: list[str]


class ResumeAnalysisSchema(BaseModel):
    contact: ContactSchema
    education: EducationSchema
    experience: ExperienceSchema
    skills: list[str]
    ats: dict[str, Any]
    recommendation: RecommendationSchema
    analytics: dict[str, Any]
    explainability: dict[str, Any]
    text: str
    metadata: dict[str, Any]


class ResumeResponse(BaseModel):
    success: bool
    filename: str
    message: str
    analysis: ResumeAnalysisSchema