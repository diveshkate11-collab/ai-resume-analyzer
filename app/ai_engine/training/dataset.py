from pathlib import Path

import pandas as pd


DATASET_PATH = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "ml"
    / "raw"
    / "training_data.csv"
)


REQUIRED_COLUMNS = [
    "Resume ID",
    "Resume Text",
    "Education",
    "Experience Years",
    "Skills",
    "Job Role",
    "Category",
]


def load_dataset() -> pd.DataFrame:
    """
    Load and validate the resume classification dataset.
    """

    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Training dataset not found: {DATASET_PATH}"
        )

    df = pd.read_csv(DATASET_PATH)

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df.empty:
        raise ValueError("Training dataset is empty.")

    if df["Resume Text"].isna().any():
        raise ValueError("Resume Text contains missing values.")

    if df["Job Role"].isna().any():
        raise ValueError("Job Role contains missing values.")

    return df


def prepare_text(df: pd.DataFrame) -> pd.Series:
    """
    Prepare resume text for NLP modeling.
    """

    text = (
        df["Resume Text"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    return text


def get_features_and_target(
    df: pd.DataFrame,
) -> tuple[pd.Series, pd.Series]:
    """
    Return NLP input features and job-role target.
    """

    X = prepare_text(df)
    y = df["Job Role"].astype(str).str.strip()

    return X, y