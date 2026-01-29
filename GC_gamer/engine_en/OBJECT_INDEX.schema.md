# OBJECT_INDEX.schema.md — Object Index Minimum Field Specification

## General Fields
- id: Internal unique ID (optional)
- handle: @handle (required)
- name: Human-readable name (required)
- type: NPC | LOC | QUEST | ITEM | FACTION
- status: active | inactive | resolved | hidden
- tags: [keyword]
- summary: One-sentence summary

## NPC
- role: Character positioning
- affiliation: Faction/organization
- location: Regular location

## LOC
- region: Large area
- accessibility: Accessibility/restrictions
- hazards: Risks

## QUEST
- giver: Quest giver
- stage: Current stage
- stakes: Failure consequences

## ITEM
- rarity: Rarity
- effect: Core effect

## Handle Specifications
- All lowercase, use underscores
- Examples: @marcus, @nebelheim_gate, @q_002_quarry
