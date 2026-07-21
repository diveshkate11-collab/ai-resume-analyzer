from app.ai_engine.interview.question_generator import QuestionGenerator
from app.ai_engine.interview.answer_evaluator import AnswerEvaluator
from app.ai_engine.interview.feedback import Feedback


class InterviewAnalyzer:
    """
    Coordinates interview question generation,
    answer evaluation, and feedback generation.
    """

    @staticmethod
    def analyze(role: str, answer: str) -> dict:
        """
        Generate interview analysis.
        """
        questions = QuestionGenerator.generate(role)

        evaluation = AnswerEvaluator.evaluate(answer)

        feedback = Feedback.generate(evaluation["score"])

        return {
            "role": questions["role"],
            "technical_questions": questions["technical_questions"],
            "hr_questions": questions["hr_questions"],
            "evaluation": evaluation,
            "feedback": feedback,
        }