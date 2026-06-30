from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl


class SourceType(str, Enum):
    RECRUITER_CSV = "recruiter_csv"
    RESUME = "resume"


class ExtractionMethod(str, Enum):
    CSV = "csv"
    PDF = "pdf"
    REGEX = "regex"
    INFERRED = "inferred"


class FieldMetadata(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    sources: List[SourceType] = Field(default_factory=list)
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    extraction_method: ExtractionMethod


class Email(BaseModel):
    value: EmailStr
    metadata: FieldMetadata


class Phone(BaseModel):
    value: str
    metadata: FieldMetadata


class Skill(BaseModel):
    name: str
    metadata: FieldMetadata


class Location(BaseModel):
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None


class Links(BaseModel):
    linkedin: Optional[HttpUrl] = None
    github: Optional[HttpUrl] = None
    portfolio: Optional[HttpUrl] = None