# NPC_GUIDELINES.md — NPC Consistency Constraints (Stable)

> **Purpose**: Constrain NPC "fundamental consistency" for turn execution and novel synchronization; specific content based on each NPC file.

---

## 1) Unbreakable Bottom Line

- Don't write NPC as character opposite to their "public identity/hidden agenda" (unless new session event triggers and records)
- Don't凭空 add key NPC facts (new facts must fall into `sessions/` Decision, then patch NPC file)
- Don't make "supernatural omniscient" inferences for NPC (unless file clearly marks as `entity` or equivalent)

---

## 2) Ground Truth and Update Process

- NPC ground truth: `characters/NPCs/npc_*.md`
- NPC index/alias entry: `characters/NPCs/npc_roster.md`
- Any change: First append Decision in `sessions/`, then patch NPC file (via `ARCHIVE_DELTA`)

