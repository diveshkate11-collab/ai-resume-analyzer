from pathlib import Path

from app.ai_engine.parser.pdf_parser import PDFParser


def test_pdf_parser():
    pdf_path = Path("tests/uploads/sample_resume.pdf")

    result = PDFParser.extract_text(str(pdf_path))

    assert isinstance(result, dict)
    assert "text" in result
    assert "pages" in result
    assert "characters" in result

    assert result["pages"] > 0
    assert result["characters"] > 0
    assert len(result["text"]) > 0