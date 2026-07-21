class ATSHistory:
    """
    Stores ATS score history for resume analyses.
    """

    @staticmethod
    def save(history: list[int], score: int) -> list[int]:
        """
        Save a new ATS score.
        """
        history.append(score)
        return history

    @staticmethod
    def latest(history: list[int]) -> int | None:
        """
        Return the latest ATS score.
        """
        if not history:
            return None

        return history[-1]