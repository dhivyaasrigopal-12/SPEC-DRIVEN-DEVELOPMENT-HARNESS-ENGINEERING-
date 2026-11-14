import random
from typing import List


VALID_RISK_LEVELS = {"low", "medium", "high"}


def _clean_text(value: str) -> str:
    return " ".join(value.split())


def generate_briefing(transcript: str, tone: str = "balanced") -> dict:
    """Generate a briefing with AI-like variability while staying within a bounded policy."""
    text = _clean_text(transcript or "")
    if not text:
        raise ValueError("transcript cannot be empty")

    rng = random.Random()
    summaries = [
        "The team aligned on scope, dependencies, and the launch window.",
        "The team identified the main blockers, agreed on ownership, and set the next milestone.",
        "The project remains on track with a few delivery risks that need review before sign-off.",
    ]

    action_bank = [
        "confirm launch checklist",
        "assign owners for testing",
        "review dependency risks",
        "draft user support notes",
        "schedule stakeholder check-in",
        "review backlog priorities",
        "confirm rollout sequence",
    ]

    action_items = random.sample(action_bank, k=rng.randint(2, 4))
    summary = rng.choice(summaries)
    risk_level = rng.choice(["low", "medium", "high"])

    if tone.lower() == "urgent":
        summary = "Urgent follow-up is required because delivery and dependency risks remain active."
        risk_level = "high"

    if tone.lower() == "calm":
        summary = "The work is stable with clear ownership and a manageable set of next actions."
        risk_level = "low"

    return {
        "title": "Project Briefing",
        "summary": summary,
        "risk_level": risk_level,
        "action_items": action_items,
    }


if __name__ == "__main__":
    sample = "We need to release the feature but still need QA sign-off and vendor approval."
    print(generate_briefing(sample, tone="balanced"))
