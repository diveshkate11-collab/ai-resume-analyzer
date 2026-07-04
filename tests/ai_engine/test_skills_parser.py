from app.ai_engine.parser.skills_parser import SkillsParser

resume_text = """
Python
FastAPI
Docker
"""

skills = SkillsParser.extract_skills(resume_text)

print("Matched Skills:")
print(skills)