# INIT_PROTOCOL.md — Initialization Protocol (Blank Campaign → Playable)

> **Goal**: Have users customize character and play preferences, and externalize these preferences into "stable data" for DM personalization and context compression.
> **Kernel**: Turn execution still follows `KERNEL_PROMPT.md`; this file only defines "how initialization persists".
>
> **Recommended Flow (Two-Phase)**: collect Step A/B/C answers and confirm summary → then AI outputs **JSON tool_calls** to run `init_campaign` for persistence (JSON keys mapping see §1.1).

---

## 0) Initialization Products (Must Persist)

After initialization completes, must exist and remain patchable:

- Player preferences (stable): `campaigns/<id>/PLAYER_PROFILE.md`
- PC档案 (stable): `campaigns/<id>/characters/PCs/pc_current.md`
- Session 0 switched: Create `campaigns/<id>/sessions/session_YYYY-MM-DD_<slug>.md`, and patch `campaigns/<id>/sessions/CURRENT_SESSION.md`
- State panel filled: `campaigns/<id>/STATE_PANEL.json`
- Hot start package written: `campaigns/<id>/HOT_PACK.json` (`CONTEXT_PACK_NEXT`)
- DM planner file exists: `.DM_PLANNER.md` (hidden, not revealed to players)
- **Mainline blueprint exists**: `campaigns/<id>/.DM_BLUEPRINT.md` (main arcs / key NPCs / relations)
- **Mainline panel exists**: `campaigns/<id>/MAINLINE_PANEL.json`

---

## 1) Initialization Interaction Steps (Recommended 3 Turns Complete)

> **Recommended Execution (Two-Phase)**:
> collect Step A/B/C answers and confirm summary → then AI outputs JSON tool_calls to run `init_campaign` for persistence.

### Step A: Preferences and Safety (OOC)

Ask and write to `campaigns/<id>/PLAYER_PROFILE.md`:
- Narrative style: Realistic/Epic/Black Humor/Horror concentration
- Rule strength: Rules-first/Narrative-first/Compromise
- Difficulty and forgiveness: Easy/Standard/Hardcore; failure forward intensity
- Pacing: Fast/Medium/Slow; combat frequency
- Content boundaries: Taboos/fade/acceptable range (optional)

When outputting, simultaneously give "preference summary" (≤8 lines, using `KEY=VALUE`), facilitating quick loading and compression each turn.

#### Quick Presets (User-Friendly)

User can directly select a preset, AI auto-fills unfilled fields:
- `PRESET=轻松叙事` / `PRESET=Easy Narrative`: Weak rules, mild consequences, fast pace, less combat
- `PRESET=标准冒险` / `PRESET=Standard Adventure`: Compromise, medium pace, combat
- `PRESET=硬核写实` / `PRESET=Hardcore Realistic`: Strong rules, strong costs, high resource pressure, less but dangerous combat
- `PRESET=悬疑调查` / `PRESET=Mystery Investigation`: Investigation priority, low combat, high clue density
- `PRESET=宗教恐怖` / `PRESET=Religious Horror`: High horror concentration, frequent sanctuaries/omens, medium to strong costs

### Step B: PC Creation (OOC → Character)

Ask and write to `campaigns/<id>/characters/PCs/pc_current.md`:
- Name/address/pronouns (optional)
- Identity archetype (1 sentence)
- Drive (1-2 items)
- 2 strengths + 1 weakness (for adjudication and style)
- Key background hook (1 item, for DM to generate quests)
- Starting equipment/resource preference (lightweight)

### Step C: Opening Choice (Soft Router)

Let player choose from 2-3 "opening hooks" (compatible with world setting, but not bound to old plot).

After completion:
- Create new session file and write `Decision: Initialization` (append)
- Patch `campaigns/<id>/sessions/CURRENT_SESSION.md` pointing to new file
- Patch `campaigns/<id>/STATE_PANEL.json`: Time/location/indicators initialization, empty quest table, empty clock table
- Patch `campaigns/<id>/HOT_PACK.json` writing first `CONTEXT_PACK_NEXT`
- Patch `campaigns/<id>/MAINLINE_PANEL.json` (write mainline status)

### Step D: Mainline Blueprint (Backstage, Mandatory)
Generate a backstage outline based on **world setting + player preferences** (not shown to players):
- 2–4 mainline arcs (1 sentence each)
- 5–8 key NPCs (name / stance / relation)
- Core conflicts & themes (2–4 items)
- Relation graph (up to 8 edges, A—relation—B)
- Variant space: swappable side entrances (2–3 items)

Write to `campaigns/<id>/.DM_BLUEPRINT.md`, and inject a 4–6 line **SPINE summary** at the top of `HOT_PACK.json` (≤6 lines):
```
SPINE:
- Arc 1…
- Arc 2…
KEY_NPCS: A, B, C
THEME: ...
```

---

## 1.1) Initialization Answer → Persistence Parameter Mapping (For AI/Agent)

`campaign_manager.py init` supports two inputs:
- **Command line arguments**: Suitable for direct execution
- **JSON answers file**: `python3 scripts/campaign_manager.py init --from answers.json` (command line > JSON for parameter priority)

JSON keys (suggest all use snake_case):

### Time and Session
- `date` → `campaigns/<id>/sessions/session_YYYY-MM-DD_<slug>.md`, `campaigns/<id>/STATE_PANEL.json`, `campaigns/<id>/HOT_PACK.json`
- `slug` → session filename `<slug>` (if not given, generated from `pc_name`+`start_loc`)

### Preferences (write to `campaigns/<id>/PLAYER_PROFILE.md` "preference summary")
- `preset` (optional): `轻松叙事` / `Easy Narrative` / `标准冒险` / `Standard Adventure` / `硬核写实` / `Hardcore Realistic` / `悬疑调查` / `Mystery Investigation` / `宗教恐怖` / `Religious Horror`
- `style` → `STYLE=...`
- `difficulty` → `DIFFICULTY=...`
- `rules` → `RULES=...`
- `pacing` → `PACING=...`
- `combat_freq` → `COMBAT_FREQ=...`
- `mystery_vs_action` → `MYSTERY_VS_ACTION=...`
- `lines_veils` → `LINES_VEILS=...`

### PC (write to `campaigns/<id>/characters/PCs/pc_current.md` table)
- `pc_name` (required)
- `pc_archetype`
- `pc_drive`
- `pc_strengths`
- `pc_weakness`
- `pc_bg_hook`

### Opening (write to `campaigns/<id>/STATE_PANEL.json` / `campaigns/<id>/HOT_PACK.json` / session Decision)
- `start_loc`
- `start_hook`

---

## 2) Context Compression Strategy (Required)

Each turn only needs to carry 1 line from preferences:
- Copy 1 line from `campaigns/<id>/PLAYER_PROFILE.md`'s "preference summary" to `campaigns/<id>/HOT_PACK.json`'s `flags` (e.g., `STYLE=Realistic-High-Pressure-Investigation-Priority`)

Other preference details are only read again when "style significantly deviates / player modifies preferences".
