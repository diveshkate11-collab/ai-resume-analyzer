import re


class ContactParser:
    """
    Extracts contact information from resume text.
    """

    @staticmethod
    def extract_contact(text: str) -> dict:
        """
        Extracts name, email and phone number from resume text.

        Args:
            text (str): Resume text.

        Returns:
            dict: Extracted contact information.
        """

        result = {
            "name": None,
            "email": None,
            "phone": None,
        }

        lines = [line.strip() for line in text.splitlines() if line.strip()]

        if lines:
            result["name"] = lines[0]

        email = re.search(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            text,
        )

        if email:
            result["email"] = email.group()

        phone = re.search(
            r"(\+91[\s-]?)?[6-9]\d{9}",
            text,
        )

        if phone:
            result["phone"] = phone.group()

        return result