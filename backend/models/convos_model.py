from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table, Index
from sqlalchemy.dialects.postgresql import UUID
from DB_CONFIG import metadata
from .users_model import users_table
from .posts_model import posts_table

messages_table = Table(
    "messages",
    metadata,
    Column("message_id", UUID(as_uuid=True), primary_key=True),
    Column("sender_id", UUID(as_uuid=True), ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False, index=True),
    Column("recipent_id", UUID(as_uuid=True), ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False, index=True),
    Column("post_id", UUID(as_uuid=True), ForeignKey("posts.post_id", ondelete="CASCADE"), nullable=False, index=True),
    Column("message", String, nullable=False),
    Column("sent_at", DateTime(timezone=True), nullable=False, index=True),
    Index("sender_recipient_post_idx", "sender_id", "recipent_id", "post_id"),
    Index("recipient_post_idx", "recipent_id", "sender_id"),
    Index("post_recipient_idx", "post_id", "recipent_id"),
    Index("post_sender_idx", "post_id", "sender_id"),
)
