from pydantic import BaseModel


class ResumeRequest(BaseModel):
    resume: str


class JobMatchRequest(BaseModel):
    resume: str
    job_description: str


class CoverLetterRequest(BaseModel):
    resume: str
    company: str
    role: str


class ExplanationRequest(BaseModel):
    content: str