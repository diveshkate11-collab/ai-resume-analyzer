from app.ai_engine.ats.keyword_matcher import KeywordMatcher

resume_text = """
Python
FastAPI
Docker
"""

result = KeywordMatcher.match(resume_text)

print(result)