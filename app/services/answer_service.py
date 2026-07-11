class AnswerService:
    """
    Service for evaluating interview answers.
    """

    @staticmethod
    def evaluate(question: str, answer: str) -> dict:
        answer = answer.strip()

        if len(answer) < 30:
            score = 3
            strengths = ["Answer provided."]
            weaknesses = ["Answer is too short."]
            improvements = [
                "Explain the concept in more detail.",
                "Add an example.",
                "Mention real-world applications."
            ]

        elif len(answer) < 100:
            score = 6
            strengths = [
                "Basic explanation provided."
            ]
            weaknesses = [
                "Lacks depth."
            ]
            improvements = [
                "Add technical details.",
                "Include examples.",
                "Explain why it is important."
            ]

        else:
            score = 9
            strengths = [
                "Detailed explanation.",
                "Good coverage of the topic."
            ]
            weaknesses = [
                "Minor improvements possible."
            ]
            improvements = [
                "Use more technical terminology.",
                "Add practical experience if applicable."
            ]

        return {
            "score": score,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "improvements": improvements,
        }