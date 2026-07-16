from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_job_recommendation():
    payload = {
        "skills": [
            "Python",
            "FastAPI",
        ],
        "education": True,
        "experience": False,
    }

    response = client.post(
        "/api/jobs/recommend",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["recommended_role"] == "Backend Developer"

    assert "SQL" in data["skill_gap"]

    assert isinstance(
        data["recommendations"],
        list,
    )

    assert isinstance(
        data["matched_jobs"],
        list,
    )