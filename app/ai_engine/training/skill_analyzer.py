class SkillAnalyzer:
    """
    Analyze current and missing skills for a predicted job role.
    """

    ROLE_SKILLS = {
        "Backend Developer": [
            "Python",
            "FastAPI",
            "SQL",
            "Docker",
            "Git",
        ],
        "Python Developer": [
            "Python",
            "OOP",
            "FastAPI",
            "Git",
            "SQL",
        ],
        "AI Engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
        ],
        "Data Scientist": [
            "Python",
            "Pandas",
            "NumPy",
            "Machine Learning",
            "SQL",
        ],
        "Java Developer": [
            "Java",
            "Spring",
            "SQL",
            "Git",
            "Docker",
        ],
    }

    @classmethod
    def analyze(cls, role: str, skills: list[str]) -> dict:
        """
        Compare candidate skills with required skills for the role.
        """

        required_skills = cls.ROLE_SKILLS.get(role, [])

        current_skills = []
        missing_skills = []

        candidate_skills = {skill.lower() for skill in skills}

        for skill in required_skills:
            if skill.lower() in candidate_skills:
                current_skills.append(skill)
            else:
                missing_skills.append(skill)

        return {
            "role": role,
            "current_skills": current_skills,
            "missing_skills": missing_skills,
        }