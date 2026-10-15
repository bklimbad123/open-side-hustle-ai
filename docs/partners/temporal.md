# Temporal

Temporal is a candidate for durable extraction jobs if ReceiptLens grows to
support retries, asynchronous review, or multi-step processing. The
`workflows/temporal_workflow.py` file is a dependency-free design sketch, not a
registered Temporal workflow.

A real deployment needs the Temporal Python SDK, activities, worker setup, and
an explicit privacy review for persisted workflow inputs and results.