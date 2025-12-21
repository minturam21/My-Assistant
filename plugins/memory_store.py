PLUGIN_NAME = "memory_store"
DESCRIPTION = "Store information explicitly when user asks to remember"
TRIGGERS = ["remember", "save", "store"]
PRIORITY = 10

from tools.memory_db import store_memory


def run(command: str, context: dict) -> dict:
    # very simple parsing (high-level baseline)
    lowered = command.lower()

    # Example: "remember my fraud project is in D:/Projects/Fraud"
    try:
        parts = lowered.replace("remember", "").strip().split(" is ")
        if len(parts) != 2:
            return {
                "status": "error",
                "output": "Please use format: remember <thing> is <detail>",
                "confidence": 0.4,
                "requires_confirmation": False,
                "summary": None
            }

        key = parts[0].strip()
        value = parts[1].strip()

        store_memory(category="note", key=key, value=value)

        return {
            "status": "success",
            "output": f"Saved: {key}",
            "confidence": 0.9,
            "requires_confirmation": False,
            "summary": None
        }

    except Exception as e:
        return {
            "status": "error",
            "output": f"Failed to save memory: {e}",
            "confidence": 0.2,
            "requires_confirmation": False,
            "summary": None
        }
