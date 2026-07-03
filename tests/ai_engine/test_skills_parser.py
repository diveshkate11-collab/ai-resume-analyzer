from app.ai_engine.parser.skills_parser import SkillsParser

skills = SkillsParser.extract_skills("")

print("Skills Found:")
print(skills)