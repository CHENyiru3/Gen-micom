# Chronicles of the Misty Border: The Transient (Engineered Tabletop RPG Repo)

This repository externalizes "long-term memory/state/settings" as files, with the LLM acting only as a turn executor, ensuring:
- Restartability (can recover even with zero context)
- Traceability (all key events in `campaigns/<id>/sessions/`)
- Compressibility (hot cache reads only a few files)

---

## 1) Quick Start (New Campaign)

1. Send: `<initialize>` (entry first reads `engine/System.md`)
2. Complete two types of configuration per `engine/INIT_PROTOCOL.md`:
   - Player preferences: write to `campaigns/<id>/PLAYER_PROFILE.md`
   - Player character: write to `campaigns/<id>/characters/PCs/pc_current.md`
3. Initialization creates a new session and updates:
   - `campaigns/<id>/sessions/CURRENT_SESSION.md`
   - `campaigns/<id>/STATE_PANEL.md`
   - `campaigns/<id>/HOT_PACK.md`
   - `campaigns/<id>/OBJECT_INDEX.md`

> The current repository has been reset to "blank campaign". Old campaign archived: `archive/campaign_clermond_2026-01-29/`

---

## 0) Campaign Directory (Core vs Save Separation)

This repository separates "reusable core" from "each campaign's save/state":

- **Engine (shared)**: `engine/` (symlink here, actual location in `GC_gamer/engine_en/`)
- **Cartridge (world content)**: `cartridges/<cartridge_id>/...`
- **Template Cartridge**: `../../Blank_Cartidge_template/game_cn/cartridges/template/` (starting point for all new cartridges)
- **Campaign (one per campaign)**: `campaigns/<campaign_id>/...`

Current active campaign: `ACTIVE.md`

Minimal steps to switch campaign:
1) Update `ACTIVE.md` to point to new directory
2) Update target campaign `CAMPAIGN.md` cartridge binding (if needed)

### Automation (Recommended)

```bash
python3 engine/scripts/campaign_manager.py new --id campaign_0002
python3 engine/scripts/campaign_manager.py switch --path campaigns/campaign_0001
```

See: `engine/CAMPAIGN_PROTOCOL.md`

### User-Friendly Method (No Need to Run Python)

You only need to input control commands in conversation, AI will execute scripts and file changes for you:
- `<new campaign campaign_0002>`: Create and switch to new campaign (entry first reads `engine/System.md`)
- `<switch campaign campaigns/campaign_0001>`: Switch to existing campaign (entry first reads `engine/System.md`)
- `<initialize>`: Run initialization wizard in current campaign (entry first reads `engine/System.md`)

---

## 3.1 Conversation Command Entry Convention (Unified Entry)

The following commands all first read `engine/System.md` as entry router, then read corresponding protocol files:
- `<initialize>` → `engine/INIT_PROTOCOL.md`
- `<new campaign ...>` / `<switch campaign ...>` → `engine/CAMPAIGN_PROTOCOL.md`
- `<continue>` / `<hot start>` → `engine/HOT_START.md`

---

## 2) What is Hot Cache and How to Use

Hot cache goal: Continue playing each turn/restart by reading the fewest files.

You only need to know two files:
- `campaigns/<id>/HOT_PACK.md`: **Next turn context package** (contains only 1 `CONTEXT_PACK_NEXT` comment block)
- `campaigns/<id>/OBJECT_INDEX.md`: **Active object index** (NPC/quest/location/map "pointer + 1-line summary")

Usually players don't need to manually edit them; they should be automatically patched by each turn's `ARCHIVE_DELTA` output.

See specifications:
- `engine/mechanics/CONTEXT_PACK.md`
- `engine/ARCHIVE_DELTA.md`

---

## 3) Hot Start (Recovery/Continue)

When changing devices/new window/context lost, execute per `engine/HOT_START.md` (recommended to directly send `<continue>` or `<hot start>`).
Unified entry: First read `engine/System.md`, then load per `HOT_START.md` order.

Hot start reading order (conceptually):
1. `campaigns/<id>/HOT_PACK.md`
2. `campaigns/<id>/PLAYER_PROFILE.md` (only read "preference summary")
3. `campaigns/<id>/OBJECT_INDEX.md`
4. `campaigns/<id>/sessions/CURRENT_SESSION.md` → Last 1-3 Decisions in current session file
5. `campaigns/<id>/STATE_PANEL.md`
6. `campaigns/<id>/index.md` (only read navigation)

If repository not yet initialized, prompts to re-`<initialize>`.

---

## 4) How to Interact Efficiently with AI (Strongly Recommended)

### 4.1 Use Tags to Input, Reduce Ambiguity

Prefer using `engine/CLI_SPEC.md` command headers:
- `[ACT]` / `[LOOK]` / `[ASK]` / `[FIGHT]` / `[CAST]` / `[MANAGE]` / `[OOC]`

### 4.2 Copy HUD Short Codes, Reduce Match Failures

Each turn AI gives HUD (`L# / N# / I# / Q#`). You can directly reference:
- `[ACT]{Talk to N1}`
- `[ACT]{Investigate L2}`

### 4.3 OOC Rules/Protocol Questions

Use `[OOC]` to ask, and have AI point to specific file as authoritative source (avoid drift).

---

## 5) Story Preference Optimization (Personalized DM)

Preference file: `campaigns/<id>/PLAYER_PROFILE.md`

Usage:
- Fill during initialization (recommended)
- You can also OOC modify preferences anytime (e.g., "more horror/faster pace/less combat"), AI will patch `campaigns/<id>/PLAYER_PROFILE.md`

Context compression strategy:
- Each turn only need to compress 1 line from preference summary (e.g., `STYLE=...`) into `campaigns/<id>/HOT_PACK.md flags=`, others not read often.

---

## 6) Stable Sources of Truth (Don't Mix)

- Kernel protocol (how to run): `engine/KERNEL_PROMPT.md`
- World entry (pointer/routing): `engine/System.md`
- Event source (history): `campaigns/<id>/sessions/`
- Player-side state panel: `campaigns/<id>/STATE_PANEL.md`
- Backend world state index: `campaigns/<id>/WORLD_STATE.md`
- Incremental archive specification: `engine/ARCHIVE_DELTA.md`
- Session end drift check: `engine/CONTINUITY_CHECK.md`

---

## 7) Hidden DM Files (Enhance Experience: Suspense/Planning/Behind-the-Scenes Motivation)

These files belong to DM/AI's behind-the-scenes tools, **strictly prohibited to directly reference or spoiler in player-visible output**:

- `.DM_SECRETS.md`: Unrevealed truth/behind-settings (migrate to `campaigns/<id>/sessions/` and content packs after triggered)
- `.DM_PLANNER.md`: Story planning and suspense engine (mainline/Fronts/clue inventory/twists/next session beats)

They are stored with the campaign: `campaigns/<id>/` (no longer using root subdirectory).

---

## 8) Now Start Creating New Cartridge Story

1. Copy `../../Blank_Cartidge_template/game_cn/cartridges/template/` → `cartridges/<new_card_id>/` (maintain lore/locations/quests/characters/maps structure).
2. Edit `cartridges/<new_card_id>/CARTRIDGE.md`: Complete `routes`, `aliases`, `invariants` and `feature_flags` for enabled features (like maps/fiction/governance).
3. Use `python3 engine/scripts/campaign_manager.py new --id campaigns/<new_campaign>` to create new campaign.
4. Modify the new campaign's `CAMPAIGN.md` `cartridge_id` to the newly created `<new_card_id>` and lock `cartridge_version_lock`.
5. Switch to that campaign (`<switch campaigns/<new_campaign>`), all Engine modules continue sharing, world provided by new cartridge.
