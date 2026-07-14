class RolePredictor:
    """
    Predict the most suitable job role.
    """

    @staticmethod
    def predict(resume_data: dict) -> str:
        skills = [skill.lower() for skill in resume_data.get("skills", [])]

        if "fastapi" in skills:
            return "Backend Developer"

        if "python" in skills:
            return "Python Developer"

        if "machine learning" in skills:
            return "AI/ML Engineer"

        if "sql" in skills:
            return "Data Analyst"

        return "Software Developer"