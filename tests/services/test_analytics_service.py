from app.services.analytics_service import AnalyticsService


def test_generate_analytics_report():
    history = [70, 80, 90]

    report = AnalyticsService.generate(history)

    assert report["history"] == [70, 80, 90]
    assert report["latest_score"] == 90
    assert report["tracking"]["total_attempts"] == 3
    assert report["tracking"]["improvement"] == 20


def test_generate_empty_history():
    report = AnalyticsService.generate([])

    assert report["history"] == []
    assert report["latest_score"] is None
    assert report["tracking"]["total_attempts"] == 0
    assert report["tracking"]["improvement"] == 0