from fastapi import APIRouter

from app.schemas.schemas import CampaignCreate, CompanyCreate
from app.services.company_service import create_campaign, create_company

router = APIRouter()


@router.post("/")
def create(payload: CompanyCreate):
    return create_company(payload.model_dump())


@router.post("/{company_id}/campaigns")
def new_campaign(company_id: int, payload: CampaignCreate):
    return create_campaign(company_id, payload.model_dump())


@router.post("/{company_id}/reports")
def buy_report(company_id: int):
    return {"message": f"Relatório adquirido pela empresa {company_id}"}
