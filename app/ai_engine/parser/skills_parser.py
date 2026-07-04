import os


class SkillsParser:

    @staticmethod
    def extract_skills(text: str) -> list:
        skills_folder = "data/skills"

        all_skills = []
        matched_skills = []

        text = text.lower()

        files = os.listdir(skills_folder)

        for file in files:
            file_path = os.path.join(skills_folder, file)

            with open(file_path, "r") as f:
                skills = f.read().splitlines()
                all_skills.extend(skills)

        for skill in all_skills:

            if skill.lower() in text:
                matched_skills.append(skill)

        return matched_skills