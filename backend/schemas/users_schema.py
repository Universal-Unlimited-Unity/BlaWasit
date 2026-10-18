from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
from datetime import datetime, timezone
from .posts_schema import VerificationStatus

class User(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    legal_papers_url_PDF: str | None = None
    first_name: str
    last_name: str
    email: EmailStr
    verified: bool = False
    verified_at: datetime | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    verification_status: str = VerificationStatus.pending
    updated_at: datetime | None = None
    image_url: str | None = None
    bio: str | None = None

class Group(BaseModel):
    group_id: UUID = Field(default_factory=uuid4)
    admin_id: UUID

class Group_Members(BaseModel):
    group_id: UUID
    user_id: UUID    