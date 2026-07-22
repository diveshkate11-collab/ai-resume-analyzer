from app.ai_engine.training.skill_analyzer import SkillAnalyzer
from app.ai_engine.training.course_recommender import CourseRecommender
from app.ai_engine.training.learning_planner import LearningPlanner
from app.ai_engine.training.progress_tracker import ProgressTracker


class TrainingEngine:
    """
    Coordinate the complete training recommendation workflow.
    """

    @staticmethod
    def generate(role: str, skills: list[str]) -> dict:
        """
        Generate a complete training report.
        """

        analysis = SkillAnalyzer.analyze(role, skills)

        missing_skills = analysis["missing_skills"]

        recommended_courses = CourseRecommender.recommend(
            missing_skills
        )

        learning_plan = LearningPlanner.create(
            missing_skills
        )

        progress = ProgressTracker.track(
            completed=0,
            total=len(missing_skills),
        )

        return {
            "role": role,
            "current_skills": analysis["current_skills"],
            "missing_skills": missing_skills,
            "recommended_courses": recommended_courses,
            "learning_plan": learning_plan,
            "progress": progress,
        }