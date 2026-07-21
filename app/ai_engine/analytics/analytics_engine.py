from app.ai_engine.analytics.ats_history import ATSHistory
from app.ai_engine.analytics.improvement_tracker import ImprovementTracker


class AnalyticsEngine:
    """
    Generates analytics from ATS score history.
    """

    @staticmethod
    def generate(history: list[int]) -> dict:
        return {
            "history": history,
            "latest_score": ATSHistory.latest(history),
            "tracking": ImprovementTracker.track(history),
        }