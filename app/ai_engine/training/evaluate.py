from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split


DATASET_PATH = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "ml"
    / "raw"
    / "training_data.csv"
)

MODEL_PATH = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "ml"
    / "artifacts"
    / "job_role_classifier.joblib"
)


def evaluate_model() -> dict:
    df = pd.read_csv(DATASET_PATH)

    X = df["Resume Text"].astype(str).str.strip()
    y = df["Job Role"].astype(str).str.strip()

    _, X_test, _, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = joblib.load(MODEL_PATH)

    predictions = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision_macro": precision_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),
        "recall_macro": recall_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),
        "f1_macro": f1_score(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        ),
        "precision_weighted": precision_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0,
        ),
        "recall_weighted": recall_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0,
        ),
        "f1_weighted": f1_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0,
        ),
    }

    print("\n=== MODEL EVALUATION ===")
    print(f"Accuracy:          {metrics['accuracy']:.4f}")
    print(f"Macro Precision:   {metrics['precision_macro']:.4f}")
    print(f"Macro Recall:      {metrics['recall_macro']:.4f}")
    print(f"Macro F1:          {metrics['f1_macro']:.4f}")
    print(f"Weighted Precision:{metrics['precision_weighted']:.4f}")
    print(f"Weighted Recall:   {metrics['recall_weighted']:.4f}")
    print(f"Weighted F1:       {metrics['f1_weighted']:.4f}")

    print("\n=== CLASSIFICATION REPORT ===")
    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0,
        )
    )

    return metrics


if __name__ == "__main__":
    evaluate_model()