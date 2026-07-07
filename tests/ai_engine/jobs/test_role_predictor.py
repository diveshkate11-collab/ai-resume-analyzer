from app.ai_engine.jobs.role_predictor import RolePredictor

skills = [
    "Python",
    "SQL",
    "FastAPI",
    "Docker",
]

roles = RolePredictor.predict(skills)

print(roles)