from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, timezone
from uuid import UUID
class Message(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    sender_id: UUID = Field(description="The unique identifier of the user who sent the message")
    recipent_id: UUID = Field(description="The unique identifier of the user who is the recipient of the message")
    post_id: UUID = Field(description="The unique identifier of the post to which the message belongs")
    message: str = Field(description="The content of the message")
    sent_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Timestamp of when the message was sent")

