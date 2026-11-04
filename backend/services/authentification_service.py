from sqlalchemy import insert
from DB_CONFIG import engine
from models.users_model import users_table
from schemas.users_schema import User

def create_user(user: User):
    with engine.begin() as conn:
        stmt = insert(users_table).values(user.model_dump())
        conn.execute(stmt)