from sqlalchemy import MetaData, create_engine
from config import Settings, settings
metadata = MetaData()
engine = create_engine(f"postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}")


