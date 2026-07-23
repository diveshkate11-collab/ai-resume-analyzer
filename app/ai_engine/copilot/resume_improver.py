from app.ai_engine.copilot.llm_client import MockLLMClient
from app.ai_engine.copilot.prompt_manager import PromptManager


class ResumeImprover:
    """
    AI-powered resume improvement.
    """

    def __init__(self, client=None):
        self.client = client or MockLLMClient()

    def improve(self, resume: str) -> dict:
        """
        Generate AI suggestions for improving a resume.
        """

        prompt = PromptManager.resume_improver(resume)

        response = self.client.generate(prompt)

        return {
            "success": True,
            "feature": "resume_improver",
            "prompt": prompt,
            "response": response,
        }