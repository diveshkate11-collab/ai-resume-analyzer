from app.ai_engine.jobs.role_predictor import RolePredictor


def test_backend_developer_prediction():
    resume_data = {
        "skills": [
            "Python",
            "FastAPI",
            "SQL",
            "Docker",
        ]
    }

    result = RolePredictor.predict(resume_data)

    assert isinstance(result, dict)
    assert "roles" in result
    assert "Backend Developer" in result["roles"]


def test_python_developer_prediction():
    resume_data = {
        "skills": [
            "Python",
        ]
    }

    result = RolePredictor.predict(resume_data)

    assert isinstance(result, dict)
    assert "Python Developer" in result["roles"]


def test_ai_ml_prediction():
    resume_data = {
        "skills": [
            "Machine Learning",
        ]
    }

    result = RolePredictor.predict(resume_data)

    assert isinstance(result, dict)
    assert "AI/ML Engineer" in result["roles"]


def test_default_prediction():
    resume_data = {
        "skills": [],
    }

    result = RolePredictor.predict(resume_data)

    assert isinstance(result, dict)
    assert result["roles"] == ["Software Developer"]
    assert result["count"] == 1