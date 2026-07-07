from app.ai_engine.jobs.skill_gap import SkillGap

skills = [
    "Python",
    "SQL",
    "FastAPI",
]

result = SkillGap.analyze(
    skills,
    "Backend Developer"
)

print(result)