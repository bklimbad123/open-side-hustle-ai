import uuid
from typing import Any

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse

from app.ai import LocalAIExtractor
from app.config import settings
from app.observability import initialize_sentry
from app.storage import LocalStorage

initialize_sentry(settings.sentry_dsn)

app = FastAPI(title=settings.app_name, version="0.1.0")
extractor = LocalAIExtractor()
storage = LocalStorage(settings.storage_path)


@app.get("/")
def home() -> dict[str, Any]:
    return {
        "app": settings.app_name,
        "description": "Local-first invoice and receipt sorter powered by an open-weight model.",
        "model": settings.ollama_model,
        "storage_path": settings.storage_path,
    }


@app.get("/health")
def health() -> dict[str, Any]:
    availability = extractor.is_model_available()
    return {"status": "ok", "ollama_available": availability, "model": settings.ollama_model}


@app.post("/extract")
async def extract_invoice(file: UploadFile = File(...)) -> JSONResponse:
    if not file.filename:
        raise HTTPException(status_code=400, detail="A file is required")

    content = await file.read()
    result = extractor.extract(content, file.filename)
    job_id = str(uuid.uuid4())
    saved = storage.save_job(job_id, file.filename, result)

    response = {
        "job_id": job_id,
        "document_type": saved.get("document_type"),
        "vendor": saved.get("vendor"),
        "currency": saved.get("currency"),
        "amount": saved.get("amount"),
        "date": saved.get("date"),
        "items": saved.get("items"),
        "raw_response": saved.get("raw_response"),
    }
    return JSONResponse(content=response)


@app.get("/jobs")
def list_jobs() -> dict[str, Any]:
    return {"jobs": storage.list_jobs()}
