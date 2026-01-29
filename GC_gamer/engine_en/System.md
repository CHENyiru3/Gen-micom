# System.md — World Instance Router (Entry, Without Kernel Details)

> **Purpose**: This world instance's "entry/routing" file: tells kernel where to read content packs and states.
> **Stable Kernel Protocol**: See `engine/KERNEL_PROMPT.md` (turn pipeline, HUD, RAG, ARCHIVE_DELTA).

---

## 0) Hot Start (Recommended Entry)

Execute per `engine/HOT_START.md`.

Minimum read set:
- `ACTIVE.md`
- `campaigns/<id>/CAMPAIGN.md`
- `cartridges/<id>/CARTRIDGE.md`
- `campaigns/<id>/HOT_PACK.md`
- `campaigns/<id>/PLAYER_PROFILE.md`
- `campaigns/<id>/OBJECT_INDEX.md`
- `campaigns/<id>/sessions/CURRENT_SESSION.md` → Corresponding `campaigns/<id>/sessions/session_*.md` ending Decision
- `campaigns/<id>/STATE_PANEL.md`
- `campaigns/<id>/index.md` (only read "next goal/pointer")

Initialization entry: `engine/INIT_PROTOCOL.md`

---

## 1) World Instance: Content Pack Entry (Will Change)

### 1.1 State
- `campaigns/<id>/STATE_PANEL.md` (player-visible persistent panel)
- `campaigns/<id>/index.md` (navigation index/short summary)
- `campaigns/<id>/WORLD_STATE.md` (backend world state: indicators, clocks, complete clue index)
- `campaigns/<id>/GOVERNANCE_PANEL.md` (governance panel: territory/followers/assets; optional)

### 1.2 Event
- `campaigns/<id>/sessions/SESSION_INDEX.md`
- `campaigns/<id>/sessions/session_*.md`

### 1.3 Setting Library (Canon/Mist)
- `cartridges/<id>/lore/INDEX.md`
- `cartridges/<id>/lore/CANON/*`
- `cartridges/<id>/lore/MIST/*`
- `cartridges/<id>/lore/MECHANICS/*`

### 1.4 Object Library (NPC/Location/Quest)
- `campaigns/<id>/characters/PCs/*`
- `cartridges/<id>/characters/NPCs/*`
- `campaigns/<id>/quests/QUEST_LOG.md`
- `cartridges/<id>/locations/LOCATION_INDEX.md`

### 1.6 Maps (Content Packs)
- `cartridges/<id>/maps/MAP_INDEX.md`
- `cartridges/<id>/maps/macro/*`, `cartridges/<id>/maps/micro/*`, `campaigns/<id>/maps/runtime/*`

### 1.5 Derived Fiction (Writing)
- `campaigns/<id>/Writing/PIPELINE.md`
- `campaigns/<id>/Writing/Fiction_index.md`
- `campaigns/<id>/Writing/Fiction_par*.md`

> Default: Turn execution does not read `Writing/` (unless player explicitly requests "write novel/align main text").

---

## 2) Input Protocol Entry

- Player input protocol: `engine/CLI_SPEC.md`
- Rule retrieval gate: `engine/mechanics/RAG_RULES.md`
- Rule catalog index: `engine/mechanics/INDEX.md`

---

## 3) Compatibility and History

- Old "kernel comprehensive prompt" archived: `archive/System_legacy_2026-01-29.md`
- Archives follow `engine/ARCHIVE_DELTA.md`; historical sessions may have non-standard "archive increment" paragraphs, **not as protocol**.
