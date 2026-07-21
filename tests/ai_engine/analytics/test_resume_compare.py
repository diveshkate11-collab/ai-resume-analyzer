from app.ai_engine.analytics.resume_compare import ResumeCompare


def test_resume_improved():
    result = ResumeCompare.compare(70, 85)

    assert result["difference"] == 15
    assert result["status"] == "Improved"


def test_resume_declined():
    result = ResumeCompare.compare(90, 80)

    assert result["difference"] == -10
    assert result["status"] == "Declined"


def test_resume_unchanged():
    result = ResumeCompare.compare(75, 75)

    assert result["difference"] == 0
    assert result["status"] == "Unchanged"