class JobMatcher:
    """
    Match jobs based on the predicted role.
    """

    JOBS = {
        "Backend Developer": [
            "Backend Developer Intern",
            "Junior Backend Developer",
            "Python Backend Developer"
        ],
        "Python Developer": [
            "Python Developer",
            "Junior Python Developer",
            "Python Software Engineer"
        ],
        "AI/ML Engineer": [
            "Machine Learning Engineer",
            "AI Engineer",
            "Data Science Intern"
        ],
        "Data Analyst": [
            "Data Analyst",
            "Business Analyst",
            "Junior Data Analyst"
        ],
        "Software Developer": [
            "Software Developer",
            "Associate Software Engineer",
            "Graduate Software Engineer"
        ]
    }

    @staticmethod
    def match(role: str) -> list[str]:
        return JobMatcher.JOBS.get(
            role,
            ["Software Engineer"]
        )