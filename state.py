import json
import os
from config import STATE_FILE


def load_previous_state() -> bool:
    if not os.path.exists(STATE_FILE):
        return False

    with open(STATE_FILE, "r") as f:
        return json.load(f).get("available", False)


def save_current_state(available: bool):
    with open(STATE_FILE, "w") as f:
        json.dump({"available": available}, f)