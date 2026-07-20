class StrengthAnalyzer:
    """
    Analyze resume strengths.
    """

    @staticmethod
    def analyze(data: dict) -> list[str]:
        """
        Analyze strengths from parsed resume.

        Args:
            data (dict): Parsed resume.

        Returns:
            list[str]
        """

        strengths = []

        skills = data.get("skills", [])
        education = data.get("education", {})
        experience = data.get("experience", {})

        if "Python" in skills:
            strengths.append("Strong Python skills.")

        if "FastAPI" in skills:
            strengths.append("Backend development skills identified.")

        if "SQL" in skills:
            strengths.append("Database knowledge identified.")

        if education.get("degree"):
            strengths.append("Education details are present.")

        if experience.get("experience"):
            strengths.append("Experience section is available.")

        if len(skills) >= 5:
            strengths.append("Good technical skill coverage.")

        if not strengths:
            strengths.append("Resume contains basic information.")

        return strengths