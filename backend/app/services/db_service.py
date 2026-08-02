from sqlalchemy.orm import Session

from app.database.connection import Base, engine
from app.database.models import Answer, Campaign, Company, Reward, Survey, User


def create_all_tables() -> None:
    Base.metadata.create_all(bind=engine)


def add_user(session: Session, payload: dict) -> User:
    user = User(
        nome=payload["nome"],
        email=payload["email"],
        senha=payload["senha"],
        idade=payload.get("idade"),
        sexo=payload.get("sexo"),
        cidade=payload.get("cidade"),
        aceitou_lgpd=payload.get("aceitou_lgpd", False),
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user_by_email(session: Session, email: str) -> User | None:
    return session.query(User).filter(User.email == email).first()


def add_survey(session: Session, payload: dict) -> Survey:
    survey = Survey(titulo=payload["titulo"], descricao=payload.get("descricao"))
    session.add(survey)
    session.commit()
    session.refresh(survey)
    return survey


def list_surveys(session: Session) -> list[Survey]:
    return session.query(Survey).all()


def add_answer(session: Session, user_id: int, survey_id: int, payload: dict) -> Answer:
    answer = Answer(user_id=user_id, survey_id=survey_id, resposta=payload["resposta"])
    session.add(answer)
    session.commit()
    session.refresh(answer)
    return answer


def add_reward(session: Session, user_id: int, pontos: int, saldo: float, historico: str | None = None) -> Reward:
    reward = Reward(user_id=user_id, pontos=pontos, saldo=saldo, historico=historico)
    session.add(reward)
    session.commit()
    session.refresh(reward)
    return reward


def add_company(session: Session, payload: dict) -> Company:
    company = Company(nome=payload["nome"], email=payload["email"])
    session.add(company)
    session.commit()
    session.refresh(company)
    return company


def add_campaign(session: Session, company_id: int, payload: dict) -> Campaign:
    campaign = Campaign(company_id=company_id, titulo=payload["titulo"], orcamento=payload["orcamento"])
    session.add(campaign)
    session.commit()
    session.refresh(campaign)
    return campaign
