from app.ai_engine.copilot.explanation_engine import ExplanationEngine


def test_explanation_engine():
    engine = ExplanationEngine()

    result = engine.explain(
        "ATS Score: 85"
    )

    assert result["success"] is True
    assert result["feature"] == "explanation_engine"
    assert "Explain the following content" in result["prompt"]
    assert "Mock AI Response" in result["response"]