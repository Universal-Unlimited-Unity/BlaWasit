from sqlalchemy import Table, Column, String, Boolean, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID
from DB_CONFIG import metadata

users_table = Table(
    "users",
    metadata,
    Column("user_id", UUID(as_uuid=True), primary_key=True),
    Column("legal_papers_url_PDF", String, nullable=True),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("verified", Boolean, nullable=False),
    Column("verified_at", DateTime(timezone=True), nullable=True),
    Column("verification_status", String, nullable=False),
    Column("image_url", String, nullable=True),
    Column("bio", String, nullable=True),
    Column("created_at", DateTime(timezone=True), nullable=False),
    Column("updated_at", DateTime(timezone=True), nullable=True),
    Column("add_to_group", Boolean, nullable=False),
    Column("rejected_at", DateTime(timezone=True), nullable=True),
    Column("rejection_reason", String, nullable=True),
)


groups_table = Table(
    "groups",
    metadata,
    Column("group_id", UUID(as_uuid=True), primary_key=True),
    Column("admin_id", UUID(as_uuid=True), ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False, index=True),
    Index("grp_id_admin_id", "group_id", "admin_id")
)


group_members_table = Table(
    "group_members",
    metadata,
    Column("group_id", UUID(as_uuid=True), ForeignKey("groups.group_id", ondelete="CASCADE"), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True),
    Index("grp_id_user_id", "group_id", "user_id")
)
