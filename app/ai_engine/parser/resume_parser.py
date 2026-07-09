import os

from app.ai_engine.parser.pdf_parser import PDFParser
from app.ai_engine.parser.docx_parser import DOCXParser
from app.ai_engine.parser.text_cleaner import TextCleaner
from app.ai_engine.parser.contact_parser import ContactParser
from app.ai_engine.parser.education_parser import EducationParser
from app.ai_engine.parser.experience_parser import ExperienceParser
from app.ai_engine.parser.skills_parser import SkillsParser

from app.ai_engine.ats.ats_score import ATSScorer

from app.ai_engine.jobs.role_predictor import RolePredictor
from app.ai_engine.jobs.recommendation import Recommendation
from app.ai_engine.jobs.skill_gap import SkillGap

from app.ai_engine.analytics.ats_history import ATSHistory

from app.ai_engine.explainability.ats_explanation import ATSExplanation
from app.ai_engine.explainability.job_reason import JobReason
from app.ai_engine.explainability.skill_reason import SkillReason


class ResumeParser:
    """
    Main Resume Parser.
    """

    @staticmethod
    def extract(file_path: str) -> dict:

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            result = PDFParser.extract_text(file_path)

        elif extension == ".docx":
            result = DOCXParser.extract_text(file_path)

        else:
            raise ValueError("Unsupported file format.")

        text = TextCleaner.clean(result["text"])

        contact = ContactParser.extract_contact(text)
        education = EducationParser.extract_education(text)
        experience = ExperienceParser.extract_experience(text)
        skills = SkillsParser.extract_skills(text)

        ats = ATSScorer.calculate(text)

        roles = RolePredictor.predict(skills)

        recommendation = Recommendation.generate(
            ats["ats_score"],
            roles,
        )

        analytics = {
            "ats_history": ATSHistory.save([], ats["ats_score"])
        }

        skill_gap = SkillGap.analyze(
            skills,
            "Backend Developer",
        )

        explainability = {
            "ats": ATSExplanation.explain(ats),

            "jobs": JobReason.explain(
                roles,
                skills,
            ),

            "skills": SkillReason.explain(
                skill_gap["matched"],
                skill_gap["missing"],
            ),
        }

        return {
            "contact": contact,
            "education": education,
            "experience": experience,
            "skills": skills,
            "ats": ats,
            "recommendation": recommendation,
            "analytics": analytics,
            "explainability": explainability,
            "text": text,
            "metadata": {
                "pages": result.get("pages"),
                "paragraphs": result.get("paragraphs"),
                "characters": result["characters"],
            },
        }