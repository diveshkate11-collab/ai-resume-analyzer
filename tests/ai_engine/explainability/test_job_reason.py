from app.ai_engine.explainability.job_reason import JobReason

roles = [
    "Python Developer",
    "Backend Developer",
]

skills = [
    "Python",
    "SQL",
    "FastAPI",
]

result = JobReason.explain(
    roles,
    skills,
)

print(result)