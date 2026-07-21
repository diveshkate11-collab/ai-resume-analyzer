from app.ai_engine.analytics.ats_history import ATSHistory


def test_save_first_score():
    history = []

    history = ATSHistory.save(history, 70)

    assert history == [70]


def test_save_multiple_scores():
    history = []

    history = ATSHistory.save(history, 70)
    history = ATSHistory.save(history, 82)
    history = ATSHistory.save(history, 91)

    assert history == [70, 82, 91]


def test_latest_score():
    history = [65, 75, 88]

    assert ATSHistory.latest(history) == 88


def test_latest_empty_history():
    assert ATSHistory.latest([]) is None