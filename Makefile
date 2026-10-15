PYTHON ?= python3

run:
	$(PYTHON) -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

install:
	$(PYTHON) -m pip install -r requirements.txt

model:
	ollama pull gemma3:4b
