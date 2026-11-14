# Part 1B — AI app under a harness

## Summary

Build a project-briefing generator that behaves like an AI assistant but remains constrained by a validation harness.

## Goals

- Simulate a non-deterministic AI output generator.
- Keep output within safe operational ranges.
- Use validation to catch and document policy violations.
- Allow corrective generation after failure.

## Non-goals

- Unbounded freeform AI behavior without governance
- Hidden randomness with no fail-safe
- Accepting invalid output without review

## Requirements

1. The app accepts a `transcript` string and an optional `tone` argument.
2. The app must produce a dictionary with `title`, `summary`, `risk_level`, and `action_items`.
3. `risk_level` must be one of `low`, `medium`, or `high`.
4. `action_items` must contain no more than 5 items.
5. Each action item must be 12 words or fewer and contain at least one verb.
6. The summary must be no longer than 180 characters for the harness to accept it.
7. Output variability is acceptable, but all outputs must be validated against the same constraints.
8. A failed generation must be recorded as structured evidence.

## Acceptance criteria

- AC1: The app generates a valid briefing for a typical transcript.
- AC2: Multiple runs can produce different valid outputs without violating policy.
- AC3: Invalid outputs are rejected via a harness and documented as evidence.
- AC4: The harness identifies the exact constraint violated.

## Risks and constraints

- AI-like output is inherently non-deterministic.
- The harness must operate outside generated implementation logic.
- Human review is required before final acceptance.

