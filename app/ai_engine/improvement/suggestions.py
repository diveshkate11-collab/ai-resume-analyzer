class SuggestionGenerator:
    """
    Generate resume improvement suggestions.
    """

    @staticmethod
    def generate(data: dict) -> list[str]:
        """
        Generate improvement suggestions.

        Args:
            data (dict): Parsed resume.

        Returns:
            list[str]
        """

        suggestions = []

        skills = data.get("skills", [])
        experience = data.get("experience", {})

        if "SQL" not in skills:
            suggestions.append(
                "Learn SQL and add it to your resume."
            )

        if "Docker" not in skills:
            suggestions.append(
                "Learn Docker for backend deployment."
            )

        if "Git" not in skills:
            suggestions.append(
                "Add Git and GitHub experience."
            )

        if "FastAPI" not in skills:
            suggestions.append(
                "Build REST APIs using FastAPI."
            )

        if not experience.get("experience"):
            suggestions.append(
                "Include internships, projects, or freelance experience."
            )

        suggestions.append(
            "Quantify achievements using numbers wherever possible."
        )

        suggestions.append(
            "Keep the resume limited to one page if you are a fresher."
        )

        return suggestions