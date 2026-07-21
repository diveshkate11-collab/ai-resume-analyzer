class ResumeCompare:
    """
    Compare two ATS scores and determine improvement.
    """

    @staticmethod
    def compare(previous_score: int, current_score: int) -> dict:
        difference = current_score - previous_score

        if difference > 0:
            status = "Improved"
        elif difference < 0:
            status = "Declined"
        else:
            status = "Unchanged"

        return {
            "previous_score": previous_score,
            "current_score": current_score,
            "difference": difference,
            "status": status,
        }