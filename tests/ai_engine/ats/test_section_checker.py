from app.ai_engine.ats.section_checker import SectionChecker


def test_all_sections_present():
    resume_text = """
    John Doe

    Education

    Skills

    Projects

    Experience
    """

    result = SectionChecker.check(resume_text)

    assert isinstance(result, dict)
    assert result["education"] is True
    assert result["skills"] is True
    assert result["projects"] is True
    assert result["experience"] is True


def test_missing_projects():
    resume_text = """
    John Doe

    Education

    Skills

    Experience
    """

    result = SectionChecker.check(resume_text)

    assert result["education"] is True
    assert result["skills"] is True
    assert result["experience"] is True
    assert result["projects"] is False


def test_only_education():
    resume_text = """
    Education

    Bachelor of Technology
    """

    result = SectionChecker.check(resume_text)

    assert result["education"] is True
    assert result["skills"] is False
    assert result["experience"] is False
    assert result["projects"] is False


def test_empty_resume():
    result = SectionChecker.check("")

    assert result["education"] is False
    assert result["skills"] is False
    assert result["experience"] is False
    assert result["projects"] is False