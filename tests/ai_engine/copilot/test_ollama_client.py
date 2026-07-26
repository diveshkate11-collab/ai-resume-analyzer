from app.ai_engine.copilot.ollama_client import OllamaLLMClient


def test_ollama_client_creation():
    """
    Test Ollama client creation.
    """

    client = OllamaLLMClient()

    assert client is not None