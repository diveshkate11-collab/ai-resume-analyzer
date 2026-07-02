import re


class TextCleaner:
    """
    Cleans extracted resume text before further processing.
    """

    @staticmethod
    def clean(text: str) -> str:
        """
        Cleans resume text.

        - Removes extra spaces
        - Removes multiple blank lines
        - Removes tabs
        - Normalizes line endings
        """

        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove multiple spaces
        text = re.sub(r"[ ]{2,}", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove leading/trailing spaces
        text = text.strip()

        return text