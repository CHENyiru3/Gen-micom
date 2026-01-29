# STATE_PANEL_SPEC.md — STATE_PANEL Stable Field Spec (Kernel Protocol)

> **Purpose**: Make `STATE_PANEL.md` patchable incrementally, stably retrievable, run long-term without drift.
> **Principle**: Field structure stable; content variable; avoid duplicate paragraphs and free expansion.

---

## 1) Sections and Order (Must Be Fixed)

`STATE_PANEL.md` must appear in following first-level heading order (can be empty, but cannot be missing):

1. `## Time`
2. `## Indicators`
3. `## Quests`
4. `## NPC Relations`
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
ID recommends using HUD side `Q#` (like `Q1`) or stable `quest_*` (choose one, but long-term consistent).

### 2.4 NPC Relations
Table header fixed as: `| Name | Status | Trust |`

### 2.5 Clocks
Table header fixed as: `| Clock | Progress | Note |`
Progress recommends stable symbols (like `⚪○○○○`) or `X/Y` (choose one, but long-term consistent).

---

## 3) Maintenance Constraints (Mandatory)

- **No duplication**: `## Key Clues` can appear only once.
- **No bloat**: Inventory recommends ≤12 lines; clues recommend ≤12 items.
- **Patchable**: When updating, only change corresponding section, don't rewrite entire file.
- **Traceable**: Each major change should leave trace in latest `sessions/session_*.md` Decision (via `ARCHIVE_DELTA` append).

