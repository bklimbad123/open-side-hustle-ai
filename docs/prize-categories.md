# Prize and partner category map

This project is intentionally designed to show how a real side-hustle AI product can sit inside a wider open-source and partner ecosystem without giving up privacy or low-cost operation.

## Core open-source stack
- Ollama + Gemma 3 or another local open-weight model
- FastAPI
- SQLite by default
- Docker for containerized deployment

## Open-source / partner ecosystem fit
- Render: container-ready app suitable for demo hosting
- DigitalOcean: deploy the API or an app droplet
- GitHub Copilot: the repository is structured for AI-assisted development
- Sentry: instrumentation-ready for production tracing
- MongoDB Atlas: optional persistent storage for a hosted version
- Mastra: orchestration and workflow layer if the product expands
- Temporal: durable workflow pattern for asynchronous jobs
- Tiger Data: vector or hybrid retrieval for future document memories
- SerpApi: optional web data enrichment for vendor lookup or comparisons
- Backboard: terminal-first or assistant-first workflows
- TabPFN: classification/future analytics experiments
- Tinker: model tuning and adaptation experiments
- ElevenLabs: voice summaries for client reporting

## Why this matters in the challenge
The real differentiator is not that the app "uses many tools." The differentiator is that the business model remains open, low-cost, and privacy-first. That is the side-hustle angle: a useful product that a small customer can actually afford to pay for and can trust on their own machine.
