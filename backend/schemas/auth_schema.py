from pydantic import BaseModel

class GoogleAuthPayload(BaseModel):
    toeken: str