# ARCHIVE_DELTA.md — Incremental Archive Specification (Stable)

> **Goal**: Externalize and make "memory/state" traceable; each turn only makes minimal changes (append/patch), never rewrites entire files.
> **适用范围**: Turn-end persistence, map updates, object archive updates, initialization to disk.

---

## 1) Hard Rules (Required)

- Only allow `append` or minimal `patch`; never rewrite entire files.
- `campaigns/<id>/sessions/` is the event source of truth: each turn must **append** a Decision to the current session file.
- Mutable state files (e.g., `campaigns/<id>/STATE_PANEL.md`, `campaigns/<id>/HOT_PACK.md`, `campaigns/<id>/PLAYER_PROFILE.md`, `campaigns/<id>/GOVERNANCE_PANEL.md`) only do chapter-level patches.
- If conflicts are found: use `campaigns/<id>/sessions/` as the standard, write a "correction note" in the current turn's Decision.

---

## 2) Format (HTML Comment Block)

At the end of the reply (invisible to players):

```md
<!-- ARCHIVE_DELTA
files:
  - path: campaigns/<id>/sessions/session_YYYY-MM-DD_slug.md
    append: |
      ## Decision: ...
      - Real time: ...
      - In-world time: ...
      - Player input: ...
      - Resolution: ...
      - Consequences: ...
      - Indicators: ...
      - Clocks: ...
  - path: campaigns/<id>/HOT_PACK.md
    patch: |
      <!-- CONTEXT_PACK_NEXT
      ...
      -->
-->
```

---

## 3) Recommended "Minimal Persistence Set" (at least per turn)

- `campaigns/<id>/sessions/<current>.md`: append Decision
- `campaigns/<id>/HOT_PACK.md`: patch latest `CONTEXT_PACK_NEXT`
- `campaigns/<id>/STATE_PANEL.md`: patch (only changed chapters)
- `campaigns/<id>/OBJECT_INDEX.md`: patch (only active pointer and 1-line summary)

Initialization turns also require:
- `campaigns/<id>/sessions/CURRENT_SESSION.md`: patch to point to new session file
- `campaigns/<id>/PLAYER_PROFILE.md`: patch preferences
- `campaigns/<id>/characters/PCs/pc_current.md`: patch character info

---

## 4) Patch Writing Suggestions (reduce ambiguity)

- Patches only include "new content of target chapter/table" (don't include whole-page copies).
- Table fields must remain stable (see `engine/mechanics/STATE_PANEL_SPEC.md`, `engine/mechanics/GOVERNANCE_PANEL_SPEC.md`).
