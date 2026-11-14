# Part 1B plan

## Overview

This app demonstrates how a harness can constrain a generative component while preserving variability.

## Components

- AI-like briefing generator
- Constraint validator
- Evidence processor
- Human acceptance gate

## Verification strategy

- Run multiple generations
- Validate each field against policy
- Record failed records as JSON evidence
- Escalate to human reviewer when needed

