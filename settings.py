from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

COCKPIT_DIR = Path(os.getenv("COCKPIT_DIR", "data/cockpit"))
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8000"))
API_URL = os.getenv("API_URL", f"http://{API_HOST}:{API_PORT}")
LOG_PREFIX = os.getenv("LOG_PREFIX", "run-")
