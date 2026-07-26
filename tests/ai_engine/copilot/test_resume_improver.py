from app.ai_engine.copilot.resume_improver import ResumeImprover
from app.ai_engine.copilot.llm_client import MockLLMClient


def test_resume_improver():
    improver = ResumeImprover(client=MockLLMClient())

    result = improver.improve(
        "Python FastAPI SQL"
    )

    assert result["success"] is True
    assert result["feature"] == "resume_improver"
    assert "Strengths" in result["prompt"]
    assert "Mock AI Response" in result["response"]