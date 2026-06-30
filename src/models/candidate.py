from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from .common import Email, Links, Location, Phone, Skill
from .education import Education
from .employment import Experience


class Candidate(BaseModel):

    model_config = ConfigDict(validate_assignment=True)

    candidate_id: Optional[str] = None

    full_name: Optional[str] = None

    headline: Optional[str] = None

    emails: List[Email] = Field(default_factory=list)

    phones: List[Phone] = Field(default_factory=list)

    skills: List[Skill] = Field(default_factory=list)

    experience: List[Experience] = Field(default_factory=list)

    education: List[Education] = Field(default_factory=list)

    location: Optional[Location] = None

    links: Optional[Links] = None

    years_experience: Optional[float] = None

    overall_confidence: float = 1.0