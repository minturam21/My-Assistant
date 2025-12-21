"""
PLUGIN REGISTRY

ROLE:
- Discover plugins from plugins/ directory
- Validate plugin interface compliance
- Provide list of safe, usable plugins to router

SECURITY RULES:
- Ignore files starting with "_"
- Ignore non-.py files
- Reject plugins missing required attributes
- Never execute plugin.run() here

DOES:
- Load plugin files
- Verify plugin interface compliance
- Expose available plugins to router

DOES NOT:
- Execute plugins
- Contain plugin logic
- Handle intent or safety
"""
import importlib.util
import os
from typing import List, Dict


PLUGIN_DIR = os.path.join(os.path.dirname(__file__), "..", "plugins")


REQUIRED_ATTRIBUTES = [
    "PLUGIN_NAME",
    "DESCRIPTION",
    "TRIGGERS",
    "run"
]


def discover_plugins() -> List[Dict]:
    plugins = []

    for filename in os.listdir(PLUGIN_DIR):
        if not filename.endswith(".py"):
            continue
        if filename.startswith("_"):
            continue
        if filename == "plugin_interface.py":
            continue

        path = os.path.join(PLUGIN_DIR, filename)
        name = filename[:-3]

        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)

        try:
            spec.loader.exec_module(module)
        except Exception:
            continue

        if validate_plugin(module):
            plugins.append({
                "name": module.PLUGIN_NAME,
                "triggers": module.TRIGGERS,
                "priority": getattr(module, "PRIORITY", 1),
                "module": module
            })

    return plugins


def validate_plugin(plugin_module) -> bool:
    for attr in REQUIRED_ATTRIBUTES:
        if not hasattr(plugin_module, attr):
            return False
    return callable(plugin_module.run)
