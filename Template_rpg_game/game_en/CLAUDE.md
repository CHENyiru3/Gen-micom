# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is a **filesystem-based TTRPG game template** designed for LLM/DM automation. The template provides a complete structure that can be customized with any world setting, mechanics, and content.

## Project Structure

```
/
├── KERNEL_PROMPT.md        # Stable DM kernel protocol (how to run)
├── System.md               # World instance router + file entrypoints
├── README.md               # Main user guide
├── INIT_PROTOCOL.md        # Initialization protocol
├── CLI_SPEC.md             # Player input specification
├── HOT_START.md            # Resume/recovery procedure
├── ARCHIVE_DELTA.md        # Incremental save specification
├── HOT_PACK.md             # Next turn context package
├── STATE_PANEL.md          # Player-visible persistent panel
├── OBJECT_INDEX.md         # Active object index
├── PLAYER_PROFILE.md       # Player preferences
├── Char.md                 # Character system overview
├── Map-Gen.md              # Map generation notes
└── lore/
    ├── INDEX.md            # Lore RAG entrypoint
    ├── WORLD_STATE.md      # Global indicators + dynamic state
    ├── CANON/              # Daylight History (static world facts)
    ├── MIST/               # Mist History (supernatural elements)
    └── MECHANICS/          # Game mechanics indicators

/locations/                 # Location files
/characters/
    ├── PCs/                # Player character records
    ├── NPCs/               # NPC roster and individual files
/quests/                    # Quest logs and details
/sessions/                  # Session play records
/mechanics/                 # House rules and trackers
/skills_repo/               # Installable Codex skills
/maps/                      # Maps content pack
/scripts/                   # Automation scripts
/campaigns/                 # Campaign saves (per-campaign state)
```

## Game Sessions

**How to run sessions (kernel vs content)**:
- Kernel protocol: `KERNEL_PROMPT.md` (stable, never changes)
- World instance/router: `System.md`
- Hot start: `HOT_START.md` (reads `HOT_PACK.md` first)
- Live state: `index.md` + `STATE_PANEL.md` + latest `sessions/session_*.md`

**Starting a Game**:
- Use the input protocol in `CLI_SPEC.md`
- Follow the turn pipeline in `KERNEL_PROMPT.md`
- Initialize with `<Initialize>` command

**Current Game State**: See `index.md` for active quest log, NPC status, and indicators.

## Working with This Repository

This is a creative/narrative project with markdown documents for an LLM-based RPG game:
- No build commands, tests, or linting required
- Files are markdown documents for game content
- Key difference from code: **KERNEL_PROMPT.md is stable API** — do not embed world content in it

## Key Reference Files

| File | Purpose |
|------|---------|
| `KERNEL_PROMPT.md` | Stable DM kernel protocol |
| `System.md` | World instance/router + file entrypoints |
| `HOT_START.md` | Stable reboot procedure |
| `HOT_PACK.md` | Latest reboot context pack |
| `OBJECT_INDEX.md` | Hot cache for active objects |
| `ARCHIVE_DELTA.md` | Canonical delta-save spec |
| `CONTINUITY_CHECK.md` | End-of-session drift checklist |
| `lore/WORLD_STATE.md` | Global indicators and dynamic world state |
| `mechanics/HOUSE_RULES.md` | Dice rules, action syntax, constraints |
| `mechanics/STATE_PANEL_SPEC.md` | Stable state panel schema |
| `sessions/session_*.md` | Session play records |
| `Writing/Fiction_index.md` | Fiction/novel progress tracking |

## HOT/WARM/COLD Pattern

- **HOT**: Read every turn (`HOT_PACK.md`, `OBJECT_INDEX.md`, `STATE_PANEL.md` summary)
- **WARM**: Read when triggered (`mechanics/*.md`, `lore/CANON/*`, `characters/NPCs/*`)
- **COLD**: Rarely read (`Writing/`, `.DM_*` files)

## Customization

When customizing this template:
1. Read `Generate_game.md` for complete instructions
2. Edit `lore/CANON/` files for world setting
3. Edit `lore/MIST/` files for supernatural elements (if any)
4. Edit `mechanics/` files for game rules
5. Edit `characters/NPCs/`, `locations/`, `quests/` for content
