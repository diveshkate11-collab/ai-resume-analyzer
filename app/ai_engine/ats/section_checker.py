class SectionChecker:
    """
    Checks whether important resume sections are present.
    """

    REQUIRED_SECTIONS = [
        "education",
        "skills",
        "experience",
        "projects",
    ]

    @staticmethod
    def check(text: str) -> dict:
        """
        Checks if required resume sections exist.

        Args:
            text (str): Resume text.

        Returns:
            dict: Section availability.
        """

        result = {}

        lower_text = text.lower()

        for section in SectionChecker.REQUIRED_SECTIONS:
            result[section] = section in lower_text

        return result