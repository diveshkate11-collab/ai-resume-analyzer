from app.ai_engine.copilot.llm_factory import LLMFactory
from app.ai_engine.copilot.prompt_manager import PromptManager
from app.ai_engine.copilot.response_parser import ResponseParser


class CoverLetterGenerator:
    """
    AI-powered cover letter generator.
    """

    def __init__(self, client=None):
        self.client = client or LLMFactory.create()

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

        response = ResponseParser.parse(
            self.client.generate(prompt)
        )

        return {
            "success": True,
            "feature": "cover_letter",
            "prompt": prompt,
            "response": response,
        }