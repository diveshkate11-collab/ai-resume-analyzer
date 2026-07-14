from app.ai_engine.improvement.improvement_engine import ImprovementEngine


class ImprovementService:
    """
    Service layer for resume improvement analysis.
    """

    @staticmethod
    def analyze(data: dict) -> dict:
        return ImprovementEngine.analyze(data)