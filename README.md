# ReceiptLens

ReceiptLens is a local-first invoice and receipt sorter for freelancers and small business owners. It turns uploaded purchase docs into clean structured data without sending files to a third-party service.

Why this exists
- Many solo workers and micro-business owners spend hours sorting receipts and invoices by vendor, date, and total.
- The task is repetitive, boring, and often sensitive.
- A local AI tool can make this cheap to operate and privacy-safe.

Open-core idea
- Built on open-weight models and open-source tooling.
- Runs locally with Ollama and an open model such as Gemma 3.
- Stores uploads and job records locally by default; cloud sync is not currently implemented.
- Can be swapped for a different model or fine-tuned for a niche workflow.

This is a side hustle product with a real customer problem:
- freelancers tracking reimbursable expenses
- independent contractors sorting invoices for bookkeeping
- restaurant groups or service businesses batching receipts

Why open innovation matters here
- No internet required once the model is installed.
- No recurring API bill for every upload.
- Data stays in the user's control.
- The app can be adapted to niche languages, currencies, or invoice formats without waiting on a vendor roadmap.
- Compared with a closed AI API, this lets the business remain inexpensive, private, and resilient.

What the app does
- Accepts receipt and invoice images (JPG, PNG, or WebP) in the browser dashboard
- Uses Gemma through a local Ollama server to classify the document and extract:
  - vendor name
  - invoice date
  - total amount
  - currency
  - line items
  - notes or categorization
- Saves extracted fields to a local SQLite database
- Lets you review recent documents and extracted line items in the dashboard
- Exposes the extraction and job-list APIs for other clients

Current status
- The FastAPI service serves a browser dashboard and a small JSON API.
- Receipt extraction uses a model served by Ollama; the app does not bundle model weights.
- If Ollama or the configured model is unavailable, the app stores a placeholder result marked for review. Confirm the model status before relying on extracted fields.
- The prototype still needs validation with real users and representative receipts before making accuracy or willingness-to-pay claims.

Architecture
- Frontend: responsive browser dashboard served by FastAPI
- API: FastAPI
- AI runtime: open-weight model served by Ollama
- Storage: SQLite by default, with room for MongoDB Atlas if a cloud-backed SaaS version is needed
- Observability: Sentry-ready config
- Durability: Temporal-ready workflow design
- Retrieval: optional vector search using Tiger Data / pgvector patterns

Quick start

Prerequisites
- Python 3.11+
- Ollama installed locally
- An open model that supports vision or prompt-based extraction. The default is Gemma 3 4B.

1) Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Pull the model

```bash
ollama pull gemma3:4b
```

3) Start the app

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Open `http://localhost:8000` and confirm the dashboard reports that the local model is ready. If you use Docker Compose, start the Ollama service with `docker compose up -d ollama`, then pull the model with `docker compose exec ollama ollama pull gemma3:4b`.

The dashboard accepts JPG, PNG, and WebP images. The API is available at `/extract`, recent jobs at `/jobs`, model status at `/health`, and app metadata at `/api`.

4) Upload a file via the API

```bash
curl -X POST http://localhost:8000/extract \
  -F "file=@/path/to/receipt.jpg"
```

Example response

```json
{
  "job_id": "uuid",
  "document_type": "invoice",
  "vendor": "Acme Studio",
  "currency": "USD",
  "amount": 142.50,
  "date": "2026-10-15",
  "items": [
    {"description": "Brand strategy sprint", "amount": 125.00},
    {"description": "Tax", "amount": 17.50}
  ],
  "raw_response": {
    "confidence": "medium"
  }
}
```

Local-first value proposition
- Works on a laptop without a cloud dependency after the model is downloaded.
- Keeps document data local and private.
- Lets the owner replace the model as better open-weight options become available.
- Keeps cost near zero after the initial hardware purchase.
- Creates a business model that is not dominated by API pricing or vendor lock-in.

Prize and partner category alignment
This repo is designed to support multiple partner categories and show how an open-source AI side hustle can fit a broader ecosystem.

- Gemma: default local model choice for open-weight inference
- Render: container-ready for deployment and demo hosting
- DigitalOcean: app can be deployed to a GPU or app droplet
- GitHub: this repo is structured for Copilot-assisted development and CI automation
- Sentry: ready for trace instrumentation and production debugging
- MongoDB Atlas: optional data layer for a hosted SaaS version
- Mastra: can orchestrate the extraction workflow and memory features
- Temporal: workflow durability patterns are compatible with the service design
- Tiger Data: optional vector search for document memory and RAG patterns
- SerpApi: optional market or vendor lookup features for data enrichment
- Tinker / TabPFN: helpful for future forecasting or classification experiments
- Backboard: open-source terminal workflow use cases
- ElevenLabs: optional voice summaries for finance workflows

A simple launch strategy
1. Sell a local-only version to one freelancer or small business owner.
2. Offer a $29–$99/month plan for exports and folder sync.
3. Add an admin dashboard for grouping vendors and categories.
4. Add a CSV export for bookkeeping tools.
5. Expand to more document types and more niche workflows.

This is the kind of tiny product that can become a real business because it solves one boring task well and keeps the customer in control of their data.
