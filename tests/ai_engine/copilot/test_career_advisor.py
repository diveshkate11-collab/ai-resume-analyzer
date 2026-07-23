from app.ai_engine.copilot.career_advisor import CareerAdvisor


def test_career_advisor():
    advisor = CareerAdvisor()

    result = advisor.advise(
        "Python FastAPI SQL"
    )

    assert result["success"] is True
    assert result["feature"] == "career_advisor"
    assert "Career path" in result["prompt"]
    assert "Mock AI Response" in result["response"]