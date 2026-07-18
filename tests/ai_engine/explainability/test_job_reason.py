from app.ai_engine.explainability.job_reason import JobReason


def test_multiple_roles():
    roles = [
        "Python Developer",
        "Backend Developer",
    ]

    skills = [
        "Python",
        "SQL",
        "FastAPI",
    ]

    result = JobReason.explain(
        roles,
        skills,
    )

    assert isinstance(result, dict)


def test_single_role():
    roles = [
        "Python Developer",
    ]

    skills = [
        "Python",
    ]

    result = JobReason.explain(
        roles,
        skills,
    )

    assert isinstance(result, dict)


def test_no_roles():
    result = JobReason.explain(
        [],
        ["Python", "SQL"],
    )

    assert isinstance(result, dict)


def test_empty_input():
    result = JobReason.explain(
        [],
        [],
    )

    assert isinstance(result, dict)