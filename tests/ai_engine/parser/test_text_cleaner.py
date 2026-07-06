from app.ai_engine.parser.text_cleaner import TextCleaner

sample_text = """



John Doe


    Python        FastAPI


Machine Learning




SQL




"""

cleaned = TextCleaner.clean(sample_text)

print("Original:\n")
print(sample_text)

print("\n----------------------------\n")

print("Cleaned:\n")
print(cleaned)