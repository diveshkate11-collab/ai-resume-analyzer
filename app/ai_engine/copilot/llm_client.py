from abc import ABC, abstractmethod


class LLMClient(ABC):
    """
    Base interface for all Large Language Model providers.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from the LLM.
        """
        pass


class MockLLMClient(LLMClient):
    """
    Temporary implementation for development and testing.

    Replace with OpenAI, Ollama, Gemini, etc.
    """

    def generate(self, prompt: str) -> str:
        return (
            "Mock AI Response\n\n"
            "This is a placeholder response.\n\n"
            "Prompt Preview:\n"
            f"{prompt[:300]}"
        )