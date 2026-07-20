from app.ai_engine.improvement.weaknesses import WeaknessAnalyzer


def test_weaknesses():
    data = {
        "skills": [
            "Python",
        ],
        "education": {},
        "experience": {},
    }

    result = WeaknessAnalyzer.analyze(data)

    assert isinstance(result, list)

    assert "SQL skill is missing." in result
    assert "Docker skill is missing." in result
    assert "Git skill is missing." in result
    assert "FastAPI skill is missing." in result
    assert "Experience section is missing." in result