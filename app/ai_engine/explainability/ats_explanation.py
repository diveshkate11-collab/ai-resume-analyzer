class ATSExplanation:
    """
    Explains the ATS score.
    """

    @staticmethod
    def explain(ats: dict) -> dict:
        """
        Explains the ATS score.

        Args:
            ats (dict): ATS analysis.

        Returns:
            dict
        """

        score = ats["ats_score"]

        explanation = []

        if score >= 80:
            explanation.append(
                "Your resume has a strong ATS score."
            )

        elif score >= 60:
            explanation.append(
                "Your resume has a moderate ATS score."
            )

        else:
            explanation.append(
                "Your resume needs improvement to pass ATS filters."
            )

        if ats["section"]["education"]:
            explanation.append(
                "Education section is present."
            )

        if ats["section"]["skills"]:
            explanation.append(
                "Skills section is present."
            )

        if ats["section"]["experience"]:
            explanation.append(
                "Experience section is present."
            )

        if ats["section"]["projects"]:
            explanation.append(
                "Projects section is present."
            )

        explanation.append(
            f"Matched {ats['keywords']['count']} technical skills."
        )

        return {
            "ats_score": score,
            "explanation": explanation,
        }