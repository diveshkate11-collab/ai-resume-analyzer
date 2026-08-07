from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_improve_resume():
    response = client.post(
        "/copilot/improve",
        json={
            "resume": "Python FastAPI SQL"
        },
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


def test_rewrite_resume():
    response = client.post(
        "/copilot/rewrite",
        json={
            "resume": "Python FastAPI SQL"
        },
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


def test_rewrite_resume_empty_resume():
    response = client.post(
        "/copilot/rewrite",
        json={
            "resume": ""
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is False
    assert data["feature"] == "resume_rewriter"
    assert data["error"] == "Resume cannot be empty."


def test_job_match():
    response = client.post(
        "/copilot/job-match",
        json={
            "resume": "Python FastAPI SQL",
            "job_description": "Backend Developer",
        },
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


def test_career_advice():
    response = client.post(
        "/copilot/career-advice",
        json={
            "resume": "Python FastAPI SQL"
        },
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


def test_cover_letter():
    response = client.post(
        "/copilot/cover-letter",
        json={
            "resume": "Python FastAPI SQL",
            "company": "Google",
            "role": "Software Engineer",
        },
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


def test_explain():
    response = client.post(
        "/copilot/explain",
        json={
            "content": "ATS Score: 85"
        },
    )

    assert response.status_code == 200
    assert response.json()["success"] is True