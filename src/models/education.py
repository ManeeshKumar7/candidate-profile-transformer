from typing import Optional

from pydantic import BaseModel

from .common import FieldMetadata


class Education(BaseModel):
    institution: Optional[str] = None
    degree: Optional[str] = None
    field: Optional[str] = None
    start_year: Optional[int] = None
    end_year: Optional[int] = None
    metadata: Optional[FieldMetadata] = None