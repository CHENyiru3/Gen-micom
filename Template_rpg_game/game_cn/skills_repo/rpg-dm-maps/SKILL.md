---
name: rpg-dm-maps
description: Create and maintain map content packs including render (description), data (YAML), and logic files, with fog-of-war and versioning support.
---

# RPG DM Map Management

Use this skill when you need to create or maintain map content for the RPG system.

## Map Structure (Triad)

Each map consists of three files:

| File | Purpose | Format |
|------|---------|--------|
| `[map_id].md` | Render/description | Markdown |
| `[map_id].data.yaml` | Data/database | YAML |
| `[map_id].logic.md` | Rules/logic | Markdown |

## Map Types

### Macro Maps (Regional)
- **Scale**: Hex-based
- **Purpose**: Regional exploration, travel
- **Location**: `maps/macro/`
- **Example**: `maps/macro/macro_0001_region.md`

### Micro Maps (Local)
- **Scale**: Node-based
- **Purpose**: Local exploration, dungeons
- **Location**: `maps/micro/`
- **Example**: `maps/micro/micro_0001_dungeon.md`

## Map Creation Process

### Step 1: Create Render File
Write descriptive markdown file:
- Overview and atmosphere
- Points of interest
- Hazards and challenges
- NPCs and treasure

### Step 2: Create Data File
Write YAML data file:
- Meta information (ID, name, type, scale)
- Node/hex data
- Connections
- NPCs, hazards, treasure
- Encounter tables

### Step 3: Create Logic File
Write rules markdown file:
- Movement rules
- Encounter logic
- Exploration rules
- Special interactions

### Step 4: Update Index
Add entry to `maps/MAP_INDEX.md`:
- map_id
- name
- type
- scale
- version
- status
- file paths

## Fog of War

### Tracking
- Track explored areas in `OBJECT_INDEX.md`
- Store exploration state in map data file
- Use `OBJECT_INDEX.md` for current exploration state

### Reveal Rules
- Fully explored: Full visibility
- Adjacent to explored: Partial visibility
- Beyond: Hidden

## Versioning

Update version when:
- Adding new nodes/hexes: patch version (+0.0.1)
- Changing existing content: minor version (+0.1.0)
- Changing structure: major version (+1.0.0)

Record changes in logic file changelog.

## Quality Checklist

- [ ] All three files exist and are linked
- [ ] Render file is descriptive and atmospheric
- [ ] Data file is valid YAML
- [ ] Logic file contains all relevant rules
- [ ] Map index is updated
- [ ] Version is bumped and recorded
