from __future__ import annotations


def initialize_sentry(dsn: str | None = None) -> bool:
    """Initialize Sentry when a DSN is configured; otherwise do nothing."""
    if dsn is None:
        from app.config import settings

        dsn = settings.sentry_dsn

    if not dsn:
        return False

    import sentry_sdk

    sentry_sdk.init(dsn=dsn)
    return True