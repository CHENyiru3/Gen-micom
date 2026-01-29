# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is a **D&D 5e tabletop RPG project** called **《迷雾边境编年史：瞬变》** (Chronicles of the Misty Border: The Transient). The repository contains markdown documents for an LLM-based RPG game.

## Project Structure

```
/                     # Root game files
├── ACTIVE.md         # Active campaign pointer
├── CLAUDE.md         # This file
├── engine/           # Shared engine (symlink to GC_gamer/engine)
├── cartridges/       # World content (cards)
│   ├── nebelmark_1444/
│   └── template_card/
└── campaigns/         # Per-campaign runtime storage
    ├── _template/
    └── campaign_0001/
```

## User Guide

See `README.md` for:
- Initialization (`<初始化>`)
- Hot cache (`campaigns/<id>/HOT_PACK.md` / `campaigns/<id>/OBJECT_INDEX.md`)
- Hot start / recovery (`engine/HOT_START.md`)
- Efficient interaction (`engine/CLI_SPEC.md`)
- Story preference tuning (`campaigns/<id>/PLAYER_PROFILE.md`)
- Campaign separation (`campaigns/` + `ACTIVE.md`)
- Campaign automation (`engine/scripts/campaign_manager.py`)

## Game Sessions

**How to run sessions (kernel vs content)**:
- Kernel protocol: `engine/KERNEL_PROMPT.md`
- World instance/router: `engine/System.md`
- Hot start: `engine/HOT_START.md` (reads `campaigns/<id>/HOT_PACK.md` first)
- Live state: `campaigns/<id>/index.md` + `campaigns/<id>/STATE_PANEL.md` + latest `campaigns/<id>/sessions/session_*.md`

**Starting a Game**:
- Use the input protocol in `engine/CLI_SPEC.md` and the turn pipeline in `engine/KERNEL_PROMPT.md`.

**Current Game State**: See `campaigns/<id>/index.md` for active quest log, NPC status, and indicators.

## Working with This Repository

This is a creative/narrative project:
- No build commands, tests, or linting required
- No code execution or development environment setup
- Files are markdown documents for an LLM-based RPG game

## Key Reference Files

| File | Purpose |
|------|---------|
| `campaigns/<id>/index.md` | Quick reference for current game state |
| `engine/KERNEL_PROMPT.md` | Stable DM kernel protocol |
| `engine/System.md` | World instance/router + file entrypoints |
| `engine/HOT_START.md` | Stable reboot procedure |
| `campaigns/<id>/HOT_PACK.md` | Latest reboot context pack |
| `campaigns/<id>/OBJECT_INDEX.md` | Hot cache for active objects |
| `engine/ARCHIVE_DELTA.md` | Canonical delta-save spec |
| `engine/CONTINUITY_CHECK.md` | End-of-session drift checklist |
| `campaigns/<id>/WORLD_STATE.md` | Global indicators and dynamic world state |
| `engine/mechanics/HOUSE_RULES.md` | Dice rules, action syntax, constraints |
| `engine/mechanics/STATE_PANEL_SPEC.md` | Stable state panel schema |
| `campaigns/<id>/sessions/session_*.md` | Session play records |
| `campaigns/<id>/Writing/Fiction_index.md` | Fiction/novel progress tracking |
