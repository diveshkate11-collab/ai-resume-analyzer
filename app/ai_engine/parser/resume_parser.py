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

from app.ai_engine.analytics.resume_compare import ResumeCompare
from app.ai_engine.analytics.improvement_tracker import ImprovementTracker
from app.ai_engine.analytics.ats_history import ATSHistory


class ResumeParser:
    """
    Main Resume Parser.
    """

    @staticmethod
    def extract(file_path: str) -> dict:
        """
        Extracts complete resume information.
        """

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

        return {
            "contact": contact,
            "education": education,
            "experience": experience,
            "skills": skills,
            "ats": ats,
            "recommendation": recommendation,
            "analytics": analytics,
            "text": text,
            "metadata": {
                "pages": result.get("pages"),
                "paragraphs": result.get("paragraphs"),
                "characters": result["characters"],
            },
        }