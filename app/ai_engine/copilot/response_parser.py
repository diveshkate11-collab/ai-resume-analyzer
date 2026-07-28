import json


class ResponseParser:
    """
    Parse AI responses into Python objects.
    """

    @staticmethod
    def parse(response):
        """
        Convert JSON strings into Python objects.
        Return the original response if parsing fails.
        """

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return response