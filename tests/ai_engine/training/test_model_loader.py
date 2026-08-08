from app.ai_engine.training.model_loader import ModelLoader


def test_model_loads():
    model = ModelLoader.load()

    assert model is not None


def test_model_predicts_job_role():
    resume_text = (
        "Education: Bachelor's in Computer Science "
        "Experience: 2 years "
        "Skills: Python, FastAPI, SQL, Docker, Git"
    )

    prediction = ModelLoader.predict(resume_text)

    assert isinstance(prediction, str)
    assert prediction


def test_empty_resume_text():
    try:
        ModelLoader.predict("")
        assert False
    except ValueError as exc:
        assert str(exc) == "Resume text cannot be empty."