PLUGIN_NAME = "memory_list"
DESCRIPTION = "List saved memories"
TRIGGERS = ["list memory", "show memory", "memory list"]
PRIORITY = 7

from tools.memory_db import list_memory


def run(command: str, context: dict) -> dict:
    rows = list_memory()

    if not rows:
        return {
            "status": "success",
            "output": "No memories saved.",
            "confidence": 0.8,
            "requires_confirmation": False,
            "summary": None
        }

    output = []
    for mem_id, category, key, value, created_at in rows:
        output.append(f"[{mem_id}] {key} → {value}")

    return {
        "status": "success",
        "output": output,
        "confidence": 0.9,
        "requires_confirmation": False,
        "summary": {"count": len(rows)}
    }
