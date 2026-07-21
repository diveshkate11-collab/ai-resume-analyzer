from app.ai_engine.interview.interview_analyzer import InterviewAnalyzer


def test_complete_interview_analysis():
    answer = (
        "Python is a high level programming language used for "
        "web development machine learning automation and data analysis."
    )

    result = InterviewAnalyzer.analyze(
        "Python Developer",
        answer,
    )

    assert result["role"] == "Python Developer"
    assert len(result["technical_questions"]) == 10
    assert len(result["hr_questions"]) == 20
    assert result["evaluation"]["score"] == 100
    assert (
        result["feedback"]
        == "Excellent answer. Keep up the good work."
    )


def test_empty_answer():
    result = InterviewAnalyzer.analyze(
        "Backend Developer",
        "",
    )

    assert result["evaluation"]["score"] == 0
    assert result["feedback"] == "No answer was provided."