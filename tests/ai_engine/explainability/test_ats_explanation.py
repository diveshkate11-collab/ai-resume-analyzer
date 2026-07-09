from app.ai_engine.explainability.ats_explanation import ATSExplanation

ats = {
    "ats_score": 85,
    "section": {
        "education": True,
        "skills": True,
        "experience": True,
        "projects": True,
    },
    "keywords": {
        "count": 4,
    },
}

result = ATSExplanation.explain(ats)

print(result)