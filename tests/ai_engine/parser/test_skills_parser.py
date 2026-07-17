from app.ai_engine.parser.skills_parser import SkillsParser


def test_extract_multiple_skills():
    resume_text = """
    Python
    FastAPI
    Docker
    SQL
    """

    skills = SkillsParser.extract_skills(resume_text)

    assert "Python" in skills
    assert "FastAPI" in skills
    assert "Docker" in skills
    assert "SQL" in skills


def test_extract_single_skill():
    resume_text = "Python"

    skills = SkillsParser.extract_skills(resume_text)

    assert skills == ["Python"]


def test_no_matching_skills():
    resume_text = """
    Cooking
    Singing
    Dancing
    """

    skills = SkillsParser.extract_skills(resume_text)

    assert skills == []


def test_empty_resume():
    skills = SkillsParser.extract_skills("")

    assert skills == []