from app.ai_engine.copilot.llm_factory import LLMFactory
from app.ai_engine.copilot.prompt_manager import PromptManager
from app.ai_engine.copilot.response_parser import ResponseParser


class JDMatcher:
    """
    AI-powered resume and job description matcher.
    """

    def __init__(self, client=None):
        self.client = client or LLMFactory.create()

    def match(self, resume: str, job_description: str) -> dict:
        """
        Compare a resume with a job description using AI.
        """

        prompt = PromptManager.job_match(
            resume,
            job_description,
        )

        response = ResponseParser.parse(
            self.client.generate(prompt)
        )

        return {
            "success": True,
            "feature": "jd_matcher",
            "prompt": prompt,
            "response": response,
        }