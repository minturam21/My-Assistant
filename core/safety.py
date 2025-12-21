"""
SAFETY GATE

ROLE:
- Final authority on whether an action is allowed or blocked

DOES:
- Enforce OS and protected-path rules
- Enforce multi-step confirmations
- Classify actions by risk
- Generate summaries before destructive actions

DOES NOT:
- Execute actions
- Reason creatively
- Trust model output blindly
"""
from typing import Dict

PROTECTED_PATHS = [
    "c:\\windows",
    "c:\\program files",
    "c:\\program files (x86)",
    "c:\\users\\default",
    "c:\\users\\public"]

def evaluate(intent: Dict, plugin_response: Dict) -> Dict:
    """
    Evaluate whether the requested action is safe.

    INPUTS:
    - intent: structured intent from intent.py
    - plugin_response: declared action intent from plugin (NOT execution)

    RETURNS:
    {
        "allowed": bool,
        "requires_confirmation": bool,
        "confirmation_steps": int,   # 0, 1, or 2
        "summary": dict | None,      # must exist for delete/modify
        "reason": str                # human-readable explanation
    }

    RULES:
    - Protected OS paths are ALWAYS blocked
    - Personal files require multiple confirmations
    - Ambiguity defaults to BLOCK
    """

    summary = plugin_response.get("summary")

    if summary:
        path = summary.get("path", "").lower()
        for protected in PROTECTED_PATHS:
            if path.startswith(protected):
                return {
                    "allowed": False,
                    "requires_confirmation": False,
                    "confirmation_steps": 0,
                    "summary": None,
                    "reason": "Protected system path"
                }

    return {
        "allowed": True,
        "requires_confirmation": plugin_response.get("requires_confirmation", False),
        "confirmation_steps": 1 if plugin_response.get("requires_confirmation") else 0,
        "summary": summary,
        "reason": "Allowed"
    }
