from app.ai_engine.copilot.llm_client import LLMClient


class OllamaLLMClient(LLMClient):
    """
    Ollama implementation.

    This will be connected to the Ollama REST API
    in a later step.
    """

    def generate(self, prompt: str) -> str:
        raise NotImplementedError(
            "Ollama integration is not implemented yet."
        )