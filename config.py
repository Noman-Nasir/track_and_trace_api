"""
Project config file
"""
import os

from dotenv import load_dotenv

load_dotenv()


def get_meteomatics_credentials() -> (str, str):
    """
    Returns meteomatics credentials from environment file
    """
    username = os.getenv("METEOMATICS_USERNAME")
    password = os.getenv("METEOMATICS_PASSWORD")
    return username, password


def get_orders_db_url() -> str:
    """
    Returns postgres orders db url constructed from creds from environment file
    """
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASS")
    host = os.getenv("POSTGRES_HOST")
    dbname = os.getenv("POSTGRES_DB")
    return f"postgresql://{user}:{password}@{host}/{dbname}"
