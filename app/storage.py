import json
import os
import sqlite3
from typing import Any


class LocalStorage:
    def __init__(self, path: str):
        self.path = path
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY,
                filename TEXT NOT NULL,
                document_type TEXT,
                vendor TEXT,
                currency TEXT,
                amount REAL,
                date TEXT,
                items TEXT,
                raw_response TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.conn.commit()

    def save_job(self, job_id: str, filename: str, result: dict[str, Any]) -> dict[str, Any]:
        items_json = json.dumps(result.get("items", []))
        raw_response = json.dumps(result.get("raw_response", {}))
        self.conn.execute(
            """
            INSERT INTO jobs (id, filename, document_type, vendor, currency, amount, date, items, raw_response)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                job_id,
                filename,
                result.get("document_type"),
                result.get("vendor"),
                result.get("currency"),
                result.get("amount"),
                result.get("date"),
                items_json,
                raw_response,
            ),
        )
        self.conn.commit()
        return self.get_job(job_id)

    def get_job(self, job_id: str) -> dict[str, Any]:
        row = self.conn.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
        if row is None:
            return {}
        return dict(row)

    def list_jobs(self) -> list[dict[str, Any]]:
        rows = self.conn.execute("SELECT * FROM jobs ORDER BY created_at DESC").fetchall()
        return [dict(row) for row in rows]
