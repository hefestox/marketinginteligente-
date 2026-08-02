import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

print("[connection.py] Initializing database connection...")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./market_intelligence.db"
    print(
        "[connection.py] DATABASE_URL environment variable is not set. "
        "Using local SQLite fallback for development."
    )

print("[connection.py] DATABASE_URL found, creating engine...")

Base = declarative_base()

try:
    connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
    engine = create_engine(DATABASE_URL, connect_args=connect_args)
    print("[connection.py] Database engine created successfully.")
except Exception as exc:
    print(f"[connection.py] ERROR: Failed to create database engine: {exc}")
    sys.exit(1)
