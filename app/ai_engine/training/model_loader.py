from pathlib import Path

import joblib


MODEL_PATH = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "ml"
    / "artifacts"
    / "job_role_classifier.joblib"
)


class ModelLoader:
    """Load and provide access to the trained job-role classifier."""

    _model = None

    @classmethod
    def load(cls):
        """Load the trained model once and reuse it."""
        if cls._model is None:
            if not MODEL_PATH.exists():
                raise FileNotFoundError(
                    f"Trained model not found: {MODEL_PATH}"
                )

            cls._model = joblib.load(MODEL_PATH)

        return cls._model

    @classmethod
    def predict(cls, resume_text: str) -> str:
        """Predict the most likely job role from resume text."""
        if not resume_text or not resume_text.strip():
            raise ValueError("Resume text cannot be empty.")

        model = cls.load()

        prediction = model.predict([resume_text.strip()])

        return str(prediction[0])