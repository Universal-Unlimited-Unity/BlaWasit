from sqlalchemy import (
    Table, Column, String, Float, Boolean, 
    Numeric, Integer, Date, DateTime, ForeignKey, Index
)
from sqlalchemy.dialects.postgresql import UUID
from DB_CONFIG import metadata
from .users_model import users_table

posts_table = Table(
    "posts",
    metadata,
    Column("post_id", UUID(as_uuid=True), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False, index=True),
    Column("imags_url", String, nullable=False),
    Column("title", String, nullable=False),
    Column("legal_papers_url_PDF", String, nullable=True),    
    Column("size_m2", Float, nullable=False),
    Column("property_type", String, nullable=False),
    Column("bedrooms", Integer, nullable=False),
    Column("bathrooms", Integer, nullable=False),
    Column("floor", Integer, nullable=True),
    Column("furnished", Boolean, nullable=False),
    Column("accept_multiple_renters", Boolean, nullable=False),
    Column("boys_only", Boolean, nullable=False),
    Column("girls_only", Boolean, nullable=False),
    Column("families_only", Boolean, nullable=False),
    Column("accept_smokers", Boolean, nullable=False),
    Column("wifi", Boolean, nullable=False),
    Column("ac", Boolean, nullable=False),
    Column("boiler", Boolean, nullable=False),
    Column("fridge", Boolean, nullable=False),
    Column("stove", Boolean, nullable=False),
    Column("tv", Boolean, nullable=False),
    Column("max_renters", Integer, nullable=True),
    Column("monthly_rent", Numeric(precision=10, scale=2), nullable=False),
    Column("security_deposit", Numeric(precision=10, scale=2), nullable=False),
    Column("agency_fee", Numeric(precision=10, scale=2), nullable=False),
    Column("utilities_included", Boolean, nullable=False),
    Column("utilities_estimated_cost", Numeric(precision=10, scale=2), nullable=True),
    Column("negotiable", Boolean, nullable=False),
    Column("available_from", Date, nullable=False),
    Column("minimum_stay_months", Integer, nullable=True),
    Column("verification_status", String, nullable=False),
    Column("verified_at", DateTime(timezone=True), nullable=True),
    Column("last_confirmed_at", DateTime(timezone=True), nullable=False),
    Column("expires_at", DateTime(timezone=True),  nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False),
    Column("updated_at", DateTime(timezone=True), nullable=False),
    Column("rejected_at", DateTime(timezone=True), nullable=True),
    Column("rejection_reason", String, nullable=True),
    Index("post_id_user_id_idx", "user_id", "post_id")
)

post_price_history_table = Table(
    "post_price_history",
    metadata,
    Column("post_id", UUID(as_uuid=True), ForeignKey("posts.post_id", ondelete="CASCADE"), primary_key=True),
    Column("price", Numeric(precision=10, scale=2), nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False),
    Index("post_time_idx", "created_at")
)
