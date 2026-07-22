class ProgressTracker:
    """
    Track learning progress.
    """

    @staticmethod
    def track(completed: int, total: int) -> dict:
        """
        Calculate learning progress.
        """

        if total <= 0:
            progress = 0.0
        else:
            progress = round((completed / total) * 100, 2)

        return {
            "completed": completed,
            "total": total,
            "progress": progress,
        }