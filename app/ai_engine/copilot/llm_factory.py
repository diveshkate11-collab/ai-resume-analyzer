from app.ai_engine.copilot.llm_client import MockLLMClient
from app.ai_engine.copilot.ollama_client import OllamaLLMClient
from app.core.settings import settings


class LLMFactory:
    """
    Creates the appropriate LLM client based on configuration.
    """

    @staticmethod
    def create():
        provider = settings.LLM_PROVIDER.lower()

        if provider == "mock":
            return MockLLMClient()

        if provider == "ollama":
            return OllamaLLMClient()

        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )