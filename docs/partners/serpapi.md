# SerpApi

SerpApi could support optional vendor enrichment, such as looking up a vendor's
canonical name after extraction. No search calls are made by the current app.

Keep enrichment separate from the extracted source data, disclose external
queries, and configure `SERPAPI_KEY` only in the environment that needs it.