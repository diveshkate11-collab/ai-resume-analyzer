from pathlib import Path

from app.ai_engine.parser.resume_parser import ResumeParser


def test_resume_parser():
    resume_path = Path("tests/uploads/sample_resume.pdf")

    result = ResumeParser.extract(str(resume_path))

    assert isinstance(result, dict)

    assert "contact" in result
    assert "education" in result
    assert "experience" in result
    assert "skills" in result
    assert "ats" in result
    assert "recommendation" in result
    assert "improvement" in result
    assert "analytics" in result
    assert "explainability" in result
    assert "text" in result
    assert "metadata" in result

    assert isinstance(result["skills"], list)
    assert isinstance(result["ats"], dict)
    assert isinstance(result["recommendation"], dict)
    assert isinstance(result["improvement"], dict)
    assert isinstance(result["analytics"], dict)
    assert isinstance(result["explainability"], dict)
    assert isinstance(result["metadata"], dict)

    assert result["metadata"]["characters"] > 0