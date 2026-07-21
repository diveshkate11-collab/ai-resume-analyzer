class InterviewRoadmap:
    """
    Generates a learning roadmap based on interview performance.
    """

    @staticmethod
    def generate(score: int) -> list[str]:
        """
        Generate a learning roadmap.
        """
        if score >= 90:
            return [
                "Practice advanced interview questions.",
                "Solve coding challenges regularly.",
                "Participate in mock interviews.",
            ]

        if score >= 60:
            return [
                "Strengthen core programming concepts.",
                "Practice technical interview questions.",
                "Review common HR interview questions.",
            ]

        return [
            "Learn programming fundamentals.",
            "Study data structures and algorithms.",
            "Build small projects to improve practical skills.",
        ]