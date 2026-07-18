from app.ai_engine.ats.ats_score import ATSScorer


def test_complete_resume():
    resume_text = """
    John Doe

    Education

    B.Tech in Computer Science

    Skills

    Python
    SQL
    FastAPI
    Docker

    Projects

    AI Resume Copilot

    Experience

    Fresher
    """

    result = ATSScorer.calculate(resume_text)

    assert isinstance(result, dict)
    assert "ats_score" in result
    assert "section" in result
    assert "keywords" in result
    assert "formatting" in result
    assert "grammar" in result


def test_resume_without_projects():
    resume_text = """
    John Doe

    Education

    Skills

    Python
    SQL

    Experience

    Fresher
    """

    result = ATSScorer.calculate(resume_text)

    assert isinstance(result, dict)
    assert "ats_score" in result


def test_resume_with_only_skills():
    resume_text = """
    Python
    SQL
    FastAPI
    """

    result = ATSScorer.calculate(resume_text)

    assert isinstance(result, dict)


def test_empty_resume():
    result = ATSScorer.calculate("")

    assert isinstance(result, dict)