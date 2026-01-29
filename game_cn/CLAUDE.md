# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is a **D&D 5e tabletop RPG project** called **《迷雾边境编年史：瞬变》** (Chronicles of the Misty Border: The Transient). The repository contains markdown documents for an LLM-based RPG game.

## Project Structure

```
/                     # Root game files
├── Background*.md    # Game lore and worldbuilding
├── Char.md           # Character content
├── Map-Gen.md        # Map generation notes
├── index.md          # Game state index (updated after sessions)
├── CLAUDE.md         # This file
├── KERNEL_PROMPT.md  # ← Stable DM kernel protocol (no plot/state)
├── System.md         # World instance + kernel router (no live snapshot)
└── lore/
    ├── WORLD_STATE.md      # Global indicators + dynamic state
    ├── INDEX.md            # Lore RAG entrypoint
    ├── CANON/              # Day history (static)
    └── MIST/               # Mist history (discoverable)

/locations/           # Location files
/characters/
    ├── PCs/           # Player character records
    ├── NPCs/          # NPC roster and individual files
/quests/              # Quest logs and details
/sessions/            # Session records
/mechanics/           # House rules and trackers
/skills_repo/         # Installable Codex skills (kernel/content authoring)
/maps/                # Maps content pack (render/data/logic triad)
```

## User Guide

See `README.md` for:
- Initialization (`<初始化>`)
- Hot cache (`HOT_PACK.md` / `OBJECT_INDEX.md`)
- Hot start / recovery (`HOT_START.md`)
- Efficient interaction (`CLI_SPEC.md`)
- Story preference tuning (`PLAYER_PROFILE.md`)
- Campaign separation (`campaigns/` + `CURRENT_CAMPAIGN.md`)
- Campaign automation (`scripts/campaign_manager.py`)

## Game Sessions

**How to run sessions (kernel vs content)**:
- Kernel protocol: `KERNEL_PROMPT.md`
- World instance/router: `System.md`
- Hot start: `HOT_START.md` (reads `HOT_PACK.md` first)
- Live state: `index.md` + `STATE_PANEL.md` + latest `sessions/session_*.md`

**Starting a Game**:
- Use the input protocol in `CLI_SPEC.md` and the turn pipeline in `KERNEL_PROMPT.md`.

**Current Game State**: See [index.md](index.md) for active quest log, NPC status, and indicators.

## Working with This Repository

This is a creative/narrative project:
- No build commands, tests, or linting required
- No code execution or development environment setup
- Files are markdown documents for an LLM-based RPG game

## Key Reference Files

| File | Purpose |
|------|---------|
| `index.md` | Quick reference for current game state |
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
