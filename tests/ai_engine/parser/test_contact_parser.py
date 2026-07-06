from app.ai_engine.parser.contact_parser import ContactParser

resume_text = """
Alex Johnson
alex.johnson@example.com
+91 9123456789
New Delhi
"""

contact = ContactParser.extract_contact(resume_text)

print(contact)