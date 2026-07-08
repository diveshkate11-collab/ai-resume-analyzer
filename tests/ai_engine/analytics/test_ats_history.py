from app.ai_engine.analytics.ats_history import ATSHistory

history = []

history = ATSHistory.save(history, 70)
history = ATSHistory.save(history, 85)

print(history)