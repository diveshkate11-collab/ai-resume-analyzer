class LearningPlanner:
    """
    Generate a simple week-by-week learning plan.
    """

    @staticmethod
    def create(missing_skills: list[str]) -> list[str]:
        """
        Create a learning roadmap based on missing skills.
        """

        learning_plan = []

        for week, skill in enumerate(missing_skills, start=1):
            learning_plan.append(
                f"Week {week}: Learn {skill}"
            )

        return learning_plan