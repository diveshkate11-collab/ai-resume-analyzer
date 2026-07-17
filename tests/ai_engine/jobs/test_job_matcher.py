from app.ai_engine.jobs.job_matcher import JobMatcher


def test_backend_jobs():
    jobs = JobMatcher.match("Backend Developer")

    assert "Backend Developer Intern" in jobs
    assert "Junior Backend Developer" in jobs
    assert len(jobs) == 3


def test_python_jobs():
    jobs = JobMatcher.match("Python Developer")

    assert "Python Developer" in jobs
    assert len(jobs) == 3


def test_ai_ml_jobs():
    jobs = JobMatcher.match("AI/ML Engineer")

    assert "AI Engineer" in jobs
    assert len(jobs) == 3


def test_default_jobs():
    jobs = JobMatcher.match("Unknown Role")

    assert jobs == ["Software Engineer"]