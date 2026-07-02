import re

from app.ai_engine.parser.pdf_parser import PDFParser
from app.ai_engine.parser.docx_parser import DOCXParser
from app.ai_engine.parser.text_cleaner import TextCleaner


class ResumeParser:
    """
    Parses resume files and extracts basic information.
    """

    @staticmethod
    def parse(file_path: str) -> dict:
        """
        Parse a resume and extract basic information.
        """

        # Determine parser
        if file_path.lower().endswith(".pdf"):
            result = PDFParser.extract_text(file_path)

        elif file_path.lower().endswith(".docx"):
            result = DOCXParser.extract_text(file_path)

        else:
            raise ValueError("Unsupported resume format.")

        # Clean extracted text
        text = TextCleaner.clean(result["text"])

        # -----------------------------
        # Extract Name
        # -----------------------------
        lines = text.split("\n")

        name = ""

        for line in lines:
            line = line.strip()

            if line:
                name = line
                break

        # -----------------------------
        # Extract Email
        # -----------------------------
        email_match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        email = email_match.group(0) if email_match else ""

        # -----------------------------
        # Extract Phone Number
        # -----------------------------
        phone_match = re.search(
            r"(\+?\d[\d\s-]{8,}\d)",
            text,
        )

        phone = phone_match.group(0) if phone_match else ""

        return {
            "name": name,
            "email": email,
            "phone": phone,
            "text": text,
            "metadata": {
                key: value
                for key, value in result.items()
                if key != "text"
            },
        }