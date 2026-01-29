# Chronicle of the Mist Frontier: Flux (Engineering TTRPG Repo)

This repository externalizes "long-term memory/state/settings" to files, with the LLM acting only as a turn executor, ensuring:
- Restartable (recoverable even with zeroed context)
- Traceable (all key events in `sessions/`)
- Compressible (hot cache reads only a few files)

---

## 1) Quick Start (New Campaign)

1. Send: `<Initialize>`
2. Complete two configurations per `INIT_PROTOCOL.md`:
   - Player preferences: Write to `PLAYER_PROFILE.md`
   - Player character: Write to `characters/PCs/pc_current.md`
3. Initialization creates a new session and updates:
   - `sessions/CURRENT_SESSION.md`
   - `STATE_PANEL.md`
   - `HOT_PACK.md`
   - `OBJECT_INDEX.md`

> The repository is now reset to a "blank campaign." Old campaign archived: `archive/campaign_clermond_2026-01-29/`

---

## 0) Campaign Directory (Core vs. Save Separation)

This repository separates "reusable core" from "per-campaign save/state":

- **Core (Shared)**: `KERNEL_PROMPT.md`, `mechanics/`, `lore/`, `maps/`, `Char.md`, `Map-Gen.md`, etc.
- **Campaign (One per campaign)**: `campaigns/<campaign_id>/...`

Current active campaign: `CURRENT_CAMPAIGN.md`

For backward compatibility, the following root paths are **symbolic links** (pointing to current campaign):
- `sessions/`, `quests/`, `characters/`, `Writing/`
- `STATE_PANEL.md`, `HOT_PACK.md`, `OBJECT_INDEX.md`, `PLAYER_PROFILE.md`, `GOVERNANCE_PANEL.md`, `.DM_SECRETS.md`

Minimum steps to switch campaigns:
1) Update `CURRENT_CAMPAIGN.md` to point to new directory
2) Rebuild the above symbolic links (keep "root path unchanged")

### Automation (Recommended)

```bash
python3 scripts/campaign_manager.py new --id campaign_0002
python3 scripts/campaign_manager.py switch --path campaigns/campaign_0001
```

See: `CAMPAIGN_PROTOCOL.md`

### User-Friendly Method (No Python Required)

Simply enter control commands in conversation; the AI will execute scripts and file changes for you:
- `<New campaign campaign_0002>`: Create and switch to new campaign
- `<Switch campaign campaigns/campaign_0001>`: Switch to existing campaign
- `<Initialize>`: Run initialization wizard in current campaign (character + preferences)

---

## 2) What is Hot Cache (HOT) and How to Use It

Hot cache goal: Each turn/restart only reads the minimum files to continue playing.

You only need to know two files:
- `HOT_PACK.md`: **Next turn context package** (contains only 1 `CONTEXT_PACK_NEXT` comment block)
- `OBJECT_INDEX.md`: **Active object index** (NPC/quest/location/map "pointers + 1-line summary")

Players typically don't need to edit them manually; they should be auto-patched by each turn's `ARCHIVE_DELTA` output.

Specs:
- `mechanics/CONTEXT_PACK.md`
- `ARCHIVE_DELTA.md`

---

## 3) Hot Start (Resume/Continue)

When changing devices/new window/context lost, execute per `HOT_START.md` (recommend sending `<Hot Start>` or `<Continue>` directly).

Hot start read order (conceptual):
1. `HOT_PACK.md`
2. `PLAYER_PROFILE.md` (read only "preference summary")
3. `OBJECT_INDEX.md`
4. `sessions/CURRENT_SESSION.md` → Last 1-3 Decisions in current session file
5. `STATE_PANEL.md`
6. `index.md` (read only navigation)

If repository not yet initialized, prompts to `<Initialize>` again.

---

## 4) How to Interact with AI Efficiently (Strongly Recommended)

### 4.1 Use Tag Input to Reduce Ambiguity

Prefer using tags from `CLI_SPEC.md`:
- `[Action]{...}` / `[Dialogue]"..."` / `[Investigation]{...}` / `[Combat]{...}` / `[Management]{...}` / `[Inner]{...}` / `<OOC>...`

### 4.2 Copy HUD Shortcodes to Reduce Match Failures

Each turn AI provides HUD (`L# / N# / I# / Q#`). You can directly reference:
- `[Action]{Talk to N1}`
- `[Action]{Investigate L2}`

### 4.3 OOC Rules/Protocol Questions

Use `<OOC>` to ask and have AI point to specific files as authoritative source (avoid drift).

---

## 5) Story Preference Optimization (Personalized DM)

Preference file: `PLAYER_PROFILE.md`

Usage:
- Fill during initialization (recommended)
- You can also OOC modify preferences anytime (e.g., "more horror/faster pace/less combat"), AI will patch `PLAYER_PROFILE.md`

Context compression strategy:
- Each turn only compress 1 line from preference summary (e.g., `STYLE=...`) into `HOT_PACK.md flags=`, rest not frequently read.

---

## 6) Stable Ground Truth (Don't Mix)

- Kernel protocol (how to run): `KERNEL_PROMPT.md`
- World entry (pointer/routing): `System.md`
- Event ground truth (history): `sessions/`
- Player-side state panel: `STATE_PANEL.md`
- Backend world state index: `lore/WORLD_STATE.md`
- Incremental save spec: `ARCHIVE_DELTA.md`
- Session end drift check: `CONTINUITY_CHECK.md`

---

## 7) Hidden DM Files (Enhance Experience: Suspense/Planning/Behind-Scenes)

These files belong to DM/AI behind-the-scenes tools, **must not be directly referenced or spoilered in player-visible output**:

- `.DM_SECRETS.md`: Unrevealed truth/behind-settings (migrated to `sessions/` and content packages upon triggering)
- `.DM_PLANNER.md`: Story planning and suspense engine (main plot/Fronts/clue inventory/revelations/next session beats)

They are stored with campaigns at: `campaigns/<id>/root/`, root directory keeps symbolic links for compatibility.
