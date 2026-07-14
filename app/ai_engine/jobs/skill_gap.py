class SkillGapAnalyzer:
    """
    Analyze missing skills for the predicted job role.
    """

    ROLE_SKILLS = {
        "Backend Developer": ["Python", "FastAPI", "SQL", "Docker", "Git"],
        "Python Developer": ["Python", "OOP", "Git"],
        "AI/ML Engineer": ["Python", "Machine Learning", "NumPy", "Pandas"],
        "Data Analyst": ["SQL", "Excel", "Python", "Power BI"],
        "Software Developer": ["Git", "Problem Solving"],
    }

    @staticmethod
    def analyze(resume_data: dict, role: str) -> list[str]:
        resume_skills = {
            skill.lower() for skill in resume_data.get("skills", [])
        }

        required_skills = SkillGapAnalyzer.ROLE_SKILLS.get(role, [])

        missing_skills = [
            skill
            for skill in required_skills
            if skill.lower() not in resume_skills
        ]

        return missing_skills