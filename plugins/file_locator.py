PLUGIN_NAME = "file_locator"
DESCRIPTION = "Find files or folders by name"
TRIGGERS = ["find", "where", "locate", "search"]
PRIORITY = 8

from tools.filesystem import search_files
import os


DEFAULT_SEARCH_ROOTS = [
    os.path.expanduser("~"),   # User home
    "d:\\"                     # Common data drive
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
    results = []

    for root in DEFAULT_SEARCH_ROOTS:
        if os.path.exists(root):
            results.extend(search_files(root, keyword))

    if not results:
        return {
            "status": "success",
            "output": f"No files found for '{keyword}'.",
            "confidence": 0.7,
            "requires_confirmation": False,
            "summary": None
        }

    return {
        "status": "success",
        "output": results[:5],   # show top 5 only
        "confidence": 0.9,
        "requires_confirmation": False,
        "summary": {
            "matches": len(results)
        }
    }
