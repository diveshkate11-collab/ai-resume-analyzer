import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Application settings.
    """

    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

    LLM_MODEL = os.getenv("LLM_MODEL", "llama3.2")

    LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT", 60))

    LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", 0.3))

    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )


settings = Settings()