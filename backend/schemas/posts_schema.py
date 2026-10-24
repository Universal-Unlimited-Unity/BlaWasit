from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ConfigDict


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
    user_id: UUID = Field(description="The unique identifier of the user who created the post")
    post_id: UUID = Field(default_factory=uuid4, description="Auto generated unique identifier for the post")
    imags_url: str = Field(description="URL to the folder that contains the images of the post")
    title: str = Field(description="The title of the post")
    legal_papers_url_PDF: str | None = Field(default=None, description="URL to the legal papers of the post in PDF format, if provided")
    size_m2: float = Field(description="The size of the property in square meters")
    property_type: PropertyType = Field(description="The type of the property, can be 'room', 'house', 'apartment', or 'studio'")
    accept_multiple_renters: bool = Field(default=False, description="Indicates whether the property can accept multiple renters")
    boys_only: bool = Field(default=False, description="Indicates whether the property is for boys only")
    girls_only: bool = Field(default=False, description="Indicates whether the property is for girls only")
    families_only: bool = Field(default=False, description="Indicates whether the property is for families only")
    accept_smokers: bool = Field(default=False, description="Indicates whether the property accepts smokers")
    wifi: bool = Field(default=False, description="Indicates whether the property has Wi-Fi")
    ac: bool = Field(default=False, description="Indicates whether the property has air conditioning")
    heating: bool = Field(default=False, description="Indicates whether the property has heating")
    boiler: bool = Field(default=False, description="Indicates whether the property has a boiler")
    fridge: bool = Field(default=False, description="Indicates whether the property has a fridge")
    stove: bool = Field(default=False, description="Indicates whether the property has a stove")
    tv: bool = Field(default=False, description="Indicates whether the property has a TV")
    max_renters: int | None = Field(default=None, description="The maximum number of renters allowed for the property, if applicable")
    monthly_rent: Decimal = Field(description="The monthly rent for the property")
    security_deposit: Decimal = Field(default=Decimal("0"), description="The security deposit for the property")
    agency_fee: Decimal = Field(default=Decimal("0"), description="The agency fee for the property")
    utilities_included: bool = Field(default=False, description="Indicates whether utilities are included in the rent")
    utilities_estimated_cost: Decimal | None = Field(default=None, description="The estimated cost of utilities per month, if applicable")
    negotiable: bool = Field(default=False, description="Indicates whether the rent is negotiable")
    bedrooms: int = Field(description="The number of bedrooms in the property")
    bathrooms: int = Field(description="The number of bathrooms in the property")
    furnished: bool = Field(default=False, description="Indicates whether the property is furnished")
    floor: int | None = Field(default=None, description="The floor number of the property, if applicable")
    available_from: date = Field(description="The date from which the property is available for rent")
    minimum_stay_months: int | None = Field(default=None, description="The minimum number of months a tenant must stay, if applicable")
    verification_status: VerificationStatus = Field(default=VerificationStatus.pending, description="The current verification status of the post, can be 'pending', 'rejected', or 'accepted'")
    verified_at: datetime | None = Field(default=None, description="Timestamp of when the post was verified, if applicable")
    rejected_at: datetime | None = Field(default=None, description="Timestamp of when the post was rejected, if applicable")
    rejection_reason: str | None = Field(default=None, description="The reason for rejection of the post, if applicable")
    last_confirmed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Timestamp of when the post was last confirmed to be valid") 
    expires_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc) + timedelta(days=7), description="Timestamp of when the post will expire, default is 7 days from creation")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Timestamp of when the post was created")
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Timestamp of when the post was last updated")
    

class PostPriceHistory(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    post_id: UUID = Field(description="The unique identifier of the post")
    price: Decimal = Field(description="The price of the post at the time of the history record")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Timestamp of when the price history was created")
