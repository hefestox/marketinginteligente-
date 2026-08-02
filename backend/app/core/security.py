import os
from datetime import datetime, timedelta
from hashlib import pbkdf2_hmac
from typing import Any

import jwt

SECRET_KEY = os.getenv("JWT_SECRET", "market-intelligence-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24


def hash_password(password: str) -> str:
    salt = b"market-intelligence-salt"
    digest = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
    return digest.hex()


def verify_password(password: str, password_hash: str) -> bool:
    return hash_password(password) == password_hash


def create_access_token(subject: str | Any, expires_delta: timedelta | None = None) -> str:
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    expire = datetime.utcnow() + expires_delta
    to_encode = {"sub": str(subject), "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
