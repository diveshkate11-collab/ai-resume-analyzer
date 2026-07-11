from app.ai_engine.interview.question_generator import QuestionGenerator


class InterviewService:
    """
    Service layer for interview-related operations.
    """

    @staticmethod
    def generate_questions(role: str) -> dict:
        """
        Generate interview questions for a given job role.

        Args:
            role (str): Target job role.

        Returns:
            dict: Technical and HR interview questions.
        """

        return QuestionGenerator.generate(role)