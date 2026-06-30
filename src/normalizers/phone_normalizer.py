import re


class PhoneNormalizer:
    """
    Normalizes phone numbers to +91XXXXXXXXXX format.
    """

    @staticmethod
    def normalize(phone: str | None) -> str | None:

        if not phone:
            return None

        digits = re.sub(r"\D", "", phone)

        if len(digits) == 10:
            return f"+91{digits}"

        if len(digits) == 12 and digits.startswith("91"):
            return f"+{digits}"

        if len(digits) == 13 and digits.startswith("091"):
            return f"+91{digits[-10:]}"

        if phone.startswith("+"):
            return phone

        return phone