from fastapi import APIRouter

router = APIRouter()

@router.get("/balance")
def get_balance():
    return {"pontos": 120, "saldo": 12.40}

@router.get("/history")
def get_history():
    return [{"id": 1, "tipo": "resposta", "pontos": 20, "descricao": "Participação em pesquisa"}]
