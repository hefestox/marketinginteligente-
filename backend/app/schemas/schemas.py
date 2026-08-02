from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    idade: int | None = None
    sexo: str | None = None
    cidade: str | None = None
    aceitou_lgpd: bool = False


class UserLogin(BaseModel):
    email: EmailStr
    senha: str


class SurveyCreate(BaseModel):
    titulo: str
    descricao: str | None = None


class AnswerCreate(BaseModel):
    resposta: str


class CompanyCreate(BaseModel):
    nome: str
    email: EmailStr


class CampaignCreate(BaseModel):
    titulo: str
    orcamento: float


class RewardCreate(BaseModel):
    pontos: int
