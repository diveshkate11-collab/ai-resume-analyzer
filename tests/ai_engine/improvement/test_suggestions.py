from app.ai_engine.improvement.suggestions import SuggestionGenerator


def test_suggestions():
    data = {
        "skills": [
            "Python",
        ],
        "education": {},
        "experience": {},
    }

    result = SuggestionGenerator.generate(data)

    assert isinstance(result, list)

    assert "Learn SQL and add it to your resume." in result
    assert "Learn Docker for backend deployment." in result
    assert "Add Git and GitHub experience." in result
    assert "Build REST APIs using FastAPI." in result
    assert (
        "Include internships, projects, or freelance experience."
        in result
    )

    assert (
        "Quantify achievements using numbers wherever possible."
        in result
    )

    assert (
        "Keep the resume limited to one page if you are a fresher."
        in result
    )