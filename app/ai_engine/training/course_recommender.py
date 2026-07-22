class CourseRecommender:
    """
    Recommend learning resources for missing skills.
    """

    COURSE_LIBRARY = {
        "Python": "Python for Everybody - Coursera",
        "FastAPI": "FastAPI Official Documentation",
        "SQL": "SQLBolt",
        "Git": "Learn Git Branching",
        "Docker": "Docker Official Getting Started",
        "Machine Learning": "Machine Learning Specialization - Coursera",
        "Deep Learning": "Deep Learning Specialization - Coursera",
        "TensorFlow": "TensorFlow Official Tutorials",
        "PyTorch": "PyTorch Official Tutorials",
        "Pandas": "Pandas User Guide",
        "NumPy": "NumPy Documentation",
        "Java": "Java Programming Masterclass",
        "Spring": "Spring Framework Documentation",
    }

    @classmethod
    def recommend(cls, missing_skills: list[str]) -> list[dict]:
        """
        Recommend courses for missing skills.
        """

        recommendations = []

        for skill in missing_skills:
            recommendations.append(
                {
                    "skill": skill,
                    "course": cls.COURSE_LIBRARY.get(
                        skill,
                        "No course available.",
                    ),
                }
            )

        return recommendations