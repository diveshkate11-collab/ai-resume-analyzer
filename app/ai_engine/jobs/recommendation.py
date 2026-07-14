class RecommendationEngine:
    """
    Generate recommendations for the predicted job role.
    """

    @staticmethod
    def generate(role: str) -> list[str]:
        recommendations = {
            "Backend Developer": [
                "Build REST APIs using FastAPI.",
                "Learn Docker and containerization.",
                "Practice SQL optimization."
            ],
            "Python Developer": [
                "Strengthen Python fundamentals.",
                "Practice object-oriented programming.",
                "Build real-world Python projects."
            ],
            "AI/ML Engineer": [
                "Learn deep learning with PyTorch.",
                "Build machine learning projects.",
                "Study model deployment."
            ],
            "Data Analyst": [
                "Improve SQL skills.",
                "Learn Power BI.",
                "Practice data visualization."
            ],
            "Software Developer": [
                "Improve DSA skills.",
                "Build full-stack projects.",
                "Contribute to open source."
            ]
        }

        return recommendations.get(
            role,
            ["Continue improving your technical skills."]
        )