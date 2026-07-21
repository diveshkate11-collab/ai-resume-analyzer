from app.ai_engine.interview.answer_evaluator import AnswerEvaluator


def test_empty_answer():
    result = AnswerEvaluator.evaluate("")

    assert result["score"] == 0
    assert result["result"] == "No Answer"


def test_short_answer():
    result = AnswerEvaluator.evaluate(
        "Python is a programming language."
    )

    assert result["score"] == 50
    assert result["result"] == "Needs Improvement"


def test_good_answer():
    answer = (
        "Python is a high level programming language used for "
        "web development machine learning automation and data analysis."
    )

    result = AnswerEvaluator.evaluate(answer)

    assert result["score"] == 100
    assert result["result"] == "Good Answer"