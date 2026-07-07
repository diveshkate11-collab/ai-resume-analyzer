class JobMatcher:
    """
    Matches a resume against a job description.
    """

    @staticmethod
    def match(resume_skills: list, job_skills: list) -> dict:
        """
        Matches resume skills with job skills.

        Args:
            resume_skills (list): Skills extracted from resume.
            job_skills (list): Required job skills.

        Returns:
            dict
        """

        matched = []
        missing = []

        for skill in job_skills:

            if skill in resume_skills:
                matched.append(skill)

            else:
                missing.append(skill)

        if job_skills:
            match_percentage = (
                len(matched) / len(job_skills)
            ) * 100
        else:
            match_percentage = 0

        return {
            "matched_skills": matched,
            "missing_skills": missing,
            "match_percentage": round(match_percentage, 2),
        }