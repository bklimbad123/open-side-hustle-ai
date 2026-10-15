# Mastra

Mastra is a possible orchestration layer for future multi-step extraction and
review workflows. The current service calls its local extractor directly and
does not include a Mastra runtime.

An integration should preserve deterministic extraction, make external model
calls explicit, and avoid duplicating job state across orchestration systems.