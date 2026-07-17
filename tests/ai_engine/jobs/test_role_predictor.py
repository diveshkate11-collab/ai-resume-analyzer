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

    role = RolePredictor.predict(resume_data)

    assert role == "Backend Developer"


def test_python_developer_prediction():
    resume_data = {
        "skills": [
            "Python",
        ]
    }

    role = RolePredictor.predict(resume_data)

    assert role == "Python Developer"


def test_ai_ml_prediction():
    resume_data = {
        "skills": [
            "Machine Learning",
        ]
    }

    role = RolePredictor.predict(resume_data)

    assert role == "AI/ML Engineer"


def test_default_prediction():
    resume_data = {
        "skills": []
    }

    role = RolePredictor.predict(resume_data)

    assert role == "Software Developer"