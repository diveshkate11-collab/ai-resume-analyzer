from app.ai_engine.jobs.role_predictor import RolePredictor
from app.ai_engine.jobs.job_matcher import JobMatcher
from app.ai_engine.jobs.skill_gap import SkillGapAnalyzer
from app.ai_engine.jobs.recommendation import RecommendationEngine


class JobService:
    """
    Service layer for job recommendation.
    """

    @staticmethod
    def recommend(resume_data: dict) -> dict:
        role = RolePredictor.predict(resume_data)
        skill_gap = SkillGapAnalyzer.analyze(resume_data, role)
        recommendations = RecommendationEngine.generate(role)

        return {
            "recommended_role": role,
            "skill_gap": skill_gap,
            "recommendations": recommendations,
            "matched_jobs": JobMatcher.match(role),
        }