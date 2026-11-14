import json
from pathlib import Path
from typing import Any

from apps.ai_briefing.service import generate_briefing
from apps.deterministic_invoice.service import calculate_quote


ARTIFACT_DIR = Path(__file__).resolve().parent.parent / "artifacts" / "evidence"
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)


def write_evidence(name: str, payload: dict[str, Any]) -> Path:
    file_path = ARTIFACT_DIR / f"{name}.json"
    file_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return file_path


def validate_deterministic() -> list[str]:
    failures: list[str] = []
    sample = calculate_quote(120, 0.10, "SAVE10", "standard")
    expected = {
        "subtotal": 120.0,
        "discount_rate": 0.1,
        "discount_amount": 12.0,
        "tax_amount": 10.8,
        "shipping_amount": 0.0,
        "total": 118.8,
    }

    for key, value in expected.items():
        if sample.get(key) != value:
            failures.append(f"deterministic:{key}:expected={value} got={sample.get(key)}")

    return failures


def validate_ai() -> list[str]:
    failures: list[str] = []
    for index in range(30):
        brief = generate_briefing(
            "The launch is blocked by QA sign-off and vendor approval before the release can proceed.",
            tone="balanced",
        )

        if "title" not in brief or "summary" not in brief or "risk_level" not in brief or "action_items" not in brief:
            failures.append(f"ai:{index}:missing required fields")
            continue

        if brief["risk_level"] not in {"low", "medium", "high"}:
            failures.append(f"ai:{index}:invalid risk level {brief['risk_level']}")

        if len(brief["summary"]) > 180:
            failures.append(f"ai:{index}:summary too long ({len(brief['summary'])})")

        action_items = brief["action_items"]
        if not isinstance(action_items, list):
            failures.append(f"ai:{index}:action_items must be list")
            continue

        if len(action_items) > 5:
            failures.append(f"ai:{index}:too many action items ({len(action_items)})")

        for item_index, item in enumerate(action_items):
            if not isinstance(item, str):
                failures.append(f"ai:{index}:{item_index}:non-string action item")
                continue
            words = item.split()
            if len(words) > 12:
                failures.append(f"ai:{index}:{item_index}:action item too long ({len(words)} words)")
            if not any(word.lower() in {"confirm", "assign", "review", "draft", "schedule", "check", "approve"} for word in words):
                failures.append(f"ai:{index}:{item_index}:action item lacks command verb")

    return failures


def main() -> int:
    deterministic_failures = validate_deterministic()
    ai_failures = validate_ai()

    evidence = {
        "status": "pass" if not deterministic_failures and not ai_failures else "fail",
        "deterministic_failures": deterministic_failures,
        "ai_failures": ai_failures,
        "notes": "Validation independent from app generation.",
        "human_decision_required": True,
    }

    if deterministic_failures or ai_failures:
        write_evidence("validation_failure", evidence)
        print(json.dumps(evidence, indent=2))
        return 1

    write_evidence("validation_success", evidence)
    print(json.dumps(evidence, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
