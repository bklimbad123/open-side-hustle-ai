from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "ReceiptLens"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "gemma3:4b"
    storage_path: str = "data/receipts.db"
    sentry_dsn: str = ""
    mongo_uri: str = ""


settings = Settings()
