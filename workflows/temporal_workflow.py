"""Design sketch for making receipt extraction durable with Temporal.

Production implementation should add Temporal's Python SDK, define the
extraction steps as activities, and register this workflow with a worker.
"""


class ReceiptExtractionWorkflow:
    async def run(self, job_id: str, filename: str) -> dict[str, str]:
        """Pseudo-code outline; replace with Temporal workflow/activity calls."""
        raise NotImplementedError(
            "Implement durable upload, extraction, and persistence activities"
        )