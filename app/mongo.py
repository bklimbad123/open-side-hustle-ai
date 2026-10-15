from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class MongoStorage:
    """Optional MongoDB-backed job storage with the LocalStorage contract."""

    def __init__(
        self,
        uri: str,
        database: str = "receiptlens",
        collection: str = "jobs",
    ) -> None:
        if not uri:
            raise ValueError("A MongoDB connection URI is required")

        from pymongo import MongoClient

        self.client = MongoClient(uri)
        self.jobs = self.client[database][collection]

    def save_job(
        self, job_id: str, filename: str, result: dict[str, Any]
    ) -> dict[str, Any]:
        document = {
            "_id": job_id,
            "id": job_id,
            "filename": filename,
            "document_type": result.get("document_type"),
            "vendor": result.get("vendor"),
            "currency": result.get("currency"),
            "amount": result.get("amount"),
            "date": result.get("date"),
            "items": result.get("items", []),
            "raw_response": result.get("raw_response", {}),
            "created_at": datetime.now(timezone.utc),
        }
        self.jobs.insert_one(document)
        return self.get_job(job_id)

    def get_job(self, job_id: str) -> dict[str, Any]:
        document = self.jobs.find_one({"_id": job_id})
        if document is None:
            return {}
        document.pop("_id", None)
        return document

    def list_jobs(self) -> list[dict[str, Any]]:
        documents = self.jobs.find().sort("created_at", -1)
        jobs = []
        for document in documents:
            document.pop("_id", None)
            jobs.append(document)
        return jobs