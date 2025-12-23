import os

SAFE_EXTENSIONS = [
    ".txt", ".pdf", ".docx", ".xlsx",
    ".py", ".ipynb", ".md"
]

BLOCKED_DIRS = [
    "c:\\windows",
    "c:\\program files",
    "c:\\program files (x86)"
]


def is_blocked(path: str) -> bool:
    p = path.lower()
    return any(p.startswith(b) for b in BLOCKED_DIRS)


def search_files(root: str, keyword: str, limit: int = 20):
    matches = []
    keyword_lower = keyword.lower()

    for dirpath, dirnames, filenames in os.walk(root):
        if is_blocked(dirpath):
            continue

        for name in filenames:
            name_lower = name.lower()

            # improved matching (partial + prefix)
            if keyword_lower in name_lower or name_lower.startswith(keyword_lower[:3]):
                full_path = os.path.join(dirpath, name)

                if os.path.splitext(full_path)[1].lower() in SAFE_EXTENSIONS:
                    matches.append(full_path)

                if len(matches) >= limit:
                    return matches

    return matches
