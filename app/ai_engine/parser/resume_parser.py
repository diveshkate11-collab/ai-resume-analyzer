from pathlib import Path

from app.ai_engine.ats.ats_score import ATSScorer
from app.ai_engine.parser.pdf_parser import PDFParser
from app.ai_engine.parser.docx_parser import DocxParser
from app.ai_engine.parser.text_cleaner import TextCleaner
from app.ai_engine.parser.contact_parser import ContactParser
from app.ai_engine.parser.skills_parser import SkillsParser
from app.ai_engine.parser.education_parser import EducationParser
from app.ai_engine.parser.experience_parser import ExperienceParser

from app.ai_engine.jobs.role_predictor import RolePredictor
from app.ai_engine.jobs.job_matcher import JobMatcher
from app.ai_engine.jobs.skill_gap import SkillGapAnalyzer
from app.ai_engine.jobs.recommendation import RecommendationEngine


class ResumeParser:
    """
    Complete Resume Parser.
    """

    @staticmethod
    def extract(file_path: str) -> dict:
        """
        Extract structured resume information.

        Args:
            file_path (str): Resume path.

        Returns:
            dict
        """

        path = Path(file_path)

        # Read file
        if path.suffix.lower() == ".pdf":
            raw_result = PDFParser.extract_text(file_path)

        elif path.suffix.lower() == ".docx":
            raw_result = DocxParser.extract_text(file_path)

        else:
            raise ValueError("Unsupported file format.")

        # Extract only the text
        raw_text = raw_result["text"]

        # Clean text
        clean_text = TextCleaner.clean(raw_text)

        # Parse resume
        contact = ContactParser.extract_contact(clean_text)
        skills = SkillsParser.extract_skills(clean_text)
        education = EducationParser.extract_education(clean_text)
        experience = ExperienceParser.extract_experience(clean_text)
        ats = ATSScorer.calculate(clean_text)

        resume_data = {
            "contact": contact,
            "skills": skills,
            "education": education,
            "experience": experience,
        }

        # Predict role
        role_result = RolePredictor.predict(resume_data)

        predicted_role = (
            role_result["roles"][0]
            if role_result.get("roles")
            else "Software Developer"
        )

        return {
            "contact": contact,
            "education": education,
            "experience": experience,
            "skills": skills,

            "ats": ats,

            "recommendation": {
               "role": predicted_role,
               "recommendations": RecommendationEngine.generate(predicted_role),
            },

            "analytics": {},

            "explainability": {},

            "text": clean_text,

            "metadata": {
                "characters": len(clean_text)
                }
}