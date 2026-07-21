from app.ai_engine.interview.feedback import Feedback


def test_excellent_feedback():
    assert (
        Feedback.generate(100)
        == "Excellent answer. Keep up the good work."
    )


def test_good_feedback():
    assert (
        Feedback.generate(75)
        == "Good answer, but there is room for improvement."
    )


def test_needs_improvement_feedback():
    assert (
        Feedback.generate(40)
        == "Your answer needs improvement. Try to explain your thoughts in more detail."
    )


def test_no_answer_feedback():
    assert (
        Feedback.generate(0)
        == "No answer was provided."
    )