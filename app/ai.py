import base64
import json
from typing import Any

import requests

from app.config import settings


class LocalAIExtractor:
    def __init__(self, base_url: str | None = None, model: str | None = None):
        self.base_url = (base_url or settings.ollama_base_url).rstrip("/")
        self.model = model or settings.ollama_model

    def is_model_available(self) -> bool:
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=10)
            response.raise_for_status()
            payload = response.json()
            models = [item.get("name") for item in payload.get("models", [])]
            return self.model in models or any(model.startswith(self.model) for model in models)
        except Exception:
            return False

    def _fallback_result(self, filename: str) -> dict[str, Any]:
        return {
            "document_type": "receipt",
            "vendor": "Unknown vendor",
            "currency": "USD",
            "amount": 0.0,
            "date": "",
            "items": [],
            "raw_response": {
                "source": "fallback",
                "filename": filename,
                "confidence": "low",
            },
        }

    def extract(self, file_bytes: bytes, filename: str) -> dict[str, Any]:
        if not self.is_model_available():
            return self._fallback_result(filename)

        prompt = (
            "You are extracting a receipt or invoice from a document image. "
            "Return strict JSON with these keys only: "
            "document_type, vendor, currency, amount, date, items, raw_response. "
            "document_type must be invoice or receipt. "
            "amount is a number. "
            "items is an array of objects with description and amount. "
            "raw_response can include confidence and notes. "
            "Do not include markdown fences."
        )

        encoded = base64.b64encode(file_bytes).decode("utf-8")
        payload = {
            "model": self.model,
            "prompt": prompt,
            "images": [encoded],
            "stream": False,
            "options": {"temperature": 0.1},
        }

        try:
            response = requests.post(f"{self.base_url}/api/generate", json=payload, timeout=120)
            response.raise_for_status()
            body = response.json()
            text = body.get("response", "")
            parsed = json.loads(text)
            if not isinstance(parsed, dict):
                raise ValueError("response is not JSON object")
            parsed.setdefault("raw_response", {"confidence": "medium"})
            parsed.setdefault("items", [])
            parsed.setdefault("document_type", "receipt")
            parsed.setdefault("currency", "USD")
            return parsed
        except Exception:
            return self._fallback_result(filename)
