"""
ROLE:
- Central orchestrator of the system
- Controls execution flow only

flow:
1. Get user input
2. Parse intent
3. Discover plugins
4. Select plugin
5. Ask plugin what it intends to do
6. Ask safety if it is allowed
7. Execute via tools (only if allowed)
8. Send result to output


DOES:
- Calls input handler
- Calls intent detection
- Calls safety checks
- Routes to plugin via router
- Collects result and sends to output

DOES NOT:
- Contain business logic
- Know about specific plugins
- Execute system actions
- Talk directly to LLM
"""
from core.intent import parse_intent
from core.registry import discover_plugins
from core.router import select_plugin
from core.safety import evaluate


def run_engine():
    """
    Main orchestration loop.
    """

    # 1. Get user input (text only for now)
    command = input(">> ").strip()
    if not command:
        print("No command received.")
        return

    # 2. Parse intent
    intent = parse_intent(command)

    # 3. Discover plugins
    plugins = discover_plugins()
    print("Loaded plugins:", [p["name"] for p in plugins])
    if not plugins:
        print("No plugins available.")
        return

    # 4. Select plugin
    plugin = select_plugin(intent, plugins)
    if not plugin:
        print("No suitable plugin found.")
        return

    # 5. Ask plugin what it intends to do (NOT execute)
    try:
        plugin_response = plugin["module"].run(command, {})
    except Exception as e:
        print(f"Plugin error: {e}")
        return

    # 6. Safety evaluation
    decision = evaluate(intent, plugin_response)

    if not decision["allowed"]:
        print(f"Blocked: {decision['reason']}")
        return

    # 7. Confirmation handling
    if decision["requires_confirmation"]:
        print("Action requires confirmation:")
        if decision.get("summary"):
            print("Summary:", decision["summary"])

        confirm = input("Confirm? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Action cancelled.")
            return

    
    # 8. Final output (execution happens inside tools later)
    print("Result:", plugin_response.get("output"))
    input("Press Enter to exit...")

