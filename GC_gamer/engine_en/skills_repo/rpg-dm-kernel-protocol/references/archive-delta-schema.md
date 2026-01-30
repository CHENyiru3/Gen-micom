# ARCHIVE_DELTA schema (append/patch only)

Goal: persist game state without rewriting whole files.

## Format


## Rules

- Only `append` or minimal `patch`.
- Never rewrite entire files.
- If correcting contradictions, include a short correction note inside the appended decision.
