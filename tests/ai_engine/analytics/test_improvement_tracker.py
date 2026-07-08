from app.ai_engine.analytics.improvement_tracker import ImprovementTracker

comparison = {
    "old_ats_score": 70,
    "new_ats_score": 85,
    "ats_difference": 15,
    "added_skills": [
        "Docker",
        "Git",
    ],
    "removed_skills": [],
}

result = ImprovementTracker.track(comparison)

print(result)