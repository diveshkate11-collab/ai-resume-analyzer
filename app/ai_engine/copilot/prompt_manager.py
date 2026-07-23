class PromptManager:
    """
    Centralized prompt templates for AI Copilot.
    """

    @staticmethod
    def resume_improver(resume: str) -> str:
        return f"""
You are an expert resume reviewer.

Analyze the following resume.

Provide:
1. Strengths
2. Weaknesses
3. Missing skills
4. ATS improvements
5. Professional suggestions

Resume:

{resume}
"""

    @staticmethod
    def resume_rewriter(resume: str) -> str:
        return f"""
Rewrite the following resume professionally.

Improve:
- Grammar
- Formatting
- Professional wording
- ATS optimization

Resume:

{resume}
"""

    @staticmethod
    def job_match(resume: str, job_description: str) -> str:
        return f"""
Compare this resume with the given job description.

Return:
- Match percentage
- Missing skills
- Improvement suggestions

Resume:

{resume}

Job Description:

{job_description}
"""

    @staticmethod
    def cover_letter(resume: str, company: str, role: str) -> str:
        return f"""
Write a professional cover letter.

Company:
{company}

Role:
{role}

Resume:

{resume}
"""

    @staticmethod
    def career_advice(resume: str) -> str:
        return f"""
Analyze this resume.

Suggest:
- Career path
- Skills to learn
- Certifications
- Next career steps

Resume:

{resume}
"""