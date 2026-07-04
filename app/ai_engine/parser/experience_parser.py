import re


class ExperienceParser:
    """
    Extracts experience information from resume text.
    """

    @staticmethod
    def extract_experience(text: str) -> dict:
        """
        Extracts experience level from resume text.

        Args:
            text (str): Resume text.

        Returns:
            dict: Experience information.
        """

        result = {
            "experience": None,
        }

        if re.search(r"\bfresher\b", text, re.IGNORECASE):
            result["experience"] = "Fresher"

        else:
            experience = re.search(
                r"(\d+)\+?\s*(years?|yrs?)",
                text,
                re.IGNORECASE,
            )

            if experience:
                result["experience"] = experience.group()

        return result