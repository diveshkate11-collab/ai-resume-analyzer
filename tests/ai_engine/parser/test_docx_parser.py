from pathlib import Path

from app.ai_engine.parser.docx_parser import DOCXParser


def test_docx_parser():
    docx_path = Path("uploads/resumes/sample_resume.docx")

    result = DOCXParser.extract_text(str(docx_path))

    assert isinstance(result, dict)
    assert "text" in result
    assert "paragraphs" in result
    assert "characters" in result

    assert result["paragraphs"] > 0
    assert result["characters"] > 0
    assert len(result["text"]) > 0