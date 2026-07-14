class WeaknessAnalyzer:
    """
    Analyze resume weaknesses.
    """

    @staticmethod
    def analyze(data: dict) -> list[str]:
        weaknesses = []

        skills = data.get("skills", [])

        if "SQL" not in skills:
            weaknesses.append("SQL skill is missing.")

        if "Docker" not in skills:
            weaknesses.append("Docker skill is missing.")

        if "Git" not in skills:
            weaknesses.append("Git skill is missing.")

        if not data.get("experience"):
            weaknesses.append("Experience section is missing.")

        return weaknesses