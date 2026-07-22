from app.ai_engine.training.training_engine import TrainingEngine


class TrainingService:
    """
    Service layer for training recommendations.
    """

    @staticmethod
    def recommend(role: str, skills: list[str]) -> dict:
        """
        Generate a personalized training report.
        """
        return TrainingEngine.generate(role, skills)