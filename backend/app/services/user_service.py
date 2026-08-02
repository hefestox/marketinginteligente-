from typing import Dict

from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.database.connection import engine
from app.database.models import User
from app.services.db_service import add_user, create_all_tables, get_user_by_email

USERS_DB: Dict[str, Dict[str, object]] = {}


def ensure_schema() -> None:
    create_all_tables()


def register_user(payload: dict) -> dict:
    ensure_schema()
    email = payload["email"]

    with Session(engine) as session:
        existing = get_user_by_email(session, email)
        if existing:
            return {"message": "Email já cadastrado"}

        user_payload = {
            **payload,
            "senha": hash_password(payload["senha"]),
        }
        add_user(session, user_payload)

    return {
        "message": "Usuário cadastrado com sucesso",
        "email": email,
    }


def login_user(payload: dict) -> dict:
    ensure_schema()
    with Session(engine) as session:
        user = get_user_by_email(session, payload["email"])
        if not user:
            return {"message": "Credenciais inválidas"}

        if not verify_password(payload["senha"], user.senha):
            return {"message": "Credenciais inválidas"}

        token = create_access_token(str(user.email))
        return {
            "message": "Login realizado com sucesso",
            "access_token": token,
            "token_type": "bearer",
        }


def get_user_profile(email: str) -> dict:
    ensure_schema()
    with Session(engine) as session:
        user = get_user_by_email(session, email)
        if not user:
            return {"message": "Usuário não encontrado"}

        return {
            "nome": user.nome,
            "email": user.email,
            "idade": user.idade,
            "sexo": user.sexo,
            "cidade": user.cidade,
            "aceitou_lgpd": user.aceitou_lgpd,
        }
