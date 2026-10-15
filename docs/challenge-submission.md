# Side Hustle Challenge Submission

## Readiness

ReceiptLens is a prototype, not yet a validated receipt-extraction product. On 2026-10-15, Gemma 3 4B was installed in the Codespace and answered a text-only prompt. Its Ollama vision runner failed on both image-generation and image-chat requests with `unexpected EOF`; the app then returned its low-confidence fallback instead of extracted receipt fields. Gemma 3 1B was also checked, but that Ollama model does not support images.

The dashboard, API upload path, SQLite job listing, and fallback behavior have passed mocked integration checks. Real image extraction, user feedback, demo media, measured accuracy, and willingness to pay have not been verified. Do not present this as a working AI receipt sorter or claim a customer result until those gaps are addressed.

## Draft Post

### ReceiptLens: a local-first receipt desk prototype

Freelancers and independent workers often have to turn a pile of receipts into expense records before bookkeeping. Those documents can contain personal and financial details, so sending every image to a hosted AI service is not always a good fit.

I built ReceiptLens, a prototype receipt desk with a browser dashboard for uploading JPG, PNG, and WebP images, reviewing recent jobs, and inspecting extracted fields and line items. The app uses FastAPI and stores job records in SQLite on the machine running it. Its intended AI path is Gemma 3 served locally through Ollama.

Open innovation matters to this project because the goal is to keep sensitive receipt images on the user's machine, avoid per-document hosted inference fees, and retain the freedom to change models. Those are design advantages, not measured wins over a closed model. In my Codespace test, Gemma 3 4B answered text prompts, but its vision runner failed on receipt images with `unexpected EOF`; ReceiptLens correctly marked the resulting placeholder for review. So this is an honest prototype report, not a claim that receipt extraction is working end to end.

The intended customer is a freelancer who regularly sorts reimbursable expenses. I have not yet tested the prototype with a freelancer or small-business owner, so I do not know whether someone would pay for it. Customer interviews and a successful local vision run are the next validation steps.

**Source:** [ReceiptLens on GitHub](https://github.com/bklimbad123/open-side-hustle-ai)

I have not recorded a demo or captured verified extraction results yet. I would submit this as a prototype/build-in-progress entry only; for a product-focused submission, first get Gemma image extraction working, test several synthetic or non-sensitive receipts, and include a short demo plus real user feedback. The best-fitting featured prize category is Best Use of Gemma; I am not claiming other partner categories based only on planning notes.