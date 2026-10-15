# Sentry

Sentry initialization is opt-in through `SENTRY_DSN`. With an empty DSN,
`initialize_sentry` does nothing. When configured, the FastAPI module
initializes the Sentry SDK during startup/import.

Review event scrubbing and privacy settings before monitoring production
traffic so receipt contents and personal data are not unintentionally sent.