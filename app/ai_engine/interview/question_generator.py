from app.ai_engine.interview.technical_questions import TECHNICAL_QUESTIONS
from app.ai_engine.interview.hr_questions import HR_QUESTIONS


ROLE_ALIASES = {
    "python": "python developer",
    "python dev": "python developer",
    "python developer": "python developer",

    "java": "java developer",
    "java dev": "java developer",
    "java developer": "java developer",

    "backend": "backend developer",
    "backend dev": "backend developer",
    "backend developer": "backend developer",

    "data science": "data scientist",
    "data scientist": "data scientist",

    "ai": "ai engineer",
    "ai engineer": "ai engineer",
    "ml engineer": "ai engineer",
    "machine learning engineer": "ai engineer",
}


class QuestionGenerator:

    @staticmethod
    def generate(role: str) -> dict:
        """
        Generate interview questions based on the job role.
        """

        original_role = role

        role = role.strip().lower()

        role = ROLE_ALIASES.get(role, role)

        technical_questions = TECHNICAL_QUESTIONS.get(
            role,
            [
                "No technical questions available for this role yet."
            ],
        )

        return {
            "role": original_role,
            "technical_questions": technical_questions,
            "hr_questions": HR_QUESTIONS,
        }