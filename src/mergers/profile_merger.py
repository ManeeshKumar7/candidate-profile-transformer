from src.models.candidate import Candidate


class ProfileMerger:
    """
    Merges two Candidate objects into one.
    """

    def merge(
        self,
        csv_candidate: Candidate,
        resume_candidate: Candidate,
    ) -> Candidate:

        merged = Candidate()

        # -----------------------------
        # Candidate ID
        # -----------------------------

        merged.candidate_id = csv_candidate.candidate_id

        # -----------------------------
        # Name
        # -----------------------------

        merged.full_name = (
            csv_candidate.full_name
            or resume_candidate.full_name
        )

        # -----------------------------
        # Headline
        # -----------------------------

        merged.headline = (
            csv_candidate.headline
            or resume_candidate.headline
        )

        # -----------------------------
        # Years of Experience
        # -----------------------------

        merged.years_experience = (
            csv_candidate.years_experience
            or resume_candidate.years_experience
        )

        # -----------------------------
        # Emails
        # -----------------------------

        email_map = {}

        for email in (
            csv_candidate.emails +
            resume_candidate.emails
        ):

            key = email.value.lower()

            if key not in email_map:

                email_map[key] = email

            else:

                existing = email_map[key]

                existing.metadata.sources = list(
                    set(
                        existing.metadata.sources +
                        email.metadata.sources
                    )
                )

                existing.metadata.confidence = max(
                    existing.metadata.confidence,
                    email.metadata.confidence,
                )

        merged.emails = list(email_map.values())

        # -----------------------------
        # Phones
        # -----------------------------

        phone_map = {}

        for phone in (
            csv_candidate.phones +
            resume_candidate.phones
        ):

            key = phone.value

            if key not in phone_map:

                phone_map[key] = phone

            else:

                existing = phone_map[key]

                existing.metadata.sources = list(
                    set(
                        existing.metadata.sources +
                        phone.metadata.sources
                    )
                )

                existing.metadata.confidence = max(
                    existing.metadata.confidence,
                    phone.metadata.confidence,
                )

        merged.phones = list(phone_map.values())

        # -----------------------------
        # Skills
        # -----------------------------

        skill_map = {}

        for skill in (
            csv_candidate.skills +
            resume_candidate.skills
        ):

            key = skill.name.lower()

            if key not in skill_map:

                skill_map[key] = skill

            else:

                existing = skill_map[key]

                existing.metadata.sources = list(
                    set(
                        existing.metadata.sources +
                        skill.metadata.sources
                    )
                )

                existing.metadata.confidence = max(
                    existing.metadata.confidence,
                    skill.metadata.confidence,
                )

        merged.skills = list(skill_map.values())

        # -----------------------------
        # Education
        # -----------------------------

        merged.education = (
            resume_candidate.education
            if resume_candidate.education
            else csv_candidate.education
        )

        # -----------------------------
        # Experience
        # -----------------------------

        merged.experience = (
            resume_candidate.experience
            if resume_candidate.experience
            else csv_candidate.experience
        )

        # -----------------------------
        # Location
        # -----------------------------

        merged.location = (
            csv_candidate.location
            or resume_candidate.location
        )

        # -----------------------------
        # Links
        # -----------------------------

        merged.links = (
            resume_candidate.links
            or csv_candidate.links
        )

        # -----------------------------
        # Overall Confidence
        # -----------------------------

        confidence_scores = []

        confidence_scores.extend(
            [
                email.metadata.confidence
                for email in merged.emails
            ]
        )

        confidence_scores.extend(
            [
                phone.metadata.confidence
                for phone in merged.phones
            ]
        )

        confidence_scores.extend(
            [
                skill.metadata.confidence
                for skill in merged.skills
            ]
        )

        if confidence_scores:

            merged.overall_confidence = round(
                sum(confidence_scores) /
                len(confidence_scores),
                1,
            )

        else:

            merged.overall_confidence = 1.0

        return merged