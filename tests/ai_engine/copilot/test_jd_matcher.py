from app.ai_engine.copilot.jd_matcher import JDMatcher


def test_jd_matcher():
    matcher = JDMatcher()

    result = matcher.match(
        "Python FastAPI SQL",
        "Backend Developer with Docker",
    )

    assert result["success"] is True
    assert result["feature"] == "jd_matcher"
    assert "Job Description" in result["prompt"]
    assert "Mock AI Response" in result["response"]