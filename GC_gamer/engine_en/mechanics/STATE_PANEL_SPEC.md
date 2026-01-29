# STATE_PANEL_SPEC.md — STATE_PANEL Stable Field Specification (Kernel Protocol)

> **Purpose**: Allow `campaigns/<id>/STATE_PANEL.md` to be incrementally patchable, stably retrievable, long-term run without drift.
> **Principle**: Field structure stable; content variable; avoid duplicate paragraphs and free expansion.

---

## 1) Chapters and Order (Must Be Fixed)

`campaigns/<id>/STATE_PANEL.md` must appear in the following H2 order (can be empty, but cannot be missing):

1. `## Time`
2. `## Indicators`
3. `## Quests`
4. `## NPC Relationships`
5. `## Clocks`
6. `## Inventory`
7. `## Key Clues`
8. `## Location`

> Allowed to append: `## Notes` (at end; optional).

---

## 2) Table Fields (Must Be Stable)

### 2.1 Time
Table header fixed as: `| Date | Season | Special Date |`

### 2.2 Indicators
Table header fixed as: `| Grace | Debt | Rumor | Heat |`

### 2.3 Quests
Table header fixed as: `| ID | Quest | Status |`
ID recommended to use HUD-side `Q#` (e.g., `Q1`) or stable `quest_*` (choose one, but must be long-term consistent).

### 2.4 NPC Relationships
Table header fixed as: `| Name | Status | Trust |`

### 2.5 Clocks
Table header fixed as: `| Clock | Progress | Description |`
Progress recommended to use stable symbols (e.g., `⚪○○○○`) or `X/Y` (choose one, but must be long-term consistent).

---

## 3) Maintenance Constraints (Mandatory)

- **No duplication**: `## Key Clues` can only appear once.
- **No expansion**: Inventory suggestion ≤12 lines; clues suggestion ≤12 lines.
- **Patchable**: When updating, only change corresponding chapter, not rewrite entire file.
- **Traceable**: Each major change should leave trace in latest `campaigns/<id>/sessions/session_*.md` Decision (via `ARCHIVE_DELTA` append).
