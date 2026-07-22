from app.ai_engine.training.course_recommender import CourseRecommender


def test_recommend_known_skills():
    result = CourseRecommender.recommend(
        [
            "Docker",
            "Git",
        ]
    )

    assert len(result) == 2
    assert result[0]["skill"] == "Docker"
    assert "Docker" in result[0]["course"]
    assert result[1]["skill"] == "Git"


def test_recommend_unknown_skill():
    result = CourseRecommender.recommend(
        [
            "Kubernetes",
        ]
    )

    assert result[0]["skill"] == "Kubernetes"
    assert result[0]["course"] == "No course available."


def test_empty_missing_skills():
    result = CourseRecommender.recommend([])

    assert result == []