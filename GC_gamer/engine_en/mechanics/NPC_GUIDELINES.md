# NPC_GUIDELINES.md — NPC Consistency Constraints (Stable)

> **Purpose**: Constrain NPC "baseline consistency" for turn execution and novel synchronization; specific content based on each NPC file.

---

## 1) Irreversible Bottom Line

- Do not write NPCs as characters contrary to their "public identity/goals/hidden goals" (unless new session events trigger and record)
- Do not arbitrarily add key facts to NPCs (new facts must first fall into `campaigns/<id>/sessions/` Decision, then patch NPC file)
- Do not make "supernatural omniscient" inferences for NPCs (unless their file explicitly marks as `entity` or equivalent)

---

## 2) Source of Truth and Update Process

- NPC source of truth: `cartridges/<id>/characters/NPCs/npc_*.md`
- NPC index/alias entry: `cartridges/<id>/characters/NPCs/npc_roster.md`
- Any changes: First append Decision in `campaigns/<id>/sessions/`, then patch NPC file (via `ARCHIVE_DELTA`)
