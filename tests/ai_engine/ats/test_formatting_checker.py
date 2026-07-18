from app.ai_engine.ats.formatting_checker import FormattingChecker


def test_good_formatting():
    resume_text = """
    John Doe

    Education

    B.Tech

    Skills

    Python
    FastAPI
    Docker
    """

    result = FormattingChecker.check(resume_text)

    assert isinstance(result, dict)


def test_poor_formatting():
    resume_text = "John Doe Education Skills Python FastAPI Docker"

    result = FormattingChecker.check(resume_text)

    assert isinstance(result, dict)


def test_empty_resume():
    result = FormattingChecker.check("")

    assert isinstance(result, dict)


def test_resume_with_extra_spaces():
    resume_text = """



    John Doe



    Education




    Skills




    Python




    """

    result = FormattingChecker.check(resume_text)

    assert isinstance(result, dict)