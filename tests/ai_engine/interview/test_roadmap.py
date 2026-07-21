from app.ai_engine.interview.roadmap import InterviewRoadmap


def test_high_score_roadmap():
    roadmap = InterviewRoadmap.generate(95)

    assert len(roadmap) == 3
    assert "Practice advanced interview questions." in roadmap


def test_medium_score_roadmap():
    roadmap = InterviewRoadmap.generate(70)

    assert len(roadmap) == 3
    assert "Strengthen core programming concepts." in roadmap


def test_low_score_roadmap():
    roadmap = InterviewRoadmap.generate(40)

    assert len(roadmap) == 3
    assert "Learn programming fundamentals." in roadmap