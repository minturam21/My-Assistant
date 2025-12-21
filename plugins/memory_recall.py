PLUGIN_NAME = "memory_recall"
DESCRIPTION = "Recall stored memory when asked"
TRIGGERS = ["where", "what", "recall"]
PRIORITY = 9

from tools.memory_db import recall_memory


def run(command: str, context: dict) -> dict:
    tokens = command.lower().split()
    keyword = tokens[-1]  # simple baseline

    results = recall_memory(keyword)

    if not results:
        return {
            "status": "success",
            "output": "I don’t have that saved.",
            "confidence": 0.6,
            "requires_confirmation": False,
            "summary": None
        }

    if len(results) > 1:
        return {
            "status": "success",
            "output": f"Multiple matches found: {[r[1] for r in results]}",
            "confidence": 0.7,
            "requires_confirmation": False,
            "summary": None
        }

    category, key, value, created_at = results[0]

    return {
        "status": "success",
        "output": f"{key} → {value}",
        "confidence": 0.95,
        "requires_confirmation": False,
        "summary": None
    }
