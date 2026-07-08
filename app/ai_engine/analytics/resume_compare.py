class ResumeCompare:
    """
    Compares two parsed resumes.
    """

    @staticmethod
    def compare(old_resume: dict, new_resume: dict) -> dict:
        """
        Compares two resumes.

        Args:
            old_resume (dict): Previous resume.
            new_resume (dict): Updated resume.

        Returns:
            dict
        """

        old_skills = set(old_resume["skills"])
        new_skills = set(new_resume["skills"])

        added_skills = list(new_skills - old_skills)
        removed_skills = list(old_skills - new_skills)

        old_score = old_resume["ats"]["ats_score"]
        new_score = new_resume["ats"]["ats_score"]

        return {
            "old_ats_score": old_score,
            "new_ats_score": new_score,
            "ats_difference": new_score - old_score,
            "added_skills": added_skills,
            "removed_skills": removed_skills,
        }