"""
ENTRY POINT OF THE ASSISTANT

ROLE:
- Start the system
- Pass user input through the core pipeline
- Never contain business logic
"""

from core.engine import run_engine


def main():
    """
    High-level execution flow:
    input -> intent -> safety -> routing -> plugin -> output
    """
    run_engine()


if __name__ == "__main__":
    main()
