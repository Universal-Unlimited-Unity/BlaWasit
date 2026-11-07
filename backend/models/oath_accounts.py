from sqlalchemy import Table, Column, String, ForeignKey, UUID, DateTime, Index
from DB_CONFIG import metadata

oath_accounts_table = Table(
    "oath_accounts",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True),
    Column("provider", String, primary_key=True),
    Column("provider_user_id", String, primary_key=True),
    Column("created_at", DateTime(timezone=True), nullable=False),
    Index("user_id_provider_idx", "user_id", "provider")
)