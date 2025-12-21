"""
PLUGIN INTERFACE CONTRACT

Every plugin MUST follow this structure.
Core code depends on this contract.
This file is a reference, not an executable plugin.
"""

# Required plugin metadata
PLUGIN_NAME = "string_unique_name"
DESCRIPTION = "What this plugin does in one sentence"
TRIGGERS = ["list", "of", "keywords"]

# Optional priority (higher = preferred when multiple plugins match)
PRIORITY = 1


def run(command: str, context: dict) -> dict:
    """
    Execute the plugin logic.

    INPUTS:
    - command: raw user command (string)
    - context: read-only runtime context

    RETURNS (MANDATORY DICT FORMAT):
    {
        "status": "success" | "error",
        "output": any,                  # result or message
        "confidence": float,             # 0.0 to 1.0
        "requires_confirmation": bool,   # default False
        "summary": dict | None           # for delete/modify actions
    }

    RULES:
    - Must NOT access OS or filesystem directly
    - Must NOT execute shell commands directly
    - Must use tools layer for actions
    - Must NOT bypass safety checks
    """
    raise NotImplementedError
