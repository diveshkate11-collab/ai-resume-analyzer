from app.ai_engine.training.prediction_service import PredictionService


def test_predict_job_role():
    resume_text = (
        "Education: Bachelor's in Computer Science "
        "Experience: 2 years "
        "Skills: Python, FastAPI, SQL, Docker, Git"
    )

    result = PredictionService.predict_job_role(resume_text)

    assert "job_role" in result
    assert isinstance(result["job_role"], str)
    assert result["job_role"]
    assert result["resume_text_length"] > 0


def test_predict_empty_resume():
    try:
        PredictionService.predict_job_role("")
        assert False
    except ValueError as exc:
        assert str(exc) == "Resume text cannot be empty."