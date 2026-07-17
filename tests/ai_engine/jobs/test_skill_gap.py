from app.ai_engine.jobs.skill_gap import SkillGapAnalyzer


def test_backend_skill_gap():
    resume_data = {
        "skills": [
            "Python",
            "FastAPI",
        ]
    }

    missing = SkillGapAnalyzer.analyze(
        resume_data,
        "Backend Developer",
    )

    assert "SQL" in missing
    assert "Docker" in missing
    assert "Git" in missing
    assert len(missing) == 3


def test_python_skill_gap():
    resume_data = {
        "skills": [
            "Python",
        ]
    }

    missing = SkillGapAnalyzer.analyze(
        resume_data,
        "Python Developer",
    )

    assert "OOP" in missing
    assert "Git" in missing
    assert len(missing) == 2


def test_ai_ml_skill_gap():
    resume_data = {
        "skills": [
            "Python",
        ]
    }

    missing = SkillGapAnalyzer.analyze(
        resume_data,
        "AI/ML Engineer",
    )

    assert "Machine Learning" in missing
    assert "NumPy" in missing
    assert "Pandas" in missing


def test_unknown_role():
    resume_data = {
        "skills": [
            "Python",
        ]
    }

    missing = SkillGapAnalyzer.analyze(
        resume_data,
        "Unknown Role",
    )

    assert missing == []