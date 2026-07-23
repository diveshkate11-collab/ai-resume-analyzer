from app.ai_engine.copilot.prompt_manager import PromptManager


def test_resume_improver_prompt():
    prompt = PromptManager.resume_improver("Python Resume")

    assert "Strengths" in prompt
    assert "Weaknesses" in prompt
    assert "Python Resume" in prompt


def test_resume_rewriter_prompt():
    prompt = PromptManager.resume_rewriter("Resume")

    assert "Rewrite" in prompt
    assert "Resume" in prompt


def test_job_match_prompt():
    prompt = PromptManager.job_match(
        "Resume",
        "Backend Developer",
    )

    assert "Resume" in prompt
    assert "Job Description" in prompt


def test_cover_letter_prompt():
    prompt = PromptManager.cover_letter(
        "Resume",
        "Google",
        "Software Engineer",
    )

    assert "Google" in prompt
    assert "Software Engineer" in prompt


def test_career_advice_prompt():
    prompt = PromptManager.career_advice("Resume")

    assert "Career path" in prompt