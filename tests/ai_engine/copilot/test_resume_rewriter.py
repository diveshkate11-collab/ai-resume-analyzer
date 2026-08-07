from app.ai_engine.copilot.resume_rewriter import ResumeRewriter
from app.ai_engine.copilot.llm_client import MockLLMClient


def test_resume_rewriter():
    rewriter = ResumeRewriter(client=MockLLMClient())

    result = rewriter.rewrite(
        "Python FastAPI SQL"
    )

    assert result["success"] is True
    assert result["feature"] == "resume_rewriter"
    assert "Rewrite" in result["prompt"]
    assert "Mock AI Response" in result["response"]


def test_resume_rewriter_empty_resume():
    rewriter = ResumeRewriter(client=MockLLMClient())

    result = rewriter.rewrite("")

    assert result["success"] is False
    assert result["feature"] == "resume_rewriter"
    assert result["error"] == "Resume cannot be empty."