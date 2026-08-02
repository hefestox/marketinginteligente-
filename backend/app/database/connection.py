import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

print("[connection.py] Initializing database connection...")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print(
        "[connection.py] ERROR: DATABASE_URL environment variable is not set. "
        "Set it in the Railway service variables to connect to PostgreSQL."
    )
    sys.exit(1)

print("[connection.py] DATABASE_URL found, creating engine...")

Base = declarative_base()

try:
    engine = create_engine(DATABASE_URL)
    print("[connection.py] Database engine created successfully.")
except Exception as exc:
    print(f"[connection.py] ERROR: Failed to create database engine: {exc}")
    sys.exit(1)
