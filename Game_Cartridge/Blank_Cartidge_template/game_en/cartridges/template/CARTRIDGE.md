# CARTRIDGE.md — Template Cartridge (EN)

cartridge_id: template
version: 0.2.0
language: en

## entrypoints
- lore/INDEX.md
- locations/LOCATION_INDEX.md
- maps/MAP_INDEX.md
- quests/QUEST_LOG.md
- characters/NPCs/npc_roster.md
- characters/PCs/README.md

## routes
[LOOK]:
  - locations/LOCATION_INDEX.md
  - maps/MAP_INDEX.md
[ASK]:
  - characters/NPCs/npc_roster.md
  - lore/INDEX.md
[ACT]:
  - quests/QUEST_LOG.md
  - lore/WORLD_STATE.md
[FIGHT]:
  - engine/mechanics/COMBAT.md
[CAST]:
  - lore/INDEX.md
[MANAGE]:
  - quests/QUEST_LOG.md
[OOC]:
  - engine/mechanics/INDEX.md

## aliases
@template_loc: ["template location"]
@template_npc: ["template npc"]

## invariants
- Template cartridge provides minimal indices only.
- New cartridges should lock version via cartridge_version_lock.

## feature_flags
indicators: true
governance: true
fiction_sync: true
map_system: true
