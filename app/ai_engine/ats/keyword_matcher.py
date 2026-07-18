from app.ai_engine.parser.skills_parser import SkillsParser


class KeywordMatcher:
    """
    Matches resume skills with the skills database.
    """

    # Master skills database
    SKILLS_DATABASE = [
        "Python",
        "SQL",
        "FastAPI",
        "Docker",
        "Git",
        "Linux",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "AWS",
        "Azure",
        "Kubernetes",
    ]

    @staticmethod
    def match(text: str) -> dict:
        """
        Finds matching and missing skills from the resume.

        Args:
            text (str): Resume text.

        Returns:
            dict: Matched skills, missing skills, count,
                  and match percentage.
        """

        matched_skills = SkillsParser.extract_skills(text)

        matched_skills = sorted(set(matched_skills))

        missing_skills = sorted(
            list(
                set(KeywordMatcher.SKILLS_DATABASE)
                - set(matched_skills)
            )
        )

        match_percentage = round(
            (
                len(matched_skills)
                / len(KeywordMatcher.SKILLS_DATABASE)
            )
            * 100,
            2,
        )

        return {
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "count": len(matched_skills),
            "match_percentage": match_percentage,
        }