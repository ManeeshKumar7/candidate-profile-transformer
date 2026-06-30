from typing import Optional

from pydantic import BaseModel

from .common import FieldMetadata


class Experience(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[FieldMetadata] = None