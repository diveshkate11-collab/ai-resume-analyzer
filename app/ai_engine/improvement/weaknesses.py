class WeaknessAnalyzer:
    """
    Analyze resume weaknesses.
    """

    @staticmethod
    def analyze(data: dict) -> list[str]:
        """
        Analyze weaknesses from parsed resume.

        Args:
            data (dict): Parsed resume.

        Returns:
            list[str]
        """

        weaknesses = []

        skills = data.get("skills", [])
        experience = data.get("experience", {})

        if "SQL" not in skills:
            weaknesses.append("SQL skill is missing.")

        if "Docker" not in skills:
            weaknesses.append("Docker skill is missing.")

        if "Git" not in skills:
            weaknesses.append("Git skill is missing.")

        if "FastAPI" not in skills:
            weaknesses.append("FastAPI skill is missing.")

        if not experience.get("experience"):
            weaknesses.append("Experience section is missing.")

        return weaknesses