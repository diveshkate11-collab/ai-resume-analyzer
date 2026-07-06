from app.ai_engine.parser.skills_parser import SkillsParser


class KeywordMatcher:
    """
    Matches resume skills with the skills database.
    """

    @staticmethod
    def match(text: str) -> dict:
        """
        Finds matching skills in the resume.

        Args:
            text (str): Resume text.

        Returns:
            dict: Matched skills and count.
        """

        matched_skills = SkillsParser.extract_skills(text)

        return {
            "matched_skills": matched_skills,
            "count": len(matched_skills),
        }