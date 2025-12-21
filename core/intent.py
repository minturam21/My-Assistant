"""
INTENT MODULE

ROLE:
- Convert raw user input into structured intent

DOES:
- Classify command type (action, query, reminder, memory)
- Extract lightweight parameters
- Mark risk level and ambiguity

DOES NOT:
- Execute actions
- Call plugins
- Perform safety checks
"""
from typing import Dict


def parse_intent(command: str) -> Dict:
    """
    Parse raw user command into structured intent.

    RETURNS:
    {
        "type": str,              # e.g. "action", "query", "memory", "reminder"
        "keywords": list,         # extracted keywords
        "entities": dict,         # file names, dates, etc. (lightweight)
        "risk": str,              # "low", "medium", "high"
        "confidence": float       # confidence in intent classification
    }
    """
    tokens = command.lower().split()

    return {
        "type": "action",
        "keywords": tokens,
        "entities": {},
        "risk": "low",
        "confidence": 0.7
    }
