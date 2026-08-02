from sqlalchemy.orm import Session

from app.database.connection import engine
from app.database.models import Company
from app.services.db_service import add_campaign, add_company, create_all_tables


def ensure_schema() -> None:
    create_all_tables()


def create_company(payload: dict) -> dict:
    ensure_schema()
    with Session(engine) as session:
        company = add_company(session, payload)
        return {"message": "Empresa cadastrada", "company": {"id": company.id, "nome": company.nome, "email": company.email}}


def create_campaign(company_id: int, payload: dict) -> dict:
    ensure_schema()
    with Session(engine) as session:
        company = session.query(Company).filter(Company.id == company_id).first()
        if not company:
            return {"message": "Empresa não encontrada"}

        campaign = add_campaign(session, company.id, payload)
        return {"message": f"Campanha criada para empresa {company_id}", "campaign": {"id": campaign.id, "company_id": campaign.company_id, "titulo": campaign.titulo, "orcamento": campaign.orcamento}}
