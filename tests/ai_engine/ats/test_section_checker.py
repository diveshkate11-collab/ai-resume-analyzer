from app.ai_engine.ats.section_checker import SectionChecker

resume_text = """
John Doe

Education

Skills

Projects

Python
FastAPI
"""

result = SectionChecker.check(resume_text)

print(result)