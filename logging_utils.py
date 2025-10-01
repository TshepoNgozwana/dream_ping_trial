import json
from datetime import datetime, timezone
from settings import COCKPIT_DIR, LOG_PREFIX

def log_event(action: str, payload: dict | None = None):
    COCKPIT_DIR.mkdir(parents=True, exist_ok=True)
    filename = COCKPIT_DIR / f"{LOG_PREFIX}{datetime.utcnow().strftime('%Y%m%d')}.jsonl"
    entry = {
        "timestamp": datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(),
        "action": action,
        "payload": payload or {}
    }
    with open(filename, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry) + "\n")
