from app.ai_engine.parser.education_parser import EducationParser


def test_extract_btech():
    resume_text = """
    Alex Johnson

    Bachelor of Technology in Artificial Intelligence and Machine Learning

    XYZ University
    """

    education = EducationParser.extract_education(resume_text)

    assert education["degree"] == "Bachelor of Technology"


def test_extract_be():
    resume_text = """
    Bachelor of Engineering
    """

    education = EducationParser.extract_education(resume_text)

    assert education["degree"] == "Bachelor of Engineering"


def test_extract_bsc():
    resume_text = """
    BSc
    """

    education = EducationParser.extract_education(resume_text)

    assert education["degree"] == "BSc"


def test_no_education():
    education = EducationParser.extract_education(
        "Python FastAPI SQL"
    )

    assert education["degree"] is None