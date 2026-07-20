from app.ai_engine.improvement.strengths import StrengthAnalyzer


def test_strengths():
    data = {
        "skills": [
            "Python",
            "FastAPI",
            "SQL",
            "Docker",
            "Git",
        ],
        "education": {
            "degree": "B.Tech",
        },
        "experience": {
            "experience": "Fresher",
        },
    }

    result = StrengthAnalyzer.analyze(data)

    assert isinstance(result, list)
    assert len(result) > 0
    assert "Strong Python skills." in result