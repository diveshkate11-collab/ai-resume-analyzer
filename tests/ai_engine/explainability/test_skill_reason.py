from app.ai_engine.explainability.skill_reason import SkillReason


def test_with_matched_and_missing_skills():
    matched = [
        "Python",
        "SQL",
        "FastAPI",
    ]

    missing = [
        "Docker",
        "Git",
    ]

    result = SkillReason.explain(
        matched,
        missing,
    )

    assert isinstance(result, dict)


def test_only_matched_skills():
    matched = [
        "Python",
        "SQL",
    ]

    result = SkillReason.explain(
        matched,
        [],
    )

    assert isinstance(result, dict)


def test_only_missing_skills():
    missing = [
        "Docker",
        "Git",
    ]

    result = SkillReason.explain(
        [],
        missing,
    )

    assert isinstance(result, dict)


def test_empty_lists():
    result = SkillReason.explain(
        [],
        [],
    )

    assert isinstance(result, dict)