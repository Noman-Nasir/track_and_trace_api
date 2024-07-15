"""
Helper functions related to database connection in fastapi
"""
from db.database import SessionLocal


def db_session():
    """
    Returns a database session object
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
