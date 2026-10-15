# Side Hustle Challenge Submission

## Form Fields

**Title**

ReceiptLens: A Local-First Receipt Desk Prototype

**Tags**

`#devchallenge` `#hf26challenge` `#gemma` `#opensource`

**Cover image**

Use [the deployed dashboard screenshot](docs/submission-images/receiptlens-desktop.png). Crop it to the form's 1000:420 ratio if needed.

**Cover video link**

None. No video has been recorded.

## Post Body

Freelancers and independent workers often have to turn a pile of receipts into expense records before bookkeeping. Those documents can contain personal and financial details, so sending every image to a hosted AI service is not always a good fit.

I built ReceiptLens, an early prototype with a browser dashboard for uploading JPG, PNG, and WebP images, reviewing recent jobs, and inspecting extracted fields. It uses FastAPI and SQLite, with Gemma 3 through Ollama as its intended open-weight extraction path.

Open innovation matters here because a local installation is designed to keep receipt images on the user's machine, avoid per-document hosted inference fees, and leave the model replaceable. These are design goals, not measured accuracy wins over closed models. In my Codespace test, Gemma 3 4B answered a text prompt, but image inference failed with `unexpected EOF`; the app returned a low-confidence fallback marked for review.

The public deployment is on Render's free plan: [receiptlens-free.onrender.com](https://receiptlens-free.onrender.com). It hosts the dashboard and API, but not Ollama or Gemma, so the page reports that the model is unavailable. Uploaded files reach the Render service; this public link is for synthetic receipts only. Do not upload real financial documents. Its free storage is also ephemeral, so saved jobs may disappear after a restart.

I have not yet tested ReceiptLens with a freelancer or small-business owner, and I have no customer, payment, accuracy benchmark, or willingness-to-pay result to report. This is a prototype/build-in-progress entry, not a claim that receipt extraction works end to end. The next steps are to get Gemma vision inference working, test several synthetic receipts, and gather feedback from an intended user.

**Live prototype:** [https://receiptlens-free.onrender.com](https://receiptlens-free.onrender.com)

**Source code:** [https://github.com/bklimbad123/open-side-hustle-ai](https://github.com/bklimbad123/open-side-hustle-ai)

**Deployed dashboard:**

![ReceiptLens deployed dashboard showing the model-unavailable notice and synthetic receipt marked for review](https://raw.githubusercontent.com/bklimbad123/open-side-hustle-ai/main/docs/submission-images/receiptlens-desktop.png)

**Synthetic test receipt:**

![Synthetic receipt used to check the public deployment](https://raw.githubusercontent.com/bklimbad123/open-side-hustle-ai/main/docs/submission-images/synthetic-receipt-input.png)

Best Use of Gemma is a potential prize category if the vision path works in the submitted build. I am not claiming other partner categories based only on planning notes.