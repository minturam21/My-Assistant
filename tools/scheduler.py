import time
import threading
from datetime import datetime


def schedule_reminder(trigger_time: datetime, message: str):
    def worker():
        delay = (trigger_time - datetime.now()).total_seconds()
        if delay > 0:
            time.sleep(delay)
        print(f"\n⏰ REMINDER: {message}")

    t = threading.Thread(target=worker, daemon=True)
    t.start()
