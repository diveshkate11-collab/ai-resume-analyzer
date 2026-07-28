from app.ai_engine.copilot.llm_factory import LLMFactory
from app.ai_engine.copilot.response_parser import ResponseParser


class ExplanationEngine:
    """
    AI-powered explanation engine.
    """

    def __init__(self, client=None):
        self.client = client or LLMFactory.create()

    def explain(self, content: str) -> dict:
        """
        Generate an easy-to-understand explanation for AI outputs.
        """

        prompt = f"""
You are an AI assistant.

Explain the following content in simple, professional language.

Content:

{content}
"""

        response = ResponseParser.parse(
            self.client.generate(prompt)
        )

        return {
            "success": True,
            "feature": "explanation_engine",
            "prompt": prompt,
            "response": response,
        }