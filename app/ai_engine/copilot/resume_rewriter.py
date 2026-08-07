from app.ai_engine.copilot.llm_factory import LLMFactory
from app.ai_engine.copilot.prompt_manager import PromptManager
from app.ai_engine.copilot.response_parser import ResponseParser


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

        if not resume or not resume.strip():
            return {
                "success": False,
                "feature": "resume_rewriter",
                "error": "Resume cannot be empty.",
            }

        prompt = PromptManager.resume_rewriter(resume)

        response = ResponseParser.parse(
            self.client.generate(prompt)
        )

        return {
            "success": True,
            "feature": "resume_rewriter",
            "prompt": prompt,
            "response": response,
        }