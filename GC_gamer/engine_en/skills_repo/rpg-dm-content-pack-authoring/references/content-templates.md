# Content Pack Templates (Portable)

Keep kernel protocols stable. Put "world truth" in content files.

## NPC file template (minimal)

```md
## npc_XXX:
- **Name**:
- **Faction**:
- **Public Identity**:
- **Public Goal**:
- **Hidden Goal**:
- **Easily Discovered Secrets**:
  1.
  2.
- **Hard to Discover Secrets**:
  1.
- **Key Relationships**:
- **Mist Status**: none|touched|agent|entity
- **First Appearance**: session_YYYY-MM-DD*.md
```

## Lore file template (RAG-friendly)

```md
---
tags: [canon|mist|mechanic, ...]
related: [...]
---

# Title

## 0. Quick Reference Anchor
- ...

## 1. Core Setting

## 2. Game Connection
- Related Locations: loc_...
- Related Quests: quest_...
- Related NPCs: npc_...
```

## JSON Panels (Runtime)

Use JSON for runtime panels (not MD):
- STATE_PANEL.json
- HOT_PACK.json
- MAINLINE_PANEL.json
- OBJECT_INDEX.json
- clues/CLUE_LOG.json

Schema: skills_repo/rpg-dm-function-calling-local/references/panels.json
