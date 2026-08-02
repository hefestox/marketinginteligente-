from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.users import router as users_router
from app.routes.surveys import router as surveys_router
from app.routes.rewards import router as rewards_router
from app.routes.companies import router as companies_router
from app.routes.analytics import router as analytics_router

app = FastAPI(title="Market Intelligence MVP", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(surveys_router, prefix="/surveys", tags=["Surveys"])
app.include_router(rewards_router, prefix="/rewards", tags=["Rewards"])
app.include_router(companies_router, prefix="/companies", tags=["Companies"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])

@app.get("/")
def health_check():
    return {"message": "Market Intelligence API is running"}
