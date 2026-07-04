import re


class EducationParser:
    """
    Extracts education information from resume text.
    """

    DEGREES = [
        "Bachelor of Technology",
        "Bachelor of Engineering",
        "B.Tech",
        "B.E",
        "BSc",
        "MSc",
        "M.Tech",
        "MBA",
        "PhD",
        "Diploma",
        "HSC",
        "SSC",
    ]

    @staticmethod
    def extract_education(text: str) -> dict:
        """
        Extracts degree information from resume text.

        Args:
            text (str): Resume text.

        Returns:
            dict: Education information.
        """

        result = {
            "degree": None,
        }

        for degree in EducationParser.DEGREES:
            pattern = re.escape(degree)

            if re.search(pattern, text, re.IGNORECASE):
                result["degree"] = degree
                break

        return result