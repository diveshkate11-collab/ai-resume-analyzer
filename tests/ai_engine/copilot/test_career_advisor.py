from app.ai_engine.copilot.career_advisor import CareerAdvisor
from app.ai_engine.copilot.llm_client import MockLLMClient


def test_career_advisor():
    advisor = CareerAdvisor(client=MockLLMClient())

    result = advisor.advise(
        "Python FastAPI SQL"
    )

    assert result["success"] is True
    assert result["feature"] == "career_advisor"
    assert "Return ONLY valid JSON" in result["prompt"]
    assert "Mock AI Response" in result["response"]