from app.ai_engine.jobs.recommendation import RecommendationEngine


def test_backend_recommendations():
    recommendations = RecommendationEngine.generate(
        "Backend Developer",
    )

    assert "Build REST APIs using FastAPI." in recommendations
    assert "Learn Docker and containerization." in recommendations
    assert len(recommendations) == 3


def test_python_recommendations():
    recommendations = RecommendationEngine.generate(
        "Python Developer",
    )

    assert "Strengthen Python fundamentals." in recommendations
    assert len(recommendations) == 3


def test_ai_ml_recommendations():
    recommendations = RecommendationEngine.generate(
        "AI/ML Engineer",
    )

    assert "Learn deep learning with PyTorch." in recommendations
    assert len(recommendations) == 3


def test_unknown_role_recommendations():
    recommendations = RecommendationEngine.generate(
        "Unknown Role",
    )

    assert recommendations == [
        "Continue improving your technical skills."
    ]