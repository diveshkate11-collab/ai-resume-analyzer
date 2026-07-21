from app.ai_engine.analytics.analytics_engine import AnalyticsEngine


def test_generate_report():
    history = [70, 80, 90]

    report = AnalyticsEngine.generate(history)

    assert report["history"] == [70, 80, 90]
    assert report["latest_score"] == 90
    assert report["tracking"]["total_attempts"] == 3
    assert report["tracking"]["improvement"] == 20


def test_empty_history():
    report = AnalyticsEngine.generate([])

    assert report["history"] == []
    assert report["latest_score"] is None
    assert report["tracking"]["total_attempts"] == 0
    assert report["tracking"]["improvement"] == 0