from app.ai_engine.ats.keyword_matcher import KeywordMatcher


def test_multiple_keywords():
    resume_text = """
    Python
    FastAPI
    Docker
    SQL
    """

    result = KeywordMatcher.match(resume_text)

    assert isinstance(result, dict)
    assert "matched_skills" in result
    assert "missing_skills" in result
    assert "match_percentage" in result


def test_single_keyword():
    resume_text = """
    Python
    """

    result = KeywordMatcher.match(resume_text)

    assert isinstance(result, dict)
    assert "matched_skills" in result


def test_no_keywords():
    resume_text = """
    Cooking
    Cricket
    Singing
    """

    result = KeywordMatcher.match(resume_text)

    assert isinstance(result, dict)
    assert len(result["matched_skills"]) == 0


def test_empty_resume():
    result = KeywordMatcher.match("")

    assert isinstance(result, dict)