from app.ai_engine.analytics.analytics_engine import AnalyticsEngine


class AnalyticsService:
    """
    Service layer for analytics operations.
    """

    @staticmethod
    def generate(history: list[int]) -> dict:
        """
        Generate analytics report from ATS score history.
        """
        return AnalyticsEngine.generate(history)