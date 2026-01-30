---
name: rpg-dm-kernel-protocol
description: Run a filesystem-backed long-running RPG/DM session using HOT/WARM/COLD memory, short-code HUD, minimal RAG, and ARCHIVE_DELTA append/patch saves.
---

# RPG DM Kernel Protocol (Filesystem-Backed)

Use this skill when the user is playing a text RPG / asking you to act as DM, and the project stores memory/state in markdown files (e.g. `campaigns/<id>/index.md`, `campaigns/<id>/STATE_PANEL.json`, `campaigns/<id>/sessions/`, `cartridges/<id>/lore/`, `engine/mechanics/`).

## Hard rules (stable API)

- **Kernel ≠ content**: never embed world specifics into the kernel. Load them from content packs (files).
- **Minimal load**: prefer HOT summaries; WARM only when triggered; avoid COLD in-turn.
- **Never decide for the PC**: narrate, adjudicate, offer options.
- **Conflict priority**: `campaigns/<id>/sessions/` > `campaigns/<id>/STATE_PANEL.json`/`campaigns/<id>/index.md`/`campaigns/<id>/WORLD_STATE.md` > object files > `cartridges/<id>/lore/*` > `campaigns/<id>/Writing/*`.
- **Write only deltas**: emit `ARCHIVE_DELTA` (HTML comment) with `append`/`patch`; never rewrite whole files.

## Turn pipeline (single-agent)

1. **Bootstrap**: read minimal HOT state (time/location/indicators/clocks/active quest/NPC).
2. **Parse input**: accept either tag-style (`[行动]{...}`) or command-style (`@domain /cmd ...`); infer intent if missing.
3. **Fetch context**: load at most 3 tiny snippets (≤12 lines each), obeying repo `engine/mechanics/RAG_RULES.md`.
4. **Resolve**: roll only if necessary; show formula; fail-forward; update indicators + clocks when appropriate.
5. **Output**: Scene (2–4 sentences) → Adjudication → Result/Consequences → 5 next suggestions → HUD → ARCHIVE_DELTA.
6. **(Optional)** also emit `CONTEXT_PACK_NEXT` for next-turn paste.

## UI short codes (HUD)

Prefer: `L#` (location target), `N#` (NPC), `I#` (item/clue), `Q#` (quest), `F#` (faction).
Short codes are **UI-only** and **expire each turn**; bind them internally to stable IDs (`loc_*`, `npc_*`, `quest_*`, ...).

## References

- Turn protocol: see repo `KERNEL_PROMPT.md`
- Context pack schema: see repo `engine/mechanics/CONTEXT_PACK.md`
- State panel schema: see repo `engine/mechanics/skills_repo/rpg-dm-function-calling-local/references/panels.json`
- Retrieval rules: see repo `engine/mechanics/RAG_RULES.md`
