# CARTRIDGE.md — Nebelmark 1444 (EN)

cartridge_id: nebelmark_1444
version: 1.0.0
language: en-US

## entrypoints
- lore/INDEX.md
- locations/LOCATION_INDEX.md
- maps/MAP_INDEX.md
- quests/QUEST_LOG.md
- characters/NPCs/npc_roster.md
- characters/PCs/README.md

## routes
# Command Header -> Priority Retrieval Scope (Only read index/summary/entry headers)
[LOOK]:
  - locations/LOCATION_INDEX.md
  - maps/MAP_INDEX.md
[ASK]:
  - characters/NPCs/npc_roster.md
  - lore/INDEX.md
[ACT]:
  - quests/QUEST_LOG.md
  - lore/INDEX.md
[FIGHT]:
  - engine/mechanics/COMBAT.md
  - engine/mechanics/STATE_PANEL_SPEC.md
[CAST]:
  - lore/INDEX.md
  - engine/mechanics/HOUSE_RULES.md
[MANAGE]:
  - quests/QUEST_LOG.md
  - lore/WORLD_STATE.md
[OOC]:
  - engine/mechanics/INDEX.md
  - engine/mechanics/GOVERNANCE_PANEL_SPEC.md

## aliases
# @handle: [alias list]
@nebelheim_gate: ["Mist City North Gate", "Nebelheim North Gate", "City North Gate"]
@nebelmark_region: ["Mist Border Region", "Nebelmark"]

## invariants
- The world is under "Mist" influence, with mist phenomena persisting long-term.
- Governance panel indicators will not drastically jump in a single turn.

## feature_flags
indicators: true
governance: true
fiction_sync: true
map_system: true
