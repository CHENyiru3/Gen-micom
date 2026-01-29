# Kernel Protocol (Portable Reference)

This is the stable “DM kernel API” for filesystem-backed text RPG projects.

## File layout assumptions

- HOT: `STATE_PANEL.md`, latest `sessions/session_*.md`, `quests/QUEST_LOG.md`, `locations/LOCATION_INDEX.md`, `characters/PCs/*`
- Content packs: `lore/`, `characters/`, `locations/`, `quests/`, `sessions/`
- Rules packs: `mechanics/`
- Fiction (derived): `Writing/`

## Conflict priority

`sessions/` > state snapshots (`STATE_PANEL.md` / `index.md` / `lore/WORLD_STATE.md`) > object files (`characters/` / `quests/` / `locations/`) > lore (`lore/CANON`, `lore/MIST`) > fiction (`Writing/`).

## Turn pipeline (single agent)

1. Bootstrap minimal HOT state.
2. Parse player input (tag-style or command-style).
3. Fetch ≤3 tiny snippets (≤12 lines each), per RAG rules.
4. Resolve (roll only when needed; fail-forward; update indicators/clocks).
5. Output (Scene → Adjudication → Result → 5 suggestions → HUD → ARCHIVE_DELTA).
6. Optionally emit `CONTEXT_PACK_NEXT` (≤25 lines).

