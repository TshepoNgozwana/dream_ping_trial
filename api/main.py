from fastapi import FastAPI
from pydantic import BaseModel
from logging_utils import log_event

app = FastAPI(title="Dream Ping API (trial)")

class SpecRequest(BaseModel):
    idea: str

BASE_STUB = {
    "title": "Dream Ping",
    "inputs": ["idea"],
    "outputs": ["spec"]
}

@app.get("/health")
def health():
    log_event("health_check", {})
    return {"status": "ok"}

@app.post("/spec")
def spec(req: SpecRequest):
    log_event("api_spec_received", {"idea": req.idea})
    stub = BASE_STUB.copy()
    stub["title"] = req.idea
    return stub
