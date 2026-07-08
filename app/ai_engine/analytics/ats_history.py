class ATSHistory:
    """
    Stores ATS score history.
    """

    @staticmethod
    def save(history: list, ats_score: int) -> list:
        """
        Saves ATS score.

        Args:
            history (list): Existing history.
            ats_score (int): Current ATS score.

        Returns:
            list
        """

        history.append(ats_score)

        return history