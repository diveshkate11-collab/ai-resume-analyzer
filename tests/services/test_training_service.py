from app.services.training_service import TrainingService


def test_training_service_backend():
    result = TrainingService.recommend(
        "Backend Developer",
        [
            "Python",
            "FastAPI",
        ],
    )

    assert result["role"] == "Backend Developer"
    assert "Docker" in result["missing_skills"]
    assert len(result["recommended_courses"]) == 3
    assert len(result["learning_plan"]) == 3
    assert result["progress"]["progress"] == 0.0


def test_training_service_complete_skills():
    result = TrainingService.recommend(
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