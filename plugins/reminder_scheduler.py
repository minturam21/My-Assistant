PLUGIN_NAME = "reminder_scheduler"
DESCRIPTION = "Schedule time-based reminders"
TRIGGERS = ["remind", "notify"]
PRIORITY = 10

from datetime import datetime, timedelta
from tools.scheduler import schedule_reminder


def run(command: str, context: dict) -> dict:
    lowered = command.lower()

    # Require time specification
    if "in" not in lowered:
        return {
            "status": "error",
            "output": "Please specify time, e.g. 'remind me in 10 minutes'",
            "confidence": 0.3,
            "requires_confirmation": False,
            "summary": None
        }

    try:
        # Extract text after "in"
        after_in = lowered.split("in", 1)[1]

        tokens = after_in.split()

        # Find first number safely
        amount = None
        for t in tokens:
            if t.isdigit():
                amount = int(t)
                break

        if amount is None:
            return {
                "status": "error",
                "output": "Could not find time amount.",
                "confidence": 0.3,
                "requires_confirmation": False,
                "summary": None
            }

        # Determine unit
        if "minute" in after_in:
            trigger = datetime.now() + timedelta(minutes=amount)
        elif "hour" in after_in:
            trigger = datetime.now() + timedelta(hours=amount)
        else:
            return {
                "status": "error",
                "output": "Only minutes or hours are supported.",
                "confidence": 0.4,
                "requires_confirmation": False,
                "summary": None
            }

        # Extract message after "to"
        if "to" in tokens:
            msg_index = tokens.index("to") + 1
            message = " ".join(tokens[msg_index:])
        else:
            message = "Reminder"

        # Schedule reminder
        schedule_reminder(trigger, message)

        return {
            "status": "success",
            "output": f"Reminder set for {trigger.strftime('%H:%M:%S')}",
            "confidence": 0.9,
            "requires_confirmation": False,
            "summary": {
                "time": trigger.isoformat(),
                "message": message
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "output": f"Failed to set reminder: {e}",
            "confidence": 0.2,
            "requires_confirmation": False,
            "summary": None
        }
