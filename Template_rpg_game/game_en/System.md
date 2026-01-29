# System.md — World Instance Router (Entry Point, No Kernel Details)

> **Purpose**: This world instance's "entry/routing" file: tells kernel where to read content packages and state.
> **Stable Kernel Protocol**: See `KERNEL_PROMPT.md` (turn pipeline, HUD, RAG, ARCHIVE_DELTA).

---

## 0) Hot Start (Recommended Entry Point)

Execute per `HOT_START.md`.

Minimum read set:
- `HOT_PACK.md`
- `PLAYER_PROFILE.md`
- `OBJECT_INDEX.md`
- `sessions/CURRENT_SESSION.md` → Corresponding `sessions/session_*.md` last Decision
- `STATE_PANEL.md`
- `index.md` (read only "next objective/pointer")

Initialization entry: `INIT_PROTOCOL.md`

---

## 1) World Instance: Content Package Entry (Variable)

### 1.1 State
- `STATE_PANEL.md` (player-visible persistent panel)
- `index.md` (navigation index/short summary)
- `lore/WORLD_STATE.md` (backend world state: indicators, clocks, complete clue index)
- `GOVERNANCE_PANEL.md` (governance panel: territory/followers/assets; optional)

### 1.2 Event
- `sessions/SESSION_INDEX.md`
- `sessions/session_*.md`

### 1.3 Setting Library (Canon/Mist)
- `lore/INDEX.md`
- `lore/CANON/*`
- `lore/MIST/*`
- `lore/MECHANICS/*`

### 1.4 Object Library (NPC/Location/Quest)
- `characters/PCs/*`
- `characters/NPCs/*`
- `quests/QUEST_LOG.md`
- `locations/LOCATION_INDEX.md`

### 1.5 Maps (Content Packages)
- `maps/MAP_INDEX.md`
- `maps/macro/*`, `maps/micro/*`, `maps/instances/*`

### 1.6 Derived Narrative (Writing)
- `Writing/PIPELINE.md`
- `Writing/Fiction_index.md`
- `Writing/Fiction_par*.md`

> Default: Turn execution doesn't read `Writing/` (unless player explicitly requests "write novel/align main text").

---

## 2) Input Protocol Entry

- Player input protocol: `CLI_SPEC.md`
- Rules retrieval gate: `mechanics/RAG_RULES.md`
- Rules directory index: `mechanics/INDEX.md`

---

## 3) Compatibility and History

- Old "kernel all-encompassing prompt" archived: `archive/System_legacy_2026-01-29.md`
- Saves are authoritative per `ARCHIVE_DELTA`; historical sessions may contain non-standard "save increment" paragraphs, **not as protocol**.
