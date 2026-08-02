from sqlalchemy.orm import Session

from app.database.connection import engine
from app.database.models import Answer, Survey, User
from app.services.db_service import add_answer, add_reward, add_survey, create_all_tables, list_surveys as list_db_surveys


def ensure_schema() -> None:
    create_all_tables()


def create_survey(payload: dict) -> dict:
    ensure_schema()
    with Session(engine) as session:
        survey = add_survey(session, payload)
        return {"message": "Pesquisa criada", "survey": {"id": survey.id, "titulo": survey.titulo, "descricao": survey.descricao}}


def list_surveys() -> list[dict]:
    ensure_schema()
    with Session(engine) as session:
        surveys = list_db_surveys(session)
        return [{"id": survey.id, "titulo": survey.titulo, "descricao": survey.descricao} for survey in surveys]


def submit_answer(survey_id: int, payload: dict) -> dict:
    ensure_schema()
    with Session(engine) as session:
        survey = session.query(Survey).filter(Survey.id == survey_id).first()
        if not survey:
            return {"message": "Pesquisa não encontrada"}

        user = session.query(User).first()
        if not user:
            return {"message": "Usuário não encontrado"}

        answer = add_answer(session, user.id, survey.id, payload)
        add_reward(session, user.id, 20, 2.0, f"Resposta registrada na pesquisa {survey_id}")
        return {"message": f"Resposta registrada para pesquisa {survey_id}", "answer": {"id": answer.id, "survey_id": survey_id, "resposta": answer.resposta}}
