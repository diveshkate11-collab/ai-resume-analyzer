from app.ai_engine.parser.contact_parser import ContactParser


def test_extract_complete_contact():
    resume_text = """
    Alex Johnson
    alex.johnson@example.com
    +91 9123456789
    New Delhi
    """

    contact = ContactParser.extract_contact(resume_text)

    assert contact["name"] == "Alex Johnson"
    assert contact["email"] == "alex.johnson@example.com"
    assert contact["phone"] == "+91 9123456789"


def test_extract_email_only():
    resume_text = """
    john@example.com
    """

    contact = ContactParser.extract_contact(resume_text)

    assert contact["email"] == "john@example.com"


def test_extract_phone_only():
    resume_text = """
    +91 9876543210
    """

    contact = ContactParser.extract_contact(resume_text)

    assert contact["phone"] == "+91 9876543210"


def test_empty_contact():
    contact = ContactParser.extract_contact("")

    assert isinstance(contact, dict)