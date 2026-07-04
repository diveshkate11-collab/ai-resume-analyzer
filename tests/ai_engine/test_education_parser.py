from app.ai_engine.parser.education_parser import EducationParser

resume_text = """
Alex Johnson

Bachelor of Technology in Artificial Intelligence and Machine Learning

XYZ University
"""

education = EducationParser.extract_education(resume_text)

print(education)