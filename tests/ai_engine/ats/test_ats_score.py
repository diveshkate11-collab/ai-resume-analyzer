from app.ai_engine.ats.ats_score import ATSScorer

resume_text = """
John Doe

Education

B.Tech in Computer Science

Skills

Python
SQL
FastAPI
Docker

Projects

AI Resume Copilot

Experience

Fresher
"""

result = ATSScorer.calculate(resume_text)

print(result)