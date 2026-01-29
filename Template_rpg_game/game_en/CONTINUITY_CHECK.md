# CONTINUITY_CHECK.md — Session End Drift Verification Checklist

> **Purpose**: Verify that state files are consistent before session ends; prevent drift between `sessions/` (authoritative) and `STATE_PANEL.md`/`OBJECT_INDEX.md`.

---

## Pre-Flight Checklist (Before Ending Session)

### 1) Event Ground Truth Verification
- [ ] `sessions/<current>.md` has the latest Decision appended
- [ ] Decision includes: real time, in-world time, player input, resolution, consequences, indicators, clocks

### 2) State Panel Verification
- [ ] `STATE_PANEL.md` time matches latest Decision
- [ ] `STATE_PANEL.md` indicators (Grace/Debt/Rumor/Heat) reflect all changes
- [ ] `STATE_PANEL.md` quest status reflects all completed/updated quests
- [ ] `STATE_PANEL.md` NPC relations updated with new trust/status values
- [ ] `STATE_PANEL.md` clocks advanced to correct progress
- [ ] `STATE_PANEL.md` inventory reflects all gained/lost items
- [ ] `STATE_PANEL.md` key clues list is up to date
- [ ] `STATE_PANEL.md` location is current

### 3) Object Index Verification
- [ ] `OBJECT_INDEX.md` active location targets are accurate
- [ ] `OBJECT_INDEX.md` active quests are current
- [ ] `OBJECT_INDEX.md` active NPCs reflect who was encountered
- [ ] `OBJECT_INDEX.md` current PC points to correct file

### 4) Hot Pack Verification
- [ ] `HOT_PACK.md` contains valid `CONTEXT_PACK_NEXT`
- [ ] `CONTEXT_PACK_NEXT` reflects current state

### 5) Drift Correction (If Found)
If any inconsistency is found:
1. Use `sessions/` as the authoritative source
2. Write "correction explanation" in the session's final Decision
3. Patch `STATE_PANEL.md` / `OBJECT_INDEX.md` to match

---

## Session End Output Template

```markdown
<!-- SESSION_END_CHECK
verified:
  - sessions_last_decision: true/false
  - state_panel_time: true/false
  - state_panel_indicators: true/false
  - state_panel_quests: true/false
  - state_panel_npcs: true/false
  - state_panel_clocks: true/false
  - state_panel_inventory: true/false
  - state_panel_clues: true/false
  - state_panel_location: true/false
  - object_index: true/false
  - hot_pack: true/false
drift_corrections:
  - (list any corrections made)
-->
```
