# Market Intelligence MVP

## Stack
- Backend: FastAPI
- Database: PostgreSQL
- Frontend: React
- Deploy: Railway

## Project structure

```text
market-intelligence/
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── .env
├── frontend/
├── docker-compose.yml
└── README.md
```

## Run backend

```powershell
cd backend
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

## Run PostgreSQL locally

```powershell
docker compose up -d
```

## Railway

Set the following environment variables in Railway:
- `DATABASE_URL`
- `JWT_SECRET`

## Legal note

This MVP is based on aggregate and anonymized market intelligence and must respect user consent and LGPD compliance.
