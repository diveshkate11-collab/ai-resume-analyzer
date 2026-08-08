from app.ai_engine.training.model_loader import ModelLoader


class PredictionService:
    """Provide job-role prediction functionality for the application."""

    @staticmethod
    def predict_job_role(resume_text: str) -> dict:
        """Predict a job role and return a structured result."""
        if not resume_text or not resume_text.strip():
            raise ValueError("Resume text cannot be empty.")

        job_role = ModelLoader.predict(resume_text)

        return {
            "job_role": job_role,
            "resume_text_length": len(resume_text.strip()),
        }