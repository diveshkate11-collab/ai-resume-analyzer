from app.ai_engine.training.dataset import (
    get_features_and_target,
    load_dataset,
    prepare_text,
)


def test_load_dataset():
    df = load_dataset()

    assert not df.empty
    assert "Resume Text" in df.columns
    assert "Job Role" in df.columns


def test_prepare_text():
    df = load_dataset()

    text = prepare_text(df)

    assert len(text) == len(df)
    assert text.notna().all()
    assert text.str.len().gt(0).all()


def test_get_features_and_target():
    df = load_dataset()

    X, y = get_features_and_target(df)

    assert len(X) == len(df)
    assert len(y) == len(df)
    assert X.iloc[0]
    assert y.iloc[0]