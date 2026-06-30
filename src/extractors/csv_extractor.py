from uuid import uuid4

import pandas as pd

from src.models.candidate import Candidate
from src.models.common import (
    Email,
    ExtractionMethod,
    FieldMetadata,
    Phone,
    SourceType,
)


class CSVExtractor:
    """
    Extracts candidate information from a recruiter CSV.
    """

    def extract(self, dataframe: pd.DataFrame) -> Candidate:

        row = dataframe.iloc[0]

        candidate = Candidate()

        candidate.candidate_id = str(uuid4())

        candidate.full_name = row.get("Name")

        candidate.headline = row.get("Headline")

        candidate.years_experience = (
            float(row["YearsExperience"])
            if pd.notna(row.get("YearsExperience"))
            else None
        )

        if pd.notna(row.get("Email")):

            candidate.emails.append(
                Email(
                    value=row["Email"],
                    metadata=FieldMetadata(
                        sources=[SourceType.RECRUITER_CSV],
                        confidence=0.95,
                        extraction_method=ExtractionMethod.CSV,
                    ),
                )
            )

        if pd.notna(row.get("Phone")):

            candidate.phones.append(
                Phone(
                    value=str(row["Phone"]),
                    metadata=FieldMetadata(
                        sources=[SourceType.RECRUITER_CSV],
                        confidence=0.95,
                        extraction_method=ExtractionMethod.CSV,
                    ),
                )
            )

        return candidate