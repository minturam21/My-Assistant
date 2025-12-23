PLUGIN_NAME = "memory_delete"
DESCRIPTION = "Delete a memory safely"
TRIGGERS = ["delete memory", "remove memory"]
PRIORITY = 7

from tools.memory_db import delete_memory


def run(command: str, context: dict) -> dict:
    # expected: delete memory <id>
    try:
        mem_id = int(command.split()[-1])

        return {
            "status": "pending",
            "output": f"Confirm deletion of memory [{mem_id}]",
            "confidence": 0.8,
            "requires_confirmation": True,
            "summary": {"mem_id": mem_id}
        }
    except Exception as e:
        return {
            "status": "error",
            "output": f"Invalid delete command: {e}",
            "confidence": 0.3,
            "requires_confirmation": False,
            "summary": None
        }
