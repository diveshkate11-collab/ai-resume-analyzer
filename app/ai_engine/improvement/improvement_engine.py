from app.ai_engine.improvement.strengths import StrengthAnalyzer
from app.ai_engine.improvement.weaknesses import WeaknessAnalyzer
from app.ai_engine.improvement.suggestions import SuggestionGenerator


class ImprovementEngine:
    """
    Resume Improvement Engine.
    """

    @staticmethod
    def analyze(data: dict) -> dict:
        """
        Analyze the resume and generate improvement insights.

        Args:
            data (dict): Parsed resume data.

        Returns:
            dict
        """

        return {
            "strengths": StrengthAnalyzer.analyze(data),
            "weaknesses": WeaknessAnalyzer.analyze(data),
            "suggestions": SuggestionGenerator.generate(data),
        }