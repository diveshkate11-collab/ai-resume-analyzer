class RolePredictor:
    """
    Predicts suitable job roles based on resume skills.
    """

    ROLE_SKILLS = {
        "Python Developer": [
            "Python",
            "SQL",
            "Git",
            "FastAPI",
            "Flask",
            "Django",
        ],

        "Backend Developer": [
            "Python",
            "SQL",
            "FastAPI",
            "Docker",
            "Git",
        ],

        "AI/ML Engineer": [
            "Python",
            "Machine Learning",
            "NumPy",
            "Pandas",
            "Scikit-learn",
            "TensorFlow",
            "PyTorch",
        ],

        "Data Scientist": [
            "Python",
            "Machine Learning",
            "Pandas",
            "NumPy",
            "SQL",
            "Matplotlib",
        ],
    }

    @staticmethod
    def predict(skills: list) -> list:
        """
        Predicts job roles from extracted skills.

        Args:
            skills (list): Resume skills.

        Returns:
            list: Recommended job roles.
        """

        recommended_roles = []

        for role, required_skills in RolePredictor.ROLE_SKILLS.items():

            matched = len(set(skills).intersection(required_skills))

            if matched >= 2:
                recommended_roles.append(role)

        return recommended_roles