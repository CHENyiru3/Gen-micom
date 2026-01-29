# Content Pack Templates (Portable)

Keep kernel protocols stable. Put "world truth" in content files.

## NPC file template (minimal)

```md
## npc_XXX:
- **Name**:
- **Faction**:
- **Public Identity**:
- **Public Goal**:
- **Hidden Agenda**:
- **Easily Discovered Secrets**:
  1.
  2.
- **Hard to Discover Secret**:
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

## 2. Gameplay Connections
- Related Locations: loc_...
- Related Quests: quest_...
- Related NPCs: npc_...
```

