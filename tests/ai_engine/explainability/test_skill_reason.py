from app.ai_engine.explainability.skill_reason import SkillReason

matched = [
    "Python",
    "SQL",
    "FastAPI",
]

missing = [
    "Docker",
    "Git",
]

result = SkillReason.explain(
    matched,
    missing,
)

print(result)