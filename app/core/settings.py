class Settings:
    """
    Application settings.
    """

    LLM_PROVIDER = "ollama"

    LLM_MODEL = "llama3.2"

    LLM_TIMEOUT = 60

    LLM_TEMPERATURE = 0.3

    OLLAMA_BASE_URL = "http://localhost:11434"


settings = Settings()