from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from app.core.settings import settings


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)


engine = create_engine(
    DATABASE_URL,
    echo=True,
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


try:
    with engine.connect() as connection:
        print("Database connected successfully!")
except Exception as e:
    print(f"Database connection failed: {e}")