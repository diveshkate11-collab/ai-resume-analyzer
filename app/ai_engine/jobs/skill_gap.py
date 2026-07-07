from app.ai_engine.jobs.role_predictor import RolePredictor


class SkillGap:
    """
    Finds missing skills for a selected job role.
    """

    @staticmethod
    def analyze(skills: list, target_role: str) -> dict:
        """
        Compares resume skills with required job skills.

        Args:
            skills (list): Resume skills.
            target_role (str): Desired job role.

        Returns:
            dict
        """

        required_skills = RolePredictor.ROLE_SKILLS.get(target_role, [])

        matched = []
        missing = []

        for skill in required_skills:

            if skill in skills:
                matched.append(skill)

            else:
                missing.append(skill)

        return {
            "target_role": target_role,
            "matched": matched,
            "missing": missing,
        }