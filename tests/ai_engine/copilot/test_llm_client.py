from app.ai_engine.copilot.llm_client import MockLLMClient


def test_mock_llm_returns_string():
    client = MockLLMClient()

    response = client.generate(
        "Hello AI"
    )

    assert isinstance(response, str)


def test_mock_llm_contains_placeholder():
    client = MockLLMClient()

    response = client.generate(
        "Hello AI"
    )

    assert "Mock AI Response" in response


def test_mock_llm_contains_prompt_preview():
    client = MockLLMClient()

    response = client.generate(
        "Resume Analysis"
    )

    assert "Resume Analysis" in response