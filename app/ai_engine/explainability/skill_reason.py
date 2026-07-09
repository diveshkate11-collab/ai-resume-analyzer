class SkillReason:
    """
    Explains matched and missing skills.
    """

    @staticmethod
    def explain(matched_skills: list, missing_skills: list) -> dict:
        """
        Explains resume skill analysis.

        Args:
            matched_skills (list): Skills found in the resume.
            missing_skills (list): Skills missing for the selected role.

        Returns:
            dict
        """

        explanation = []

        if matched_skills:
            explanation.append(
                "Your resume already includes: "
                + ", ".join(matched_skills)
                + "."
            )

        if missing_skills:
            explanation.append(
                "Consider adding: "
                + ", ".join(missing_skills)
                + "."
            )

        if not missing_skills:
            explanation.append(
                "Your resume contains all required skills."
            )

        return {
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "explanation": explanation,
        }