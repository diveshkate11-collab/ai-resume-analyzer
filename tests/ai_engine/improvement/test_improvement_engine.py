from app.ai_engine.improvement.improvement_engine import ImprovementEngine


def test_improvement_engine():
    data = {
        "skills": ["Python"],
        "education": {
            "degree": "B.Tech",
        },
        "experience": {},
    }

    result = ImprovementEngine.analyze(data)

    assert isinstance(result, dict)

    assert "strengths" in result
    assert "weaknesses" in result
    assert "suggestions" in result

    assert isinstance(result["strengths"], list)
    assert isinstance(result["weaknesses"], list)
    assert isinstance(result["suggestions"], list)

    assert len(result["strengths"]) > 0
    assert len(result["weaknesses"]) > 0
    assert len(result["suggestions"]) > 0