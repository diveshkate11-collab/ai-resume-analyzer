class FormattingChecker:
    """
    Checks basic resume formatting.
    """

    @staticmethod
    def check(text: str) -> dict:
        """
        Checks resume formatting.

        Args:
            text (str): Resume text.

        Returns:
            dict
        """

        result = {
            "empty": False,
            "too_short": False,
            "blank_lines": 0,
        }

        if not text.strip():
            result["empty"] = True

        if len(text) < 200:
            result["too_short"] = True

        result["blank_lines"] = text.count("\n\n")

        return result