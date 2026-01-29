# INIT_PROTOCOL.md — Initialization Protocol (Blank Campaign → Playable)

> **Goal**: Let users customize character and play preferences, and externalize these preferences as "stable data" for DM personalization and context compression.
> **Kernel**: Turn execution still follows `KERNEL_PROMPT.md`; this file only defines "how initialization persists".
>
> **Recommended Flow (Two-Phase)**: Use dialogue to collect Step A/B/C answers and confirm summary first → then AI automatically executes `python3 scripts/campaign_manager.py init ...` to persist. Supports `--from answers.json` to import JSON-format answers (JSON keys mapping see §1.1).

---

## 0) Initialization Outputs (Must Persist)

After initialization completes, must exist and remain patchable:

- Player preferences (stable): `PLAYER_PROFILE.md`
- PC file (stable): `characters/PCs/pc_current.md`
- Session 0 switched: Create `sessions/session_YYYY-MM-DD_<slug>.md`, patch `sessions/CURRENT_SESSION.md`
- State panel populated: `STATE_PANEL.md`
- Hot start package written: `HOT_PACK.md` (`CONTEXT_PACK_NEXT`)
- DM planning file exists: `.DM_PLANNER.md` (hidden, not exposed to players)

---

## 1) Initialization Interaction Steps (Recommend 3 Turns)

### Step A: Preferences and Safety (OOC)
Ask and write to `PLAYER_PROFILE.md`:
- Narrative style: Realistic/Epic/Black Humor/Horror intensity
- Rule strength: Rules First/Narrative First/Balanced
- Difficulty and forgiveness: Easy/Standard/Hardcore; failure-forward intensity
- Pace: Fast/Medium/Slow; combat frequency
- Content boundaries: Taboos/diminishment/acceptable range (optional)

Also output "preference summary" (≤8 lines, using `KEY=VALUE`) for quick turn loading and compression.

#### Quick Presets (User-Friendly)

Users can directly select a preset; AI auto-fills unspecified fields:
- `PRESET=轻松叙事` (Easy Narrative): Weak rules, gentle consequences, fast pace, less combat
- `PRESET=标准冒险` (Standard Adventure): Balanced, medium pace, moderate combat
- `PRESET=硬核写实` (Hardcore Realistic): Strong rules, strong consequences, high resource pressure, less but dangerous combat
- `PRESET=悬疑调查` (Mystery Investigation): Investigation priority, low combat, high clue density
- `PRESET=宗教恐怖` (Religious Horror): High horror intensity, frequent sanctuaries/visions, medium-strong consequences

### Step B: PC Creation (OOC → Character)
Ask and write to `characters/PCs/pc_current.md`:
- Name/address/pronouns (optional)
- Identity archetype (1 sentence)
- Motivations (1-2 items)
- 2 strengths + 1 weakness (for adjudication and style)
- Key background hook (1 item, for DM quest generation)
- Starting equipment/resource preference (lightweight)

### Step C: Opening Choice (Soft Routing)
Let player choose from 2-3 "opening hooks" (compatible with world setting, not bound to old storylines).

After completion:
- Create new session file and write `Decision: 初始化` (append)
- Patch `sessions/CURRENT_SESSION.md` pointing to new file
- Patch `STATE_PANEL.md`: time/location/indicators initialization, empty quest table, empty clock table
- Patch `HOT_PACK.md` writing first `CONTEXT_PACK_NEXT`

---

## 1.1) Initialization Answer → Persistence Parameter Mapping (for AI/Agent)

`campaign_manager.py init` supports two input modes:
- **Command-line arguments**: Suitable for direct execution
- **JSON answer file**: `python3 scripts/campaign_manager.py init --from answers.json` (command-line > JSON priority)

JSON keys (recommend snake_case):

### Time & Session
- `date` → `sessions/session_YYYY-MM-DD_<slug>.md`, `STATE_PANEL.md`, `HOT_PACK.md`
- `slug` → session filename `<slug>` (if not provided, generated from `pc_name`+`start_loc`)

### Preferences (write to `PLAYER_PROFILE.md` "preference summary")
- `preset` (optional): `轻松叙事` / `标准冒险` / `硬核写实` / `悬疑调查` / `宗教恐怖`
- `style` → `STYLE=...`
- `difficulty` → `DIFFICULTY=...`
- `rules` → `RULES=...`
- `pacing` → `PACING=...`
- `combat_freq` → `COMBAT_FREQ=...`
- `mystery_vs_action` → `MYSTERY_VS_ACTION=...`
- `lines_veils` → `LINES_VEILS=...`

### PC (write to `characters/PCs/pc_current.md` table)
- `pc_name` (required)
- `pc_archetype`
- `pc_drive`
- `pc_strengths`
- `pc_weakness`
- `pc_bg_hook`

### Opening (write to `STATE_PANEL.md` / `HOT_PACK.md` / session Decision)
- `start_loc`
- `start_hook`

---

## 2) Context Compression Strategy (Mandatory)

Each turn only need to carry 1 line from preferences:
- Copy 1 line from `PLAYER_PROFILE.md` "preference summary" to `HOT_PACK.md` `flags` (e.g., `STYLE=Realistic-HighPressure-InvestigationPriority`)

Other preference details only read when "style significantly deviates/player modifies preferences".
