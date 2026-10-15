# Render

The existing Docker image provides a starting point for a hosted demo on
Render. A deployment should configure its start command and health check for
the FastAPI service and should use durable storage if uploaded job records must
survive restarts.

Do not deploy customer documents or enable external model calls without
explicitly documenting the data flow and obtaining user consent.