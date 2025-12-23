PLUGIN_NAME = "memory_update"
DESCRIPTION = "Update an existing memory"
TRIGGERS = ["update", "change"]
PRIORITY = 7

from tools.memory_db import update_memory


def run(command: str, context: dict) -> dict:
    # expected: update memory <id> to <new value>
    lowered = command.lower()

    try:
        parts = lowered.split("to", 1)
        before, new_value = parts[0], parts[1].strip()
        mem_id = int(before.split()[-1])

        update_memory(mem_id, new_value)

        return {
            "status": "success",
            "output": f"Memory [{mem_id}] updated.",
            "confidence": 0.9,
            "requires_confirmation": False,
            "summary": None
        }
    except Exception as e:
        return {
            "status": "error",
            "output": f"Failed to update memory: {e}",
            "confidence": 0.3,
            "requires_confirmation": False,
            "summary": None
        }
