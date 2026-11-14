# Example of a human acceptance gate
# Set HUMAN_ACCEPT=true to simulate approval.

import os


def check_human_acceptance() -> bool:
    return os.getenv("HUMAN_ACCEPT", "").strip().lower() == "true"


if __name__ == "__main__":
    print("Approved" if check_human_acceptance() else "Pending human review")
