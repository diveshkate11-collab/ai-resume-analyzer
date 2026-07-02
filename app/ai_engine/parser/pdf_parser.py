import fitz


class PDFParser:
    """
    Extracts text from PDF files.
    """

    @staticmethod
    def extract_text(file_path: str) -> dict:
        """
        Reads a PDF file and extracts its text.

        Args:
            file_path (str): Path to the PDF file.

        Returns:
            dict: Extracted text with metadata.
        """

        try:
            document = fitz.open(file_path)

            extracted_text = ""

            for page in document:
                extracted_text += page.get_text()

            result = {
                "pages": len(document),
                "characters": len(extracted_text),
                "text": extracted_text,
            }

            document.close()

            return result

        except Exception as e:
            raise Exception(f"Error reading PDF: {e}")