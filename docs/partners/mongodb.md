# MongoDB Atlas

`app/mongo.py` provides an optional MongoDB adapter with the same basic job
methods as local storage. Configure it with a MongoDB URI explicitly; the app
continues to use SQLite by default.

Before using Atlas for real receipts, define retention and access controls,
restrict network access, and disclose that records leave the user's device.