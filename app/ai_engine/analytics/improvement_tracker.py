class ImprovementTracker:
    """
    Tracks ATS score improvement over time.
    """

    @staticmethod
    def track(history: list[int]) -> dict:
        """
        Analyze ATS score history.
        """
        if not history:
            return {
                "total_attempts": 0,
                "improvement": 0,
            }

        return {
            "total_attempts": len(history),
            "improvement": history[-1] - history[0],
        }