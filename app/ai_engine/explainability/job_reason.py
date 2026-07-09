class JobReason:
    """
    Explains why a job role was recommended.
    """

    @staticmethod
    def explain(roles: list, skills: list) -> dict:
        """
        Explains job recommendations.

        Args:
            roles (list): Recommended job roles.
            skills (list): Resume skills.

        Returns:
            dict
        """

        explanations = []

        for role in roles:

            explanations.append(
                {
                    "role": role,
                    "reason": (
                        f"{role} was recommended because your resume "
                        f"contains relevant skills such as "
                        f"{', '.join(skills)}."
                    ),
                }
            )

        return {
            "job_reasons": explanations
        }