from pydantic import BaseModel


class AnswerEvaluationRequest(BaseModel):
    question: str
    answer: str


class AnswerEvaluationResponse(BaseModel):
    score: int
    strengths: list[str]
    weaknesses: list[str]
    improvements: list[str]