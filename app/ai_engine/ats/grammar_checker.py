class GrammarChecker:
    """
    Checks grammar quality of the resume.
    """

    @staticmethod
    def check(text: str) -> dict:
        """
        Grammar Checker V1.

        Args:
            text (str): Resume text.

        Returns:
            dict
        """

        result = {
            "grammar_score": 100,
            "suggestions": [],
        }

        return result