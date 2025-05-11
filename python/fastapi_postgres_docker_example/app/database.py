from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Read the DB URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy engine & session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
