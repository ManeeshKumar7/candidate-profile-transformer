from src.models.candidate import Candidate


class Projector:
    """
    Converts a Candidate object into the output JSON
    according to the runtime configuration.
    """

    def project(
        self,
        candidate: Candidate,
        config: dict,
    ) -> dict:

        output = {}

        fields = config.get("fields", [])

        rename = config.get("rename", {})

        for field in fields:

            if not hasattr(candidate, field):
                continue

            value = getattr(candidate, field)

            if value is None:
                continue

            output_name = rename.get(field, field)

            # -------------------------
            # Emails
            # -------------------------

            if field == "emails":

                output[output_name] = [
                    email.value
                    for email in value
                ]

            # -------------------------
            # Phones
            # -------------------------

            elif field == "phones":

                output[output_name] = [
                    phone.value
                    for phone in value
                ]

            # -------------------------
            # Skills
            # -------------------------

            elif field == "skills":

                output[output_name] = [
                    skill.name
                    for skill in value
                ]

            # -------------------------
            # Experience
            # -------------------------

            elif field == "experience":

                output[output_name] = [
                    exp.model_dump()
                    for exp in value
                ]

            # -------------------------
            # Education
            # -------------------------

            elif field == "education":

                output[output_name] = [
                    edu.model_dump()
                    for edu in value
                ]

            # -------------------------
            # Location / Links
            # -------------------------

            elif field in ("location", "links"):

                output[output_name] = value.model_dump()

            else:

                output[output_name] = value

        return output