# ARCHIVE_DELTA.md — Incremental Save Spec (Stable)

> **Goal**: Externalize "memory/state" and make traceable; each turn only make minimum changes (append/patch), don't rewrite entire files.
> **Scope**: Turn-end persistence, map updates, object file updates, initialization persistence.

---

## 1) Hard Rules (Must)

- Only allow `append` or minimal `patch`; prohibit whole file rewrite.
- `sessions/` is event ground truth: Must **append** one Decision to current session file each turn.
- Variable state files (like `STATE_PANEL.md`, `HOT_PACK.md`, `PLAYER_PROFILE.md`, `GOVERNANCE_PANEL.md`) only do section-level patch.
- If conflict discovered: Use `sessions/` as authority, write "correction explanation" (in this turn's Decision).

---

## 2) Format (HTML Comment Block)

Output at end of reply (invisible to player):

```md
<!-- ARCHIVE_DELTA
files:
  - path: sessions/session_YYYY-MM-DD_slug.md
    append: |
      ## Decision: ...
      - Real time: ...
      - In-world time: ...
      - Player input: ...
      - Resolution: ...
      - Consequences: ...
      - Indicators: ...
      - Clocks: ...
  - path: HOT_PACK.md
    patch: |
      <!-- CONTEXT_PACK_NEXT
      ...
      -->
-->
```

---

## 3) Recommended "Minimum Persistence Set" (At least per turn)

- `sessions/<current>.md`: append Decision
- `HOT_PACK.md`: patch latest `CONTEXT_PACK_NEXT`
- `STATE_PANEL.md`: patch (only changed sections)
- `OBJECT_INDEX.md`: patch (only active pointers and 1-line summary)

Initialization turn also needs:
- `sessions/CURRENT_SESSION.md`: patch pointing to new session file
- `PLAYER_PROFILE.md`: patch preferences
- `characters/PCs/pc_current.md`: patch character info

---

## 4) Patch Writing Suggestions (Reduce Ambiguity)

- Patch only paste "target section/table" new content (don't夹杂 entire page copy).
- Table fields must remain stable (see `mechanics/STATE_PANEL_SPEC.md`, `mechanics/GOVERNANCE_PANEL_SPEC.md`).
