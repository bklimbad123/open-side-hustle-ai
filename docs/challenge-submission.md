# Side Hustle Challenge Submission Prep

## Readiness

ReceiptLens has a local-first dashboard, a Gemma/Ollama extraction path, local SQLite storage, and CI. Do not submit it as fully validated until the following evidence is collected:

- Run Gemma 3 4B locally and confirm `/health` reports `ollama_available: true`.
- Process several non-sensitive or synthetic receipt images and manually check vendor, date, currency, total, and line items.
- Show the workflow to at least one freelancer or small-business owner; record their feedback and whether they would pay. Do not imply a customer or sale if that has not happened.
- Capture a short demo or screenshots showing the local model ready, upload, extracted fields, and review state.
- Add links to the repository and demo in the final post. A DevRelay session link is optional.

Current gaps: real Gemma extraction has not been verified in this Codespace, and user feedback and demo media have not been collected.
Extraction quality has not been benchmarked against a closed model or a labeled receipt set; do not claim an accuracy advantage without that evidence.

## Draft Post

### ReceiptLens: private receipt sorting for freelancers

Freelancers and independent workers often have to turn a pile of receipts into expense records before bookkeeping. Those documents can contain personal and financial details, so sending every image to a hosted AI service is not always a good fit.

ReceiptLens is a small receipt desk: upload a receipt image, extract its vendor, date, currency, total, and line items, then review the result and save it locally. The extraction path uses Gemma served by Ollama; SQLite stores the resulting job records on the machine running the app.

Open innovation matters here because the open-weight model is the core of the workflow, not a label around a hosted API. With the default local Ollama configuration, inference can run without an internet connection after the model is downloaded, and receipt images do not need to leave the machine. This avoids per-document inference fees and lets the operator change the configured model. Those are architectural advantages, not yet measured accuracy wins over a closed model. The tradeoff is that users need compatible hardware and must review imperfect extraction results. If the model is unavailable, ReceiptLens labels its placeholder result for review rather than presenting it as successful AI extraction.

The intended customer is a freelancer who regularly sorts reimbursable expenses. **Replace this paragraph with actual user feedback and a willingness-to-pay result after testing.** No paying customer or measured accuracy result is claimed yet.

**Demo:** [Add a demo or screenshot link after capturing the verified local-model workflow.]

**Source:** [ReceiptLens repository](https://github.com/bklimbad123/open-side-hustle-ai)

The best-fitting featured category is Best Use of Gemma. Avoid claiming other partner categories unless those technologies are used in the submitted demo, not just mentioned in planning notes.