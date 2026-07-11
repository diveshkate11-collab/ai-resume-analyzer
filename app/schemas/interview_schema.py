from pydantic import BaseModel


class InterviewRequest(BaseModel):
    role: str


class InterviewResponse(BaseModel):
    role: str
    technical_questions: list[str]
    hr_questions: list[str]