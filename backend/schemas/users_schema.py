from pydantic import BaseModel, ConfigDict, Field, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from uuid import UUID, uuid4
from datetime import datetime, timezone
from .posts_schema import VerificationStatus

class User(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    user_id: UUID = Field(default_factory=uuid4, description="Auto generated unique identifier for the user")
    legal_papers_url_PDF: str | None = Field(default=None, 
                                             description="URL to the user's legal papers in PDF format, if provided") 
    first_name: str = Field(description="The user's first name")
    last_name: str = Field(description="The user's last name")
    email: EmailStr = Field(description="The user's email address, must be a valid email format")
    phone_number: PhoneNumber = Field(description="The user's phone number, must be a valid phone number format")
    verified: bool = Field(default=False, description="Indicates whether the user's legal identification has been verified")
    verified_at: datetime | None = Field(default=None, description="Timestamp of when the user's legal identification was verified, if applicable")
    rejected_at: datetime | None = Field(default=None, description="Timestamp of when the user's legal identification was rejected, if applicable")
    rejection_reason: str | None = Field(default=None, description="The reason for rejection of the user's legal identification, if applicable")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Timestamp of when the user was created")
    verification_status: str = Field(default=VerificationStatus.pending.value, description="The current verification status of the user, can be 'pending', 'rejected', or 'accepted'")
    updated_at: datetime | None = Field(default=None, description="Timestamp of when the user was last updated")
    image_url: str | None = Field(default=None, description="URL to the user's profile image, if provided")
    bio: str | None = Field(default=None, description="A brief biography of the user, if provided")
    add_to_group: bool = Field(default=False, description="Indicates whether the user can be added to a group")

class Group(BaseModel):
    group_id: UUID = Field(default_factory=uuid4, description="Auto generated unique identifier for the group")
    admin_id: UUID = Field(description="The unique identifier of the user who is the admin of the group")

class Group_Members(BaseModel):
    group_id: UUID = Field(description="The unique identifier of the group")
    user_id: UUID = Field(description="The unique identifier of the user who is a member of the group")
    