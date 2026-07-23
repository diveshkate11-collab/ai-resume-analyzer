from app.ai_engine.copilot.llm_client import MockLLMClient
from app.ai_engine.copilot.prompt_manager import PromptManager


class JDMatcher:
    """
    AI-powered resume and job description matcher.
    """

    def __init__(self, client=None):
        self.client = client or MockLLMClient()

    def match(self, resume: str, job_description: str) -> dict:
        """
        Compare a resume with a job description using AI.
        """

        prompt = PromptManager.job_match(
            resume,
            job_description,
        )

        response = self.client.generate(prompt)

        return {
            "success": True,
            "feature": "jd_matcher",
            "prompt": prompt,
            "response": response,
        }