# Dream Ping — 2-hour trial

This repo is a minimal trial showing a Streamlit front-end wired to a FastAPI service with simple cockpit logging.

## Running

1. Copy `.env.example` to `.env` if you want to override defaults.
2. Create a virtual environment and install deps:
   ```
   python -m venv .venv
   source .venv/bin/activate   # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
3. Start the API:
   ```
   uvicorn api.main:app --reload --port 8000
   ```
4. Start the Streamlit UI:
   ```
   streamlit run streamlit_app/app.py
   ```
5. Use the UI to submit an idea — Streamlit calls `POST /spec` and displays the JSON stub.

### What the JSON stub looks like

```json
{
  "title": "User idea text here",
  "inputs": ["idea"],
  "outputs": ["spec"]
}
```

### Cockpit logging

All events (submit, API calls, health checks) are written as JSON lines to `data/cockpit/run-YYYYMMDD.jsonl`. The repo includes `.env.example`, `settings.py`, `logging_utils.py`, a smoke CI workflow, and a dummy pytest to verify basic CI setup.
