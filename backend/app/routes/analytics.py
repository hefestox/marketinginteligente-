from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return {
        "total_usuarios": 1280,
        "taxa_resposta": 0.74,
        "segmentos": ["Tech", "Financeiro", "Varejo"],
    }

@router.get("/trends")
def trends():
    return {"trend": "Crescimento de interesse em IA para atendimento"}
