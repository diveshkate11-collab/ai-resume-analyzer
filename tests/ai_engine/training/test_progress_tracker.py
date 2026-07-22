from app.ai_engine.training.progress_tracker import ProgressTracker


def test_progress_tracker_partial():
    result = ProgressTracker.track(2, 5)

    assert result["completed"] == 2
    assert result["total"] == 5
    assert result["progress"] == 40.0


def test_progress_tracker_complete():
    result = ProgressTracker.track(5, 5)

    assert result["progress"] == 100.0


def test_progress_tracker_zero_total():
    result = ProgressTracker.track(0, 0)

    assert result["progress"] == 0.0