from fastapi import APIRouter

from app.schemas.schemas import UserLogin, UserRegister
from app.services.user_service import get_user_profile, login_user, register_user

router = APIRouter()


@router.post("/register")
def register(payload: UserRegister):
    return register_user(payload.model_dump())


@router.post("/login")
def login(payload: UserLogin):
    return login_user(payload.model_dump())


@router.get("/me")
def get_profile(email: str):
    return get_user_profile(email)
