from app.ai_engine.copilot.llm_client import MockLLMClient
from app.ai_engine.copilot.prompt_manager import PromptManager


class CoverLetterGenerator:
    """
    AI-powered cover letter generator.
    """

    def __init__(self, client=None):
        self.client = client or MockLLMClient()

    def generate(
        self,
        resume: str,
        company: str,
        role: str,
    ) -> dict:
        """
        Generate a professional cover letter.
        """

        prompt = PromptManager.cover_letter(
            resume,
            company,
            role,
        )

        response = self.client.generate(prompt)

        return {
            "success": True,
            "feature": "cover_letter",
            "prompt": prompt,
            "response": response,
        }