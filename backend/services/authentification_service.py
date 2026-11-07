from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy import insert, select
from DB_CONFIG import engine
from google.oauth2 import id_token
from google.auth.transport import requests
from config import settings
from schemas.users_schema import User
from fastapi import HTTPException
from DB_CONFIG import engine
from models.users_model import users_table
from models.oath_accounts import oath_accounts_table
import jwt


GOOGLE_CLIENT_ID = settings.GOOGLE_CLIENT_ID

def get_user_by_email(email: str):
    with engine.begin() as conn:
        query = select(users_table).where(users_table.c.email == email)
        result = conn.execute(query).first()
        return result
 
def generate_token(email: str):
    with engine.begin() as conn:
        stmt = select(users_table).where(users_table.c.email == email)
        result = conn.execute(stmt).first()
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        payload = {
            "user_id": result.id,
            "email": result.email,
            "exp": settings.TOKEN_EXPIRATION_MINUTES
        }
        token = jwt.encode(payload, settings.TOKEN_SECRET_KEY, settings.TOKEN_ALGORITHM)
        return token

def google_auth(token: str):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        if not idinfo.get("email_verified"):
            raise HTTPException(status_code=400, detail="Email not verified by Google")
        payload = User(first_name=str(idinfo.get("given_name")), 
                    last_name=str(idinfo.get("family_name")), 
                    email=str(idinfo.get("email")), 
                    email_verified=bool(idinfo.get("email_verified")))
        user = get_user_by_email(payload.email)
        if user:
            with engine.begin() as conn:
                query = select(oath_accounts_table).where(oath_accounts_table.c.provider_user_id == idinfo.get("sub"), oath_accounts_table.c.provider == "google")
                result = conn.execute(query).first()
                if not result:
                    query = insert(oath_accounts_table).values({
                        "id": str(uuid4()),
                        "user_id": user.user_id,
                        "provider": "google",
                        "provider_user_id": idinfo.get("sub"),
                        "created_at": datetime.now(timezone.utc)
                    })
                    conn.execute(query)
            return generate_token(payload.email)
        else:
            with engine.begin() as conn:
                query = insert(users_table).values(payload.model_dump()).returning(users_table.c.user_id) 
                user_id = conn.execute(query).scalar_one()
                query = insert(oath_accounts_table).values({
                    "id": str(uuid4()),
                    "user_id": user_id,
                    "provider": "google",
                    "provider_user_id": idinfo.get("sub"),
                    "created_at": datetime.now(timezone.utc)
                })
                conn.execute(query)
            return generate_token(payload.email)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid token")
            