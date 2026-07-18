from app.ai_engine.explainability.ats_explanation import ATSExplanation


def test_complete_ats_result():
    ats = {
        "ats_score": 85,
        "section": {
            "education": True,
            "skills": True,
            "experience": True,
            "projects": True,
        },
        "keywords": {
            "count": 4,
        },
    }

    result = ATSExplanation.explain(ats)

    assert isinstance(result, dict)
    assert "explanation" in result
    assert isinstance(result["explanation"], list)


def test_low_ats_score():
    ats = {
        "ats_score": 45,
        "section": {
            "education": True,
            "skills": False,
            "experience": False,
            "projects": False,
        },
        "keywords": {
            "count": 1,
        },
    }

    result = ATSExplanation.explain(ats)

    assert isinstance(result, dict)
    assert "explanation" in result
    assert isinstance(result["explanation"], list)


def test_empty_ats():
    ats = {
        "ats_score": 0,
        "section": {
            "education": False,
            "skills": False,
            "experience": False,
            "projects": False,
        },
        "keywords": {
            "count": 0,
        },
    }

    result = ATSExplanation.explain(ats)

    assert isinstance(result, dict)
    assert "explanation" in result
    assert isinstance(result["explanation"], list)


def test_zero_score():
    ats = {
        "ats_score": 0,
        "section": {
            "education": False,
            "skills": False,
            "experience": False,
            "projects": False,
        },
        "keywords": {
            "count": 0,
        },
    }

    result = ATSExplanation.explain(ats)

    assert isinstance(result, dict)
    assert "explanation" in result
    assert isinstance(result["explanation"], list)