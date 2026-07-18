from app.ai_engine.ats.grammar_checker import GrammarChecker


def test_simple_resume():
    resume_text = """
    John Doe

    Python
    FastAPI
    """

    result = GrammarChecker.check(resume_text)

    assert isinstance(result, dict)


def test_resume_with_sentences():
    resume_text = """
    John Doe

    I am a Python Developer.
    I have experience in FastAPI.
    """

    result = GrammarChecker.check(resume_text)

    assert isinstance(result, dict)


def test_empty_resume():
    result = GrammarChecker.check("")

    assert isinstance(result, dict)


def test_resume_with_special_characters():
    resume_text = """
    Python!!!
    FastAPI???
    SQL@@@
    """

    result = GrammarChecker.check(resume_text)

    assert isinstance(result, dict)