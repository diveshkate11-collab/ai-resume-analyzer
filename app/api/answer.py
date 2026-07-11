from fastapi import APIRouter

from app.schemas.answer_schema import (
    AnswerEvaluationRequest,
    AnswerEvaluationResponse,
)
from app.services.answer_service import AnswerService


router = APIRouter(
    prefix="/api/interview",
    tags=["Interview"],
)


@router.post(
    "/evaluate",
    response_model=AnswerEvaluationResponse,
)
def evaluate_answer(request: AnswerEvaluationRequest):
    """
    Evaluate an interview answer.
    """

    return AnswerService.evaluate(
        question=request.question,
        answer=request.answer,
    )