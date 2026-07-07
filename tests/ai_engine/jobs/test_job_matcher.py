from app.ai_engine.jobs.job_matcher import JobMatcher

resume_skills = [
    "Python",
    "SQL",
    "FastAPI",
]

job_skills = [
    "Python",
    "Docker",
    "SQL",
    "Git",
]

result = JobMatcher.match(
    resume_skills,
    job_skills,
)

print(result)