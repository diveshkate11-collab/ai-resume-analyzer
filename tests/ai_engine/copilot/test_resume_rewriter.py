from app.ai_engine.copilot.resume_rewriter import ResumeRewriter


def test_resume_rewriter():
    rewriter = ResumeRewriter()

    result = rewriter.rewrite(
        "Python FastAPI SQL"
    )

    assert result["success"] is True
    assert result["feature"] == "resume_rewriter"
    assert "Rewrite" in result["prompt"]
    assert "Mock AI Response" in result["response"]