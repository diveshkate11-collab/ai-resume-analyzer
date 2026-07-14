class StrengthAnalyzer:
    """
    Analyze resume strengths.
    """

    @staticmethod
    def analyze(data: dict) -> list[str]:
        strengths = []

        skills = data.get("skills", [])

        if "Python" in skills:
            strengths.append("Strong Python skills.")

        if "FastAPI" in skills:
            strengths.append("Backend development skills identified.")

        if data.get("education"):
            strengths.append("Education details are present.")

        if data.get("experience"):
            strengths.append("Experience section is available.")

        if not strengths:
            strengths.append("Resume contains basic information.")

        return strengths