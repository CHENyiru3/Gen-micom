# README.md — RPG Game Template

This is a **filesystem-based TTRPG template** for LLM/DM automation. This template provides a complete structure that can be customized with your own world setting, mechanics, and content.

---

## Quick Start (Using This Template)

1. **Copy this template** to create your game
2. **Read Generate_game.md** for instructions on how to customize this template
3. **Fill in the placeholder settings** with your own world, characters, and rules
4. **Start playing** by running `<Initialize>` in your LLM session

---

## 0) Template Structure Overview

```
game_en/                    # English version template
├── KERNEL_PROMPT.md        # Stable DM kernel protocol (how to run)
├── System.md               # World instance router
├── README.md               # This file
├── INIT_PROTOCOL.md        # Campaign initialization
├── CLI_SPEC.md             # Player input protocol
├── HOT_START.md            # Resume/continue procedure
├── ARCHIVE_DELTA.md        # Incremental save spec
├── CONTINUITY_CHECK.md     # Session end drift verification
├── CAMPAIGN_PROTOCOL.md    # Campaign management
├── HOT_PACK.md             # Next turn context package
├── STATE_PANEL.md          # Player-visible state panel
├── OBJECT_INDEX.md         # Active object index
├── PLAYER_PROFILE.md       # Player preferences
├── Char.md                 # Character system
├── Map-Gen.md              # Map generation notes
├── lore/                   # World setting library
│   ├── INDEX.md            # Lore entrypoint
│   ├── CANON/              # Static world facts (customize this!)
│   ├── MIST/               # Supernatural elements (customize this!)
│   └── MECHANICS/          # Game mechanics indicators
├── mechanics/              # Game rules and systems
├── maps/                   # Map content (render/data/logic)
├── skills_repo/            # Installable Codex skills
├── campaigns/              # Campaign saves
│   └── _template/          # Template for new campaigns
├── sessions/               # Session records
├── characters/             # Character files
├── quests/                 # Quest logs
├── locations/              # Location files
└── scripts/                # Automation scripts
```

---

## 1) File Categories

### Core Kernel Files (Stable)
These files define **how the game runs** and should NOT be modified:
- `KERNEL_PROMPT.md` — Turn pipeline, HUD, RAG, ARCHIVE_DELTA
- `System.md` — World instance router
- `CLI_SPEC.md` — Player input protocol
- `HOT_START.md` — Resume procedure
- `INIT_PROTOCOL.md` — Initialization flow
- `ARCHIVE_DELTA.md` — Save format
- `CONTINUITY_CHECK.md` — Drift verification

### Game State Files (Runtime)
These are **auto-generated during play**:
- `HOT_PACK.md` — Next turn context (auto-patched)
- `STATE_PANEL.md` — Persistent state (auto-patched)
- `OBJECT_INDEX.md` — Active objects (auto-patched)
- `PLAYER_PROFILE.md` — Player preferences

### Content Files (Customize!)
These are where you **define your world**:
- `lore/CANON/*` — World history, geography, factions
- `lore/MIST/*` — Supernatural rules and phenomena
- `mechanics/*` — Combat, survival, social rules
- `maps/*` — Map data and logic
- `characters/NPCs/*` — NPC definitions
- `locations/*` — Location descriptions
- `quests/*` — Quest content

---

## 2) HOT (Hot Cache) Concept

The template uses a **HOT/WARM/COLD** file access pattern:

### HOT (Read Every Turn)
- `HOT_PACK.md` — Contains only `CONTEXT_PACK_NEXT` (≤25 lines)
- `PLAYER_PROFILE.md` — Preference summary (≤8 lines)
- `OBJECT_INDEX.md` — Active pointers with 1-line summaries
- `STATE_PANEL.md` — Only changed sections

### WARM (Read When Triggered)
- `mechanics/*.md` — When combat/survival/social triggers
- `lore/CANON/*` — When world facts needed
- `lore/MIST/*` — When supernatural rules needed
- `characters/NPCs/*` — When NPCs appear
- `maps/*` — When maps needed

### COLD (Rarely Read)
- `Writing/Fiction_par*.md` — Derived narrative
- `.DM_SECRETS.md` / `.DM_PLANNER.md` — DM behind-the-scenes

---

## 3) How to Customize

### Step 1: Define Your World
Edit files in `lore/CANON/`:
- `WORLD.md` — Geography, era, major locations
- `FACTIONS.md` — Organizations, factions, powers
- `TIMELINE.md` — Historical events

### Step 2: Add Supernatural Elements (Optional)
Edit files in `lore/MIST/`:
- `PHENOMENA.md` — Magical/uncanny phenomena
- `CREATURES.md` — Monsters and entities

### Step 3: Customize Mechanics
Edit files in `mechanics/`:
- `HOUSE_RULES.md` — Dice rules, DCs, modifiers
- `COMBAT.md` — Combat system
- `SURVIVAL.md` — Survival mechanics
- `SOCIAL_INVESTIGATION.md` — Social rules

### Step 4: Create Starting Content
- Add NPCs to `characters/NPCs/`
- Add locations to `locations/`
- Add quests to `quests/`
- Create maps in `maps/`

---

## 4) Starting a Game

1. Send `<Initialize>` to start campaign setup
2. Configure player preferences (written to `PLAYER_PROFILE.md`)
3. Create player character (written to `characters/PCs/pc_current.md`)
4. Choose opening hook
5. Begin playing!

---

## 5) Hot Start (Resume)

When context is lost or resuming:
1. Send `<Hot Start>` or `<Continue>`
2. AI reads `HOT_PACK.md` first
3. Recovers context from recent state
4. Continues from where left off

---

## 6) Campaign Management

- `<New campaign campaign_0002>` — Create and switch to new campaign
- `<Switch campaign campaigns/campaign_0001>` — Switch to existing campaign

Campaigns are stored in `campaigns/<campaign_id>/` and are isolated from each other.

---

*Template Version: 1.0.0*
