from app.ai_engine.copilot.career_advisor import CareerAdvisor
from app.ai_engine.copilot.cover_letter import CoverLetterGenerator
from app.ai_engine.copilot.explanation_engine import ExplanationEngine
from app.ai_engine.copilot.jd_matcher import JDMatcher
from app.ai_engine.copilot.resume_improver import ResumeImprover
from app.ai_engine.copilot.resume_rewriter import ResumeRewriter


class CopilotService:
    """
    Service layer for AI Copilot features.
    """

    @staticmethod
    def improve_resume(resume: str) -> dict:
        return ResumeImprover().improve(resume)

    @staticmethod
    def rewrite_resume(resume: str) -> dict:
        return ResumeRewriter().rewrite(resume)

    @staticmethod
    def match_job(
        resume: str,
        job_description: str,
    ) -> dict:
        return JDMatcher().match(
            resume,
            job_description,
        )

    @staticmethod
    def career_advice(resume: str) -> dict:
        return CareerAdvisor().advise(resume)

    @staticmethod
    def generate_cover_letter(
        resume: str,
        company: str,
        role: str,
    ) -> dict:
        return CoverLetterGenerator().generate(
            resume,
            company,
            role,
        )

    @staticmethod
    def explain(content: str) -> dict:
        return ExplanationEngine().explain(content)