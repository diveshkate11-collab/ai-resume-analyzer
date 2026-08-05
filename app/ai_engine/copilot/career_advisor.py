import json
from app.ai_engine.copilot.response_parser import ResponseParser
from app.ai_engine.copilot.llm_factory import LLMFactory
from app.ai_engine.copilot.prompt_manager import PromptManager


class CareerAdvisor:
    """
    AI-powered career advisor.
    """

    def __init__(self, client=None):
        self.client = client or LLMFactory.create()

    def advise(self, resume: str) -> dict:
        """
        Generate career guidance using AI.
        """

        prompt = PromptManager.career_advice(
            resume
        )

        response = ResponseParser.parse(
            self.client.generate(prompt)
        )

        if isinstance(response, str):
            try:
                response = json.loads(response)
            except json.JSONDecodeError:
                pass
            
        return {
            "success": True,
            "feature": "career_advisor",
            "prompt": prompt,
            "response": response,
        }