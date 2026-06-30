from src.models.candidate import Candidate

from .phone_normalizer import PhoneNormalizer
from .skill_normalizer import SkillNormalizer


class CandidateNormalizer:
    """
    Applies all normalizations to a Candidate object.
    """

    def normalize(self, candidate: Candidate) -> Candidate:

        # -------------------------
        # Phone Numbers
        # -------------------------

        for phone in candidate.phones:

            phone.value = PhoneNormalizer.normalize(phone.value)

        # -------------------------
        # Skills
        # -------------------------

        for skill in candidate.skills:

            skill.name = SkillNormalizer.normalize(skill.name)

        # -------------------------
        # Remove duplicate skills
        # -------------------------

        unique = {}

        for skill in candidate.skills:

            unique[skill.name.lower()] = skill

        candidate.skills = list(unique.values())

        # -------------------------
        # Remove duplicate emails
        # -------------------------

        emails = {}

        for email in candidate.emails:

            emails[email.value.lower()] = email

        candidate.emails = list(emails.values())

        # -------------------------
        # Remove duplicate phones
        # -------------------------

        phones = {}

        for phone in candidate.phones:

            phones[phone.value] = phone

        candidate.phones = list(phones.values())

        return candidate