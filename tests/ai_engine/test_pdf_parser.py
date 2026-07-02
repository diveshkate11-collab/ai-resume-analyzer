from app.ai_engine.parser.pdf_parser import PDFParser

result = PDFParser.extract_text("uploads/resumes/sample_resume.pdf")

print(f"Pages      : {result['pages']}")
print(f"Characters : {result['characters']}")
print("\nPreview:\n")
print(result["text"][:500])