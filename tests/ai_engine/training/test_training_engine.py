from app.ai_engine.training.training_engine import TrainingEngine


def test_training_engine_backend():
    result = TrainingEngine.generate(
        "Backend Developer",
        [
            "Python",
            "FastAPI",
        ],
    )

    assert result["role"] == "Backend Developer"
    assert "Python" in result["current_skills"]
    assert "Docker" in result["missing_skills"]
    assert len(result["recommended_courses"]) == 3
    assert len(result["learning_plan"]) == 3
    assert result["progress"]["progress"] == 0.0


def test_training_engine_complete_skills():
    result = TrainingEngine.generate(
        "Backend Developer",
        [
            "Python",
            "FastAPI",
            "SQL",
            "Docker",
            "Git",
        ],
    )

    assert result["missing_skills"] == []
    assert result["recommended_courses"] == []
    assert result["learning_plan"] == []
    assert result["progress"]["progress"] == 0.0


def test_training_engine_unknown_role():
    result = TrainingEngine.generate(
        "DevOps Engineer",
        [
            "Docker",
        ],
    )

    assert result["role"] == "DevOps Engineer"
    assert result["current_skills"] == []
    assert result["missing_skills"] == []