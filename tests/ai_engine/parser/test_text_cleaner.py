from app.ai_engine.parser.text_cleaner import TextCleaner


def test_remove_extra_spaces():
    text = """



John Doe


    Python        FastAPI


Machine Learning




SQL




"""

    cleaned = TextCleaner.clean(text)

    assert "John Doe" in cleaned
    assert "Python" in cleaned
    assert "FastAPI" in cleaned
    assert "Machine Learning" in cleaned
    assert "SQL" in cleaned


def test_empty_string():
    cleaned = TextCleaner.clean("")

    assert cleaned == ""


def test_single_line():
    cleaned = TextCleaner.clean("Python FastAPI")

    assert cleaned == "Python FastAPI"


def test_whitespace_only():
    cleaned = TextCleaner.clean("     \n\n\n     ")

    assert cleaned == ""