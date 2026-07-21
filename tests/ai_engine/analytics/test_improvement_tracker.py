from app.ai_engine.analytics.improvement_tracker import ImprovementTracker


def test_empty_history():
    result = ImprovementTracker.track([])

    assert result["total_attempts"] == 0
    assert result["improvement"] == 0


def test_improvement():
    result = ImprovementTracker.track([70, 80, 90])

    assert result["total_attempts"] == 3
    assert result["improvement"] == 20


def test_decline():
    result = ImprovementTracker.track([90, 80, 70])

    assert result["total_attempts"] == 3
    assert result["improvement"] == -20