from app.ai_engine.parser.experience_parser import ExperienceParser

resume_text = """
Alex Johnson

Software Engineer

2 years of experience in Python, FastAPI and SQL.
"""

experience = ExperienceParser.extract_experience(resume_text)

print(experience)