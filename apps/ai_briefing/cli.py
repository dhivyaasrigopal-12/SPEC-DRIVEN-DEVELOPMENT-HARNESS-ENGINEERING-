"""CLI for AI-style project briefing app."""

from apps.ai_briefing.service import generate_briefing


if __name__ == "__main__":
    transcript = "The launch window is agreed, but QA and security still need sign-off before rollout."
    print(generate_briefing(transcript, tone="balanced"))
