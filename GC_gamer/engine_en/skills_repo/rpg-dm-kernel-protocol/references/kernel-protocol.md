# Kernel Protocol (Portable Reference)

This is the stable "DM kernel API" for filesystem-based text RPG projects.

## File layout assumptions

- HOT: `campaigns/<id>/STATE_PANEL.md`, latest `campaigns/<id>/sessions/session_*.md`, `campaigns/<id>/quests/QUEST_LOG.md`, `cartridges/<id>/locations/LOCATION_INDEX.md`, `campaigns/<id>/characters/PCs/*`
- Content packs: `cartridges/<id>/lore/`, `cartridges/<id>/characters/`, `cartridges/<id>/locations/`, `cartridges/<id>/quests/`
- Rules packs: `engine/mechanics/`
- Fiction (derived): `campaigns/<id>/Writing/`

## Conflict priority

`campaigns/<id>/sessions/` > state snapshots (`campaigns/<id>/STATE_PANEL.md` / `campaigns/<id>/index.md` / `campaigns/<id>/WORLD_STATE.md`) > object files (`cartridges/<id>/characters/` / `cartridges/<id>/quests/` / `cartridges/<id>/locations/`) > lore (`cartridges/<id>/lore/CANON`, `cartridges/<id>/lore/MIST`) > fiction (`campaigns/<id>/Writing/`).

## Turn pipeline (single agent)

1. Bootstrap minimal HOT state.
2. Parse player input (tag-style or command-style).
3. Fetch ≤3 tiny snippets (≤12 lines each), per RAG rules.
4. Resolve (roll only when needed; fail-forward; update indicators/clocks).
5. Output (Scene → Adjudication → Result → 5 suggestions → HUD → ARCHIVE_DELTA).
6. Optionally emit `CONTEXT_PACK_NEXT` (≤25 lines).
