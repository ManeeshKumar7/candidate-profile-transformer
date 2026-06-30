from dateutil import parser


class DateNormalizer:
    """
    Converts dates to YYYY-MM format.
    """

    @staticmethod
    def normalize(date_string: str | None):

        if not date_string:

            return None

        try:

            date = parser.parse(date_string)

            return date.strftime("%Y-%m")

        except Exception:

            return date_string