from pydantic import BaseModel


class ImprovementRequest(BaseModel):
    skills: list[str]
    education: bool = False
    experience: bool = False


class ImprovementResponse(BaseModel):
    strengths: list[str]
    weaknesses: list[str]
    suggestions: list[str]