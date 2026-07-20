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

        role_result = RolePredictor.predict(resume_data)

        predicted_role = (
            role_result["roles"][0]
            if role_result.get("roles")
            else "Software Developer"
        )

        skill_gap = SkillGapAnalyzer.analyze(
            resume_data,
            predicted_role,
        )

        recommendations = RecommendationEngine.generate(
            predicted_role,
        )

        return {
            "recommended_role": predicted_role,
            "skill_gap": skill_gap,
            "recommendations": recommendations,
            "matched_jobs": JobMatcher.match(
                predicted_role,
            ),
        }