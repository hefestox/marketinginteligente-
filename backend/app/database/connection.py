import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

load_dotenv()

logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    logger.error(
        "DATABASE_URL environment variable is not set. "
        "Set it in the Railway service variables to connect to PostgreSQL."
    )
    raise RuntimeError("DATABASE_URL environment variable is not set")

Base = declarative_base()

try:
    engine = create_engine(DATABASE_URL)
except Exception:
    logger.exception("Failed to create database engine with the provided DATABASE_URL")
    raise
