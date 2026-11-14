# Part 1A — Deterministic app

## Summary

Build a deterministic invoice calculator that applies a fixed set of pricing rules.

## Goals

- Provide exact pricing behavior for valid inputs.
- Reject invalid inputs before calculation.
- Make the result reproducible across runs.

## Non-goals

- AI-generated pricing decisions
- Hidden state between calls
- Unbounded output interpretation

## Requirements

1. The calculator accepts `subtotal`, `tax_rate`, `discount_code`, and `shipping_option`.
2. Subtotal must be a non-negative decimal number.
3. Tax rate must be between 0 and 1 inclusive.
4. Eligible discount codes are `SAVE10` and `VIP15`.
5. Shipping is free when subtotal is at least 100; otherwise shipping is 10.
6. The output totals and tax values must be rounded to two decimal places.
7. The result must always include the keys: `subtotal`, `discount_rate`, `discount_amount`, `tax_amount`, `shipping_amount`, `total`.

## Acceptance criteria

- AC1: A valid quote is calculated exactly and deterministically.
- AC2: Invalid negative values fail with a structured error.
- AC3: Unsupported discount codes are treated as zero and recorded as a no-op.
- AC4: The validator can assert the exact output for a controlled sample.

## Risks and constraints

- The rules must be explicit and fixed.
- The implementation must not use randomness.
- Validation should rely on a separate, independent check.

