from app.ai_engine.interview.question_generator import QuestionGenerator


def test_python_developer_questions():
    result = QuestionGenerator.generate("Python Developer")

    assert result["role"] == "Python Developer"
    assert len(result["technical_questions"]) == 10
    assert len(result["hr_questions"]) == 20
    assert "What is Python?" in result["technical_questions"]


def test_backend_developer_questions():
    result = QuestionGenerator.generate("Backend Developer")

    assert result["role"] == "Backend Developer"
    assert len(result["technical_questions"]) == 10
    assert "Explain REST API." in result["technical_questions"]


def test_ai_engineer_questions():
    result = QuestionGenerator.generate("AI Engineer")

    assert result["role"] == "AI Engineer"
    assert len(result["technical_questions"]) == 10
    assert "What is Deep Learning?" in result["technical_questions"]


def test_unknown_role():
    result = QuestionGenerator.generate("Blockchain Developer")

    assert result["role"] == "Blockchain Developer"
    assert result["technical_questions"] == [
        "No technical questions available for this role yet."
    ]
    assert len(result["hr_questions"]) == 20


def test_role_alias():
    result = QuestionGenerator.generate("python")

    assert result["role"] == "python"
    assert "What is Python?" in result["technical_questions"]