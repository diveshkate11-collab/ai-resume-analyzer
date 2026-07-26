import requests

from app.ai_engine.copilot.llm_client import LLMClient
from app.core.settings import settings


class OllamaLLMClient(LLMClient):
    """
    Ollama LLM provider implementation.
    """

    def generate(self, prompt: str) -> str:
        """
        Generate a response from Ollama.
        """

        payload = {
            "model": settings.LLM_MODEL,
            "prompt": prompt,
            "stream": False,
        }

        try:
            response = requests.post(
                f"{settings.OLLAMA_BASE_URL}/api/generate",
                json=payload,
                timeout=settings.LLM_TIMEOUT,
            )

            response.raise_for_status()

            data = response.json()

            return data.get(
                "response",
                "No response returned from Ollama."
            )

        except requests.exceptions.RequestException as exc:
            raise RuntimeError(
                f"Failed to communicate with Ollama: {exc}"
            ) from exc