from src.models.candidate import Candidate
from src.models.common import (
    Email,
    ExtractionMethod,
    FieldMetadata,
    Links,
    Phone,
    Skill,
    SourceType,
)
from src.utils.patterns import (
    EMAIL_PATTERN,
    GITHUB_PATTERN,
    LINKEDIN_PATTERN,
    PHONE_PATTERN,
)
from src.utils.section_parser import SectionParser
from src.utils.text_utils import clean_text


class ResumeExtractor:
    """
    Extracts candidate information from resume text.
    """

    def __init__(self):

        self.section_parser = SectionParser()

    def extract(self, resume_text: str) -> Candidate:

        resume_text = clean_text(resume_text)

        sections = self.section_parser.parse(resume_text)

        candidate = Candidate()

        # -----------------------------
        # Emails
        # -----------------------------

        for email in set(EMAIL_PATTERN.findall(resume_text)):

            candidate.emails.append(
                Email(
                    value=email,
                    metadata=FieldMetadata(
                        sources=[SourceType.RESUME],
                        confidence=0.90,
                        extraction_method=ExtractionMethod.REGEX,
                    ),
                )
            )

        # -----------------------------
        # Phones
        # -----------------------------

        for phone in set(PHONE_PATTERN.findall(resume_text)):

            candidate.phones.append(
                Phone(
                    value=phone,
                    metadata=FieldMetadata(
                        sources=[SourceType.RESUME],
                        confidence=0.90,
                        extraction_method=ExtractionMethod.REGEX,
                    ),
                )
            )

        # -----------------------------
        # Skills
        # -----------------------------

        skills_section = sections.get("skills", "")

        skills = []

        for line in skills_section.split("\n"):

            line = line.strip()

            if not line:
                continue

            if "," in line:

                skills.extend(
                    [skill.strip() for skill in line.split(",")]
                )

            else:

                skills.append(line)

        for skill in skills:

            if skill:

                candidate.skills.append(
                    Skill(
                        name=skill,
                        metadata=FieldMetadata(
                            sources=[SourceType.RESUME],
                            confidence=0.85,
                            extraction_method=ExtractionMethod.PDF,
                        ),
                    )
                )

        # -----------------------------
        # Links
        # -----------------------------

        linkedin = LINKEDIN_PATTERN.findall(resume_text)

        github = GITHUB_PATTERN.findall(resume_text)

        if linkedin or github:

            candidate.links = Links(
                linkedin=linkedin[0] if linkedin else None,
                github=github[0] if github else None,
            )

        return candidate