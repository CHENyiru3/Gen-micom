# System.md — World Instance Router (Entry, Without Kernel Details)

> **Purpose**: This world instance's "entry/routing" file: tells kernel where to read content packs and states.
> **Stable Kernel Protocol**: See `engine/KERNEL_PROMPT.md` (turn pipeline, HUD, RAG, ARCHIVE_DELTA).
> **Role split**: See `engine/ROLE_SYSTEMS.md` (AUTHOR/BUILDER/DM scopes).  
> **Role entry**: `engine/System_AUTHOR.md` / `engine/System_BUILDER.md` / `engine/System_DM.md` / `engine/System_SAVE_READ.md`  
> **Cheatsheet**: `engine/ROLE_ENTRY.md`

---

## 0) Hot Start (Recommended Entry)

Execute per `engine/HOT_START.md`.

Minimum read set:
- `ACTIVE.md`
- `campaigns/<id>/CAMPAIGN.md`
- `cartridges/<id>/CARTRIDGE.md`
- `campaigns/<id>/HOT_PACK.md`
- `campaigns/<id>/PLAYER_PROFILE.md`
- `campaigns/<id>/characters/PCs/pc_current.md`
- `campaigns/<id>/OBJECT_INDEX.md`
- `campaigns/<id>/sessions/CURRENT_SESSION.md` → Corresponding `campaigns/<id>/sessions/session_*.md` ending Decision
- `campaigns/<id>/STATE_PANEL.md`
- `campaigns/<id>/index.md` (only read "next goal/pointer")

Initialization entry: `engine/INIT_PROTOCOL.md`

---

## 0.1 Output Pacing (Information Control)

- **Allow no‑discovery / no‑progress**: most routine checks should end with “no new findings.”
- **Fail‑forward only with explicit risk**: use failure‑as‑progress only when clear cost/threat exists.
- **If no discovery**: explicitly state “no key clues / no new progress,” with a plausible reason (visibility / obstruction / time / noise / misread).

---

## 0.2 User Guide Prompt (Once Only)

- After each new/load campaign: if `guide_shown` in `HOT_PACK.md` is empty or `0`, output a **one‑time** short user guide.
- After output, write back `guide_shown=1` to `HOT_PACK.md` via ARCHIVE_DELTA patch.

---

## 0.3 Load Consistency (Anti‑hallucination)

- **No new facts on load/continue**: recovery output must only restate `*_snapshot.md` + `HOT_PACK.md`.
- **Do not invent** new clues/NPCs/locations/text; if missing, say “not recorded / requires player action”.
- **Recovery output must be labeled as “Load Summary”**, and must not advance the plot.

## 0.4 Style Consistency (Anti‑Drift)

- Narrative output must follow the **Fixed Narrative Style** in `engine/KERNEL_PROMPT.md`.
- **On load/continue, never change writing style or formatting**: keep sectioned paragraphs, check block, result table, and action tail.

## 0.5 Role Entry (Mandatory)

Declare role at the start of each run:
- `ROLE=AUTHOR` (cartridge content author)
- `ROLE=BUILDER` (campaign builder)
- `ROLE=DM` (runtime host)

Scopes and restrictions are defined in `engine/ROLE_SYSTEMS.md`.

## 0.6 Cartridge Boundary (Required)

- New cartridges must be **sibling** to template: `Game_Cartridge/<cartridge_root>/game_cn/`
- **Never** create new cartridges/campaigns inside `Game_Cartridge/Blank_Cartidge_template/`

---

## 1) World Instance: Content Pack Entry (Will Change)

### 1.1 State
- `campaigns/<id>/STATE_PANEL.md` (player-visible persistent panel)
- `campaigns/<id>/index.md` (navigation index/short summary)
- `campaigns/<id>/WORLD_STATE.md` (backend world state: indicators, clocks, complete clue index)
- `campaigns/<id>/GOVERNANCE_PANEL.md` (governance panel: territory/followers/assets; optional)

### 1.2 Event
- `campaigns/<id>/sessions/SESSION_INDEX.md`
- `campaigns/<id>/sessions/session_YYYY_Name_compressed.md` (compressed summary)
- `campaigns/<id>/sessions/session_YYYY_Name_snapshot.md` (save snapshot)

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

## 3) Output Protocol (Critical)

### Dual-Channel Output Rules

**Every story progression must execute simultaneously:**

1. **Write to MD file** - Persist story progression to `sessions/session_*.md`
2. **Output to dialogue** - Display in CLI (users cannot see MD file content)

**Format Requirements**:
- MD file: Follow `session_*.md` format, record complete story segments
- Dialogue output: Highlight key scenes + player action menu

### Session Compression & Rebuild (Mandatory)

**Goal**: keep runtime context minimal to prevent token inflation.

- Runtime uses: `*_snapshot.md`
- Compressed: `*_compressed.md`

**Recursive compression (each turn end)**:
1. Compress all history **before last turn** → `session_YYYY_Name_compressed.md`
2. Keep **last turn + current turn** uncompressed → `session_YYYY_Name_snapshot.md`
3. `SESSION_INDEX.md` points only to latest **snapshot**

**Dialogue reference constraint**:
- Dialogue reads only `*_snapshot.md` + `HOT_PACK.md`
- `*_compressed.md` is consulted only on explicit backstory request

### Turn End Checklist

**Must execute ALL steps in order at the end of each dialogue round:**

1. [ ] Write session MD (record actions and results)
2. [ ] Update STATE_PANEL.md (indicators, NPCs, clues, clocks)
3. [ ] Update HOT_PACK.md (context pack)
4. [ ] Output scene summary + available actions in dialogue
5. [ ] Show HUD shortcode menu (if interactive objects exist)
6. [ ] **Compress history before last turn (*_compressed.md)** (MANDATORY)
7. [ ] **Generate snapshot (last + current turn, *_snapshot.md) and update SESSION_INDEX.md** (MANDATORY)

> ⚠️ Compression steps 6-7 are **MANDATORY** and cannot be skipped, otherwise token usage will grow infinitely.

---

## 4) Context Compression Protocol (Mandatory)

### 4.1 Session File Structure (Two-file)

Each session uses a recursive two‑file structure:

```
session_YYYY_Name_compressed.md  ← Summary (multi‑round)
session_YYYY_Name_snapshot.md    ← Current runtime snapshot
```

### 4.2 Compression Timing

**Must execute each turn end**:
- Compress history before last turn (*_compressed.md)
- Update snapshot (keep last + current turn uncompressed, *_snapshot.md)

### 4.3 Compression Rules

**Summary Keep Content**:
- Core Decision (decision point)
- Key events (1-5 items)
- NPCs and relationships
- Clue list
- Status changes (indicators/clocks)

**Delete Content**:
- Long internal monologues
- Repeated dialogue details
- Scene descriptions (keep key info only)

### 4.4 Session File Naming

Unified as:
- `session_YYYY_Name_compressed.md`
- `session_YYYY_Name_snapshot.md`

### 4.5 Mandatory Checkpoints

In the turn end checklist:

- [ ] *_compressed.md generated
- [ ] *_snapshot.md generated
- [ ] Dialogue references *_snapshot.md only
- [ ] Do not keep full dialogue files
