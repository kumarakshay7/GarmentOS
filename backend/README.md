# GarmentOS Backend

FastAPI REST API for GarmentOS.

## Run locally

From the `backend` directory:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` for the interactive API documentation.

## Environment

Copy `.env.example` to `.env` and set `DATABASE_URL` for your local PostgreSQL database. Never commit `.env`.
