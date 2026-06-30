class ProfileValidator:
    """
    Performs basic validation on the projected output.
    """

    REQUIRED_FIELDS = [
        "full_name",
        "primary_emails",
    ]

    def validate(self, profile: dict):

        missing = []

        for field in self.REQUIRED_FIELDS:

            value = profile.get(field)

            if value is None:
                missing.append(field)

            elif isinstance(value, list) and len(value) == 0:
                missing.append(field)

            elif value == "":
                missing.append(field)

        return {
            "valid": len(missing) == 0,
            "missing_fields": missing,
        }