class Feedback:
    """
    Generates interview feedback based on answer evaluation.
    """

    @staticmethod
    def generate(score: int) -> str:
        """
        Generate feedback using the interview score.
        """
        if score >= 90:
            return "Excellent answer. Keep up the good work."

        if score >= 60:
            return "Good answer, but there is room for improvement."

        if score > 0:
            return "Your answer needs improvement. Try to explain your thoughts in more detail."

        return "No answer was provided."