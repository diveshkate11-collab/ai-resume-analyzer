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

    DB_HOST = os.getenv("DB_HOST", "localhost")

    DB_PORT = int(os.getenv("DB_PORT", 5432))

    DB_NAME = os.getenv(
        "DB_NAME",
        "ai_resume_copilot"
    )

    DB_USER = os.getenv("DB_USER", "postgres")

    DB_PASSWORD = os.getenv("DB_PASSWORD", "")


settings = Settings()