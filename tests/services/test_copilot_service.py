from app.services.copilot_service import CopilotService


def test_improve_resume():
    result = CopilotService.improve_resume(
        "Python FastAPI SQL"
    )

    assert result["success"] is True
    assert result["feature"] == "resume_improver"


def test_rewrite_resume():
    result = CopilotService.rewrite_resume(
        "Python FastAPI SQL"
    )

    assert result["success"] is True
    assert result["feature"] == "resume_rewriter"


def test_job_match():
    result = CopilotService.match_job(
        "Python FastAPI SQL",
        "Backend Developer",
    )

    assert result["success"] is True
    assert result["feature"] == "jd_matcher"


def test_career_advice():
    result = CopilotService.career_advice(
        "Python FastAPI SQL"
    )

    assert result["success"] is True
    assert result["feature"] == "career_advisor"


def test_cover_letter():
    result = CopilotService.generate_cover_letter(
        "Python FastAPI SQL",
        "Google",
        "Software Engineer",
    )

    assert result["success"] is True
    assert result["feature"] == "cover_letter"


def test_explanation():
    result = CopilotService.explain(
        "ATS Score: 85"
    )

    assert result["success"] is True
    assert result["feature"] == "explanation_engine"