from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC


DATASET_PATH = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "ml"
    / "raw"
    / "training_data.csv"
)

ARTIFACT_DIR = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "ml"
    / "artifacts"
)

MODEL_PATH = ARTIFACT_DIR / "job_role_classifier.joblib"


def load_training_data() -> tuple[pd.Series, pd.Series]:
    df = pd.read_csv(DATASET_PATH)

    X = df["Resume Text"].astype(str).str.strip()
    y = df["Job Role"].astype(str).str.strip()

    return X, y


def build_pipeline() -> Pipeline:
    return Pipeline(
        [
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    ngram_range=(1, 2),
                    min_df=2,
                    max_df=0.95,
                    sublinear_tf=True,
                ),
            ),
            (
                "classifier",
                LinearSVC(
                    class_weight="balanced",
                    random_state=42,
                ),
            ),
        ]
    )


def train_model() -> dict:
    X, y = load_training_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    pipeline = build_pipeline()

    pipeline.fit(X_train, y_train)

    ARTIFACT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(
        pipeline,
        MODEL_PATH,
    )

    return {
        "model_path": str(MODEL_PATH),
        "training_samples": len(X_train),
        "testing_samples": len(X_test),
        "classes": len(y.unique()),
    }


if __name__ == "__main__":
    result = train_model()

    print("Training completed successfully.")
    print(f"Model: {result['model_path']}")
    print(f"Training samples: {result['training_samples']}")
    print(f"Testing samples: {result['testing_samples']}")
    print(f"Job-role classes: {result['classes']}")