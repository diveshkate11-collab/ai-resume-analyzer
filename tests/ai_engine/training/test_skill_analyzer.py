from app.ai_engine.training.skill_analyzer import SkillAnalyzer


def test_skill_analyzer_backend():
    result = SkillAnalyzer.analyze(
        "Backend Developer",
        [
            "Python",
            "FastAPI",
        ],
    )

    assert result["role"] == "Backend Developer"
    assert "Python" in result["current_skills"]
    assert "FastAPI" in result["current_skills"]
    assert "SQL" in result["missing_skills"]
    assert "Docker" in result["missing_skills"]
    assert "Git" in result["missing_skills"]


def test_skill_analyzer_ai_engineer():
    result = SkillAnalyzer.analyze(
        "AI Engineer",
        [
            "Python",
            "Machine Learning",
        ],
    )

    assert result["role"] == "AI Engineer"
    assert "Python" in result["current_skills"]
    assert "Machine Learning" in result["current_skills"]
    assert "Deep Learning" in result["missing_skills"]
    assert "TensorFlow" in result["missing_skills"]
    assert "PyTorch" in result["missing_skills"]


def test_skill_analyzer_unknown_role():
    result = SkillAnalyzer.analyze(
        "DevOps Engineer",
        [
            "Docker",
        ],
    )

    assert result["role"] == "DevOps Engineer"
    assert result["current_skills"] == []
    assert result["missing_skills"] == []