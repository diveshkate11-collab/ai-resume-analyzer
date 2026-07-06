from app.ai_engine.ats.formatting_checker import FormattingChecker

resume_text = """
John Doe

Education

B.Tech

Skills

Python
FastAPI
Docker
"""

result = FormattingChecker.check(resume_text)

print(result)