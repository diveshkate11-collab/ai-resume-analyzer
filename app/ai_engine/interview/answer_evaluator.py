class AnswerEvaluator:
    """
    Basic rule-based interview answer evaluator.
    """

    @staticmethod
    def evaluate(answer: str) -> dict:
        """
        Evaluate an interview answer based on its content length.
        """
        answer = answer.strip()

        if not answer:
            return {
                "score": 0,
                "result": "No Answer",
            }

        word_count = len(answer.split())

        if word_count < 10:
            return {
                "score": 50,
                "result": "Needs Improvement",
            }

        return {
            "score": 100,
            "result": "Good Answer",
        }