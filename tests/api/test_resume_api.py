from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_resume_upload():
    BASE_DIR = Path(__file__).resolve().parent.parent
    sample_resume = BASE_DIR / "uploads" / "sample_resume.pdf"

    with open(sample_resume, "rb") as file:
        response = client.post(
            "/api/resume/upload",
            files={
                "file": (
                    sample_resume.name,
                    file,
                    "application/pdf",
                )
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert "analysis" in data
    assert "ats" in data["analysis"]
    assert "recommendation" in data["analysis"]