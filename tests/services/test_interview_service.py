from app.services.interview_service import InterviewService


def test_interview_service():
    answer = (
        "Python is a high level programming language used for "
        "web development machine learning automation and data analysis."
    )

    report = InterviewService.analyze(
        "Python Developer",
        answer,
    )

    assert report["role"] == "Python Developer"
    assert report["evaluation"]["score"] == 100
    assert len(report["roadmap"]) == 3


def test_interview_service_empty_answer():
    report = InterviewService.analyze(
        "Backend Developer",
        "",
    )

    assert report["evaluation"]["score"] == 0
    assert report["feedback"] == "No answer was provided."
    assert len(report["roadmap"]) == 3