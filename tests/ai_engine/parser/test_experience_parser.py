from app.ai_engine.parser.experience_parser import ExperienceParser


def test_extract_fresher():
    resume_text = """
    Alex Johnson

    Fresher
    """

    experience = ExperienceParser.extract_experience(resume_text)

    assert experience["experience"] == "Fresher"


def test_extract_two_years():
    resume_text = """
    Alex Johnson

    2 years of experience in Python, FastAPI and SQL.
    """

    experience = ExperienceParser.extract_experience(resume_text)

    assert experience["experience"] == "2 years"


def test_extract_one_year():
    resume_text = """
    1 year of experience
    """

    experience = ExperienceParser.extract_experience(resume_text)

    assert experience["experience"] == "1 year"


def test_no_experience():
    experience = ExperienceParser.extract_experience(
        "Python FastAPI SQL"
    )

    assert experience["experience"] is None