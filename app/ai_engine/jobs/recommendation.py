class Recommendation:
    """
    Generates resume recommendations based on ATS score.
    """

    @staticmethod
    def generate(ats_score: int, roles: list) -> dict:
        """
        Generates recommendations.

        Args:
            ats_score (int): Resume ATS score.
            roles (list): Predicted job roles.

        Returns:
            dict
        """

        suggestions = []

        if ats_score < 60:
            suggestions.append(
                "Improve resume to increase ATS score."
            )

        elif ats_score < 80:
            suggestions.append(
                "Resume is good but can be improved."
            )

        else:
            suggestions.append(
                "Resume is ATS friendly."
            )

        if not roles:
            suggestions.append(
                "Add more technical skills to unlock more job opportunities."
            )

        return {
            "ats_score": ats_score,
            "recommended_roles": roles,
            "suggestions": suggestions,
        }