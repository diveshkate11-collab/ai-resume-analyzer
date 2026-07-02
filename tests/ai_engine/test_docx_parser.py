from app.ai_engine.parser.docx_parser import DOCXParser

result = DOCXParser.extract_text(
    "uploads/resumes/sample_resume.docx"
)

print(f"Paragraphs : {result['paragraphs']}")
print(f"Characters : {result['characters']}")
    
print("\nPreview:\n")
print(result["text"][:500])