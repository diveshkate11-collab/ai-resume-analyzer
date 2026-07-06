import os

from app.ai_engine.parser.pdf_parser import PDFParser
from app.ai_engine.parser.docx_parser import DOCXParser
from app.ai_engine.parser.text_cleaner import TextCleaner
from app.ai_engine.parser.contact_parser import ContactParser
from app.ai_engine.parser.education_parser import EducationParser
from app.ai_engine.parser.experience_parser import ExperienceParser
from app.ai_engine.parser.skills_parser import SkillsParser

from app.ai_engine.ats.ats_score import ATSScorer


class ResumeParser:
    """
    Main Resume Parser.
    """

    @staticmethod
    def extract(file_path: str) -> dict:
        """
        Extracts complete resume information.

        Args:
            file_path (str): Resume file path.

        Returns:
            dict: Parsed resume information.
        """

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            result = PDFParser.extract_text(file_path)

        elif extension == ".docx":
            result = DOCXParser.extract_text(file_path)

        else:
            raise ValueError("Unsupported file format.")

        text = TextCleaner.clean(result["text"])

        ats = ATSScorer.calculate(text)

        return {
            "contact": ContactParser.extract_contact(text),
            "education": EducationParser.extract_education(text),
            "experience": ExperienceParser.extract_experience(text),
            "skills": SkillsParser.extract_skills(text),
            "ats": ats,
            "text": text,
            "metadata": {
                "pages": result.get("pages"),
                "paragraphs": result.get("paragraphs"),
                "characters": result["characters"],
            },
        }