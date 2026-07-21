from app.ai_engine.interview.interview_analyzer import InterviewAnalyzer
from app.ai_engine.interview.roadmap import InterviewRoadmap


class InterviewService:
    """
    Service layer for interview preparation.
    """

    @staticmethod
    def analyze(role: str, answer: str) -> dict:
        """
        Generate interview analysis and learning roadmap.
        """
        report = InterviewAnalyzer.analyze(role, answer)

        report["roadmap"] = InterviewRoadmap.generate(
            report["evaluation"]["score"]
        )

        return report