# ARCHIVE_DELTA schema (append/patch only)

Goal: persist game state without rewriting whole files.

## Format

```md
<!-- ARCHIVE_DELTA
files:
  - path: campaigns/<id>/sessions/session_YYYY-MM-DD*.md
    append: |
      ## Decision: ...
      - Real time: ...
      - In-world time: ...
      - Player input: ...
      - Rolls: ...
      - Resolution: ...
      - Consequences: ...
      - Indicators: ...
      - Clocks: ...
  - path: campaigns/<id>/STATE_PANEL.md
    patch: |
      (only the changed sections)
-->
```

## Rules

- Only `append` or minimal `patch`.
- Never rewrite entire files.
- If correcting contradictions, include a short correction note inside the appended decision.
