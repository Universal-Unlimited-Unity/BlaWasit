from pydantic import BaseModel

class GoogleAuthPayload(BaseModel):
    token: str

class NormalAuthPayload(BaseModel):
    email: str
    password: str