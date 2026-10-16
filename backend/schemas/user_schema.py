
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ConfigDict, EmailStr


class PropertyType(str, Enum):
    room = "room"
    house = "house"
    apartment = "apartment"
    studio = "studio"


class VerificationStatus(str, Enum):
    pending = "pending"
    rejected = "rejected"
    accepted = "accepted"


class Post(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    user_id: UUID
    post_id: UUID = Field(default_factory=uuid4)
    imags_url: str | None = None
    title: str
    legal_papers_url_PDF: str | None = None
    size_m2: float
    property_type: PropertyType
    accept_multiple_renters: bool = False
    boys_only: bool = False
    girls_only: bool = False
    families_only: bool = False
    accpet_smokers: bool = False
    wifi: bool = False
    ac: bool = False
    boiler: bool = False
    fridge: bool = False
    stove: bool = False
    tv: bool = False
    max_renters: int | None = None
    monthly_rent: Decimal
    security_deposit: Decimal = Decimal("0")
    agency_fee: Decimal = Decimal("0")
    utilities_included: bool = False
    utilities_estimated_cost: Decimal | None = None
    negotiable: bool = False
    bedrooms: int
    bathrooms: int
    furnished: bool = False
    floor: int | None = None
    available_from: date
    minimum_stay_months: int | None = None
    verification_status: VerificationStatus = VerificationStatus.pending
    verified_at: datetime | None = None
    last_confirmed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    expires_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc) + timedelta(days=7))
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class User(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    legal_papers_url_PDF: str | None = None
    first_name: str
    last_name: str
    email: EmailStr
    verified: bool = False
    image_url: str | None = None
    bio: str | None = None
    