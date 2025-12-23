PLUGIN_NAME = "file_locator"
DESCRIPTION = "Find files or folders by name"
TRIGGERS = ["find", "where", "locate", "search"]
PRIORITY = 8

import os
from tools.filesystem import search_files
from tools.memory_db import recall_memory


DEFAULT_SEARCH_ROOTS = [
    os.path.expanduser("~"),   # user home
    "d:\\"                     # common data drive (safe)
]


def run(command: str, context: dict) -> dict:
    tokens = command.lower().split()

    if len(tokens) < 2:
        return {
            "status": "error",
            "output": "Please specify what to search for.",
            "confidence": 0.3,
            "requires_confirmation": False,
            "summary": None
        }

    keyword = tokens[-1]

    # common aliases
    if keyword in ["resume", "cv"]:
        keywords = ["resume", "cv"]
    else:
        keywords = [keyword]

    results = []

    # filesystem search
    for root in DEFAULT_SEARCH_ROOTS:
        if os.path.exists(root):
            for k in keywords:
                results.extend(search_files(root, k))

    # remove duplicates
    results = list(dict.fromkeys(results))

    if results:
        return {
            "status": "success",
            "output": results[:5],
            "confidence": 0.9,
            "requires_confirmation": False,
            "summary": {
                "matches": len(results)
            }
        }

    # memory fallback
    mem_results = recall_memory(keyword)
    if mem_results:
        category, key, value, created_at = mem_results[0]
        return {
            "status": "success",
            "output": f"From memory: {key} → {value}",
            "confidence": 0.9,
            "requires_confirmation": False,
            "summary": None
        }

    return {
        "status": "success",
        "output": f"No files or memory found for '{keyword}'.",
        "confidence": 0.6,
        "requires_confirmation": False,
        "summary": None
    }
