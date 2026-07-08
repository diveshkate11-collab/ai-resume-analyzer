class ImprovementTracker:
    """
    Tracks improvements between two resume analyses.
    """

    @staticmethod
    def track(comparison: dict) -> dict:
        """
        Generates improvement summary.

        Args:
            comparison (dict): Output from ResumeCompare.

        Returns:
            dict
        """

        improvements = []

        if comparison["ats_difference"] > 0:
            improvements.append(
                f"ATS score improved by {comparison['ats_difference']} points."
            )

        elif comparison["ats_difference"] < 0:
            improvements.append(
                f"ATS score decreased by {abs(comparison['ats_difference'])} points."
            )

        else:
            improvements.append(
                "ATS score remained unchanged."
            )

        if comparison["added_skills"]:
            improvements.append(
                f"Added skills: {', '.join(comparison['added_skills'])}."
            )

        if comparison["removed_skills"]:
            improvements.append(
                f"Removed skills: {', '.join(comparison['removed_skills'])}."
            )

        return {
            "improvements": improvements
        }