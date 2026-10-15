This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 2: Side Hustle](https://dev.to/challenges/hacktoberfest-week2-2026-10-12)

## What I Built

ReceiptLens is an early receipt-desk prototype for freelancers and independent workers who spend time turning receipts into bookkeeping records. It has a browser dashboard for uploading JPG, PNG, and WebP images, reviewing recent jobs, and inspecting extracted fields.

The problem is real, but this prototype is not yet a validated product: I have not tested it with a freelancer or small-business owner, and I have no payment or willingness-to-pay results to report.

## Demo

The public demo is hosted on Render's free plan: [https://receiptlens-free.onrender.com](https://receiptlens-free.onrender.com).

The free service hosts the dashboard and API, not Ollama or Gemma. The page reports the model unavailable, and uploads return a fallback marked for review. Uploaded files reach Render, so use synthetic receipts only; do not upload real financial documents. The free service also has ephemeral storage, so saved jobs may disappear after a restart.

![ReceiptLens on Render showing the model-unavailable notice and a synthetic receipt marked for review](https://raw.githubusercontent.com/bklimbad123/open-side-hustle-ai/main/docs/submission-images/receiptlens-desktop.png)

![Synthetic receipt used to check the deployment](https://raw.githubusercontent.com/bklimbad123/open-side-hustle-ai/main/docs/submission-images/synthetic-receipt-input.png)

## Code

Source code: [github.com/bklimbad123/open-side-hustle-ai](https://github.com/bklimbad123/open-side-hustle-ai)

## How I Built It

The dashboard and API use FastAPI, with SQLite for local job records. The intended extraction path sends receipt images to Gemma 3 4B through Ollama. In my Codespace, Gemma answered a text prompt, but image requests failed with `unexpected EOF`; ReceiptLens then returned its low-confidence fallback. The deployed free service has no model runtime, so its upload path is not a working AI extraction demo.

## Why Does Open Innovation Matter?

In a working local setup, an open-weight model can let users keep receipt images on their own machine after downloading the model, avoid per-document hosted inference fees, and switch models as their needs change. These are design benefits, not measured accuracy wins over closed APIs. The local vision path still needs to be made reliable and tested. The public Render deployment is different: uploaded files reach Render, so it is only for synthetic data.

## Prize Categories

Best Use of Gemma is the only category this project is intended to fit. Gemma 3 4B is the planned open-weight extraction model, but image inference failed in the tested build, so this prototype does not yet demonstrate a successful end-to-end Gemma receipt workflow. I am not claiming other partner categories based only on planning notes.