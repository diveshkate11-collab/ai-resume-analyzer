from app.ai_engine.copilot.llm_client import MockLLMClient
from app.ai_engine.copilot.prompt_manager import PromptManager


class CareerAdvisor:
    """
    AI-powered career advisor.
    """

    def __init__(self, client=None):
        self.client = client or MockLLMClient()

    def advise(self, resume: str) -> dict:
        """
        Generate career guidance using AI.
        """

        prompt = PromptManager.career_advice(
            resume
        )

        response = self.client.generate(prompt)

        return {
            "success": True,
            "feature": "career_advisor",
            "prompt": prompt,
            "response": response,
        }