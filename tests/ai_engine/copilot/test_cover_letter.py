from app.ai_engine.copilot.cover_letter import CoverLetterGenerator


def test_cover_letter():
    generator = CoverLetterGenerator()

    result = generator.generate(
        "Python FastAPI SQL",
        "Google",
        "Software Engineer",
    )

    assert result["success"] is True
    assert result["feature"] == "cover_letter"
    assert "Google" in result["prompt"]
    assert "Mock AI Response" in result["response"]