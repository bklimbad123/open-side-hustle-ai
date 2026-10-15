# DigitalOcean

ReceiptLens can be deployed as a container on a DigitalOcean App Platform
service or Droplet. A Droplet with suitable hardware can also host Ollama;
otherwise configure the app to reach a separately managed model service.

Keep API keys in deployment secrets, expose only required ports, and use a
persistent volume for local SQLite data.