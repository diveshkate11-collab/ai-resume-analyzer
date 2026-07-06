from app.ai_engine.ats.grammar_checker import GrammarChecker

resume_text = """
John Doe

Python
FastAPI
"""

result = GrammarChecker.check(resume_text)

print(result)