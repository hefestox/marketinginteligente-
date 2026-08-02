from fastapi import APIRouter

from app.schemas.schemas import AnswerCreate, SurveyCreate
from app.services.survey_service import create_survey, list_surveys, submit_answer

router = APIRouter()


@router.get("/")
def get_surveys():
    return list_surveys()


@router.post("/")
def create(payload: SurveyCreate):
    return create_survey(payload.model_dump())


@router.post("/{survey_id}/answers")
def submit(survey_id: int, payload: AnswerCreate):
    return submit_answer(survey_id, payload.model_dump())
