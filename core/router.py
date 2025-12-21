"""
ROUTER

ROLE:
- Select the most appropriate plugin for a given intent

DOES:
- Receive intent and available plugins
- Match intent against plugin triggers
- Resolve conflicts using priority
- Return selected plugin reference

DOES NOT:
- Execute plugin logic
- Perform safety checks
- Modify context
"""
from typing import Dict, List, Optional


def select_plugin(intent: Dict, plugins: List[Dict]) -> Optional[Dict]:
    candidates = []

    intent_keywords = intent.get("keywords", [])

    for plugin in plugins:
        for trigger in plugin["triggers"]:
           for word in intent_keywords:
               if trigger in word:
                  candidates.append(plugin)
                  break


    if not candidates:
        return None

    # Highest priority wins
    candidates.sort(key=lambda p: p["priority"], reverse=True)
    return candidates[0]
