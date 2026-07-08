from app.ai_engine.analytics.resume_compare import ResumeCompare

old_resume = {
    "skills": [
        "Python",
        "SQL",
    ],
    "ats": {
        "ats_score": 70,
    },
}

new_resume = {
    "skills": [
        "Python",
        "SQL",
        "Docker",
        "Git",
    ],
    "ats": {
        "ats_score": 85,
    },
}

result = ResumeCompare.compare(
    old_resume,
    new_resume,
)

print(result)