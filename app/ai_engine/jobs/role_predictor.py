class RolePredictor:
    """
    Predicts suitable job roles based on extracted skills.
    """

    ROLE_SKILLS = {
        "Backend Developer": [
            "python",
            "fastapi",
            "sql",
            "docker",
            "git",
        ],
        "Python Developer": [
            "python",
            "flask",
            "django",
        ],
        "AI/ML Engineer": [
            "python",
            "machine learning",
            "tensorflow",
            "pytorch",
            "scikit-learn",
        ],
        "Data Analyst": [
            "python",
            "sql",
            "pandas",
            "power bi",
            "excel",
        ],
    }

    @staticmethod
    def predict(resume_data: dict) -> dict:
        """
        Predicts suitable job roles.

        Args:
            resume_data (dict): Resume information.

        Returns:
            dict: Predicted roles.
        """

        skills = {
            skill.lower()
            for skill in resume_data.get("skills", [])
        }

        predicted_roles = []

        for role, required_skills in RolePredictor.ROLE_SKILLS.items():
            if skills.intersection(required_skills):
                predicted_roles.append(role)

        if not predicted_roles:
            predicted_roles.append("Software Developer")

        return {
            "roles": predicted_roles,
            "count": len(predicted_roles),
        }