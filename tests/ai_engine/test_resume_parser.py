from app.ai_engine.parser.resume_parser import ResumeParser

result = ResumeParser.parse(
    "uploads/resumes/sample_resume.pdf"
)

print("========== Resume ==========\n")

print(f"Name  : {result['name']}")
print(f"Email : {result['email']}")
print(f"Phone : {result['phone']}")

print("\n========== Metadata ==========\n")
print(result["metadata"])

print("\n========== Preview ==========\n")
print(result["text"][:300])