# Gemma

ReceiptLens uses Ollama with `gemma3:4b` as its default local model. This keeps
document extraction on the user's machine after the model is downloaded.

The current integration path is `OLLAMA_BASE_URL` and `OLLAMA_MODEL`. Validate
extraction quality and hardware requirements against a small, consented set of
sample receipts before changing the default.