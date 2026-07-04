from app.ai_engine.parser.resume_parser import ResumeParser

result = ResumeParser.extract(
    "uploads/resumes/sample_resume.pdf"
)

print(result)