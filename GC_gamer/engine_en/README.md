# engine_en

English localization of the GC Gamer RPG engine. This directory mirrors [engine_cn](../engine_cn/) and provides all documentation and protocols in English for English-speaking players.

## Directory Structure

```
engine_en/
├── ARCHIVE_DELTA.md          # Incremental archive specification
├── CAMPAIGN_PROTOCOL.md      # Create/switch campaign workflow
├── CLI_SPEC.md               # Player command line input specification
├── CONTINUITY_CHECK.md       # Session end consistency check
├── HOT_START.md              # Hot start/restart protocol
├── INIT_PROTOCOL.md          # Initialization protocol
├── KERNEL_PROMPT.md          # Single agent DM kernel (core)
├── Map-Gen.md                # Map generation and archive spec
├── OBJECT_INDEX.schema.md    # Object index field specification
├── RAG_ENGINE.md             # Routing retrieval and fragment facts
├── System.md                 # World instance router
├── mechanics/                # Game mechanics and rules
│   ├── COMBAT.md             # Combat rules
│   ├── CONTEXT_PACK.md       # Context pack specification
│   ├── CONTEXT_PACK_EXAMPLES.md
│   ├── GOVERNANCE.md         # Governance panel
│   ├── GOVERNANCE_PANEL_SPEC.md
│   ├── HOUSE_RULES.md        # House rules
│   ├── INDEX.md              # Mechanics file index
│   ├── NPC_GUIDELINES.md     # NPC consistency constraints
│   ├── RAG_RULES.md          # RAG retrieval rules
│   ├── RANDOM_TABLES.md      # Random encounter tables
│   ├── SOCIAL_INVESTIGATION.md
│   ├── skills_repo/rpg-dm-function-calling-local/references/panels.json   # State panel field spec
│   ├── SURVIVAL.md           # Survival rules
│   └── TRACKERS.md           # Tracker templates
├── scripts/                  # Utility scripts
│   └── campaign_manager.py   # Campaign management tool
└── skills_repo/              # Codex-compatible skills
    ├── README.md
    ├── rpg-dm-campaign-manager/
    ├── rpg-dm-content-pack-authoring/
    ├── rpg-dm-fiction-sync/
    ├── rpg-dm-governance-panel/
    ├── rpg-dm-kernel-protocol/
    └── rpg-dm-maps/
```

## Relationship to engine_cn

- **cn is the source of truth**: All content originates in `engine_cn/`
- **en is the mirror**: `engine_en/` mirrors the same structure with English translations
- When updating: Modify `engine_cn/` first, then synchronize to `engine_en/`

## Core Protocols

| Protocol | Purpose |
|----------|---------|
| `KERNEL_PROMPT.md` | Core turn execution kernel |
| `HOT_START.md` | Fast context recovery |
| `ARCHIVE_DELTA.md` | Incremental state persistence |
| `CLI_SPEC.md` | Player input format |
| `RAG_RULES.md` | Knowledge retrieval rules |

## Getting Started

1. Read `KERNEL_PROMPT.md` to understand the core kernel
2. Review `CLI_SPEC.md` for player input format
3. Study `HOT_START.md` for context recovery
4. Reference `mechanics/INDEX.md` for rules lookup
