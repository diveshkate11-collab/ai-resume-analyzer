from app.ai_engine.copilot.llm_factory import LLMFactory
from app.ai_engine.copilot.prompt_manager import PromptManager


class ResumeRewriter:
    """
    AI-powered resume rewriting.
    """

    def __init__(self, client=None):
        self.client = client or LLMFactory.create()

    def rewrite(self, resume: str) -> dict:
        """
        Rewrite a resume professionally using AI.
        """

        prompt = PromptManager.resume_rewriter(resume)

        response = self.client.generate(prompt)

        return {
            "success": True,
            "feature": "resume_rewriter",
            "prompt": prompt,
            "response": response,
        }