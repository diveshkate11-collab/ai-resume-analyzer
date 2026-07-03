import os


class SkillsParser:

    @staticmethod
    def extract_skills(text: str) -> list:
        skills_folder = "data/skills"

        all_skills = []

        files = os.listdir(skills_folder)

        for file in files:
            file_path = os.path.join(skills_folder, file)

            with open(file_path, "r") as f:
                skills = f.read().splitlines()
                all_skills.extend(skills)

        return all_skills