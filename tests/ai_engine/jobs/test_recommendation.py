from app.ai_engine.jobs.recommendation import Recommendation

result = Recommendation.generate(
    85,
    [
        "Python Developer",
        "Backend Developer",
    ],
)

print(result)