---
name: rpg-dm-content-pack-authoring
description: Create and maintain content packs (lore, NPCs, quests, locations, sessions, state) for a filesystem-backed RPG without modifying the kernel protocol.
---

# RPG DM Content Pack Authoring

Use this skill when you need to create or modify content files for the RPG system (lore, NPCs, quests, locations, sessions, state).

## Content Pack Types

| Type | Location | Purpose |
|------|----------|---------|
| Lore | `lore/` | World setting, history, factions |
| NPCs | `characters/NPCs/` | Non-player characters |
| Quests | `quests/` | Quest definitions and tracking |
| Locations | `locations/` | Location descriptions |
| Sessions | `sessions/` | Session records and decisions |
| State | `campaigns/<id>/root/` | Campaign-specific state |

## Content Creation Rules

### Lore Files
- Use the template in `lore/INDEX.md`
- Include tags for RAG retrieval
- Keep paragraphs short (≤100 words each)
- Include "Quick Reference Anchors" at top

### NPC Files
- Use the template in `characters/NPCs/npc_roster.md`
- Include public identity AND hidden agenda
- List secrets (2 easy, 1 hard to discover)
- Note relationships with other NPCs

### Quest Files
- Use the template in `quests/QUEST_LOG.md`
- Define clear objectives
- Include time limits if applicable
- Define consequences for success/failure

### Location Files
- Include description and atmosphere
- List points of interest
- Note hazards and challenges
- Include NPCs and treasure if present

### Session Files
- Use the template format from `sessions/session_0000_bootstrap.md`
- Document decisions with full context
- Note clues discovered
- Track indicator changes

## Naming Conventions

| Content Type | Pattern | Example |
|--------------|---------|---------|
| Lore files | `lore/[TYPE]/[NAME].md` | `lore/CANON/WORLD.md` |
| NPCs | `characters/NPCs/[npc_id].md` | `characters/NPCs/npc_marcus.md` |
| Quests | `quests/[quest_id].md` | `quests/quest_save_village.md` |
| Locations | `locations/[loc_id].md` | `locations/loc_tavern.md` |
| Sessions | `sessions/session_YYYY-MM-DD_slug.md` | `sessions/session_2026-01-30_adventure.md` |

## Content Linking

When creating content, link to related content:
- NPCs → Factions, Locations, Quests
- Quests → NPCs, Locations, Rewards
- Locations → NPCs, Quests, Items

Use short codes for linking:
- `N#` for NPCs
- `L#` for Locations
- `Q#` for Quests
- `I#` for Items
- `F#` for Factions

## Quality Checklist

- [ ] Content follows template format
- [ ] Tags are included for RAG
- [ ] Content is searchable (not too long)
- [ ] Related content is linked
- [ ] Secrets are clearly marked
- [ ] Game mechanics are separated from description
