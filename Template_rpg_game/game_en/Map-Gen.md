# Map-Gen.md — Map Generation and Save Spec

> **Purpose**: Map generation notes and extended specification for the map system

---

## 0) Map System Overview

This template uses a **triad system** for maps:
- **Render** (`.md`): Descriptive text and atmosphere
- **Data** (`.data.yaml`): Structured data and connections
- **Logic** (`.logic.md`): Rules for movement, encounters, etc.

---

## 1) Map Types

### 1.1 Macro Maps (Regional)
- **Location**: `maps/macro/`
- **Scale**: Hex-based (typically 6 miles/hex)
- **Purpose**: Regional exploration, travel, wilderness

### 1.2 Micro Maps (Local)
- **Location**: `maps/micro/`
- **Scale**: Node-based (rooms, areas)
- **Purpose**: Local exploration, dungeons, buildings

---

## 2) Map Naming Convention

### 2.1 Macro Maps
```
macro_[NUMBER]_[REGION_NAME].md/data.yaml/logic.md
```

Examples:
- `macro_0001_nebelmark_region.md`
- `macro_0002_silver_highlands.md`

### 2.2 Micro Maps
```
micro_[NUMBER]_[LOCATION_NAME].md/data.yaml/logic.md
```

Examples:
- `micro_0001_nebelheim_city.md`
- `micro_0002_ancient_ruins.md`

---

## 3) Map Index

All maps must be registered in `maps/MAP_INDEX.md`:

```markdown
| map_id | name | type | scale | version | status | files |
|--------|------|------|-------|---------|--------|-------|
| macro_0001 | Region Name | macro | hex | 0.1.0 | active | `maps/macro/...` |
```

---

## 4) Fog of War

### 4.1 Tracking State
- Store in `OBJECT_INDEX.md` (runtime)
- Store in map `.data.yaml` (persistent)

### 4.2 Visibility Rules
- Explored: Full visibility
- Adjacent to explored: Partial visibility
- Beyond: Hidden

---

## 5) Version Control

### 5.1 Version Format
`MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes to structure
- **MINOR**: Content additions or changes
- **PATCH**: Typo fixes, clarifications

### 5.2 Version Changelog
Record in each map's `.logic.md`:

```markdown
## Version History

| Version | Date | Change |
|---------|------|--------|
| 0.1.0 | 2026-01-29 | Initial version |
```

---

## 6) Map Creation Workflow

### Step 1: Plan
- Sketch the map (hand-drawn or tool)
- Define key locations
- Plan connections

### Step 2: Create Files
```bash
cp maps/macro/macro_0001_template.md maps/macro/macro_0001_[name].md
cp maps/macro/macro_0001_template.data.yaml maps/macro/macro_0001_[name].data.yaml
cp maps/macro/macro_0001_template.logic.md maps/macro/macro_0001_[name].logic.md
```

### Step 3: Fill Content
- Write render file
- Update data file
- Customize logic file

### Step 4: Register
- Add entry to `maps/MAP_INDEX.md`

### Step 5: Test
- Verify all files exist
- Check YAML syntax
- Test movement logic

---

## 7) YAML Data Format

### 7.1 Macro Map Data
```yaml
version: 0.1.0
meta:
  map_id: macro_0001
  name: Region Name
  type: macro
  scale: hex
  hex_size: 6 miles

regions:
  - hex: "0000"
    name: Region Name
    terrain: forest
    features: []
    resources: []
```

### 7.2 Micro Map Data
```yaml
version: 0.1.0
meta:
  map_id: micro_0001
  name: Location Name
  type: micro
  scale: node

nodes:
  - id: "node_a"
    name: Room Name
    connections: ["node_b"]
    features: []
```

---

## 8) Integration with Game

### 8.1 Loading Maps
1. Read `maps/MAP_INDEX.md`
2. Load requested map's `.data.yaml`
3. Load requested map's `.md` for description
4. Load requested map's `.logic.md` for rules

### 8.2 Map References
- NPCs reference locations by ID
- Quests reference locations by ID
- Sessions reference locations by ID

---

*Customize this file with your game's specific map generation rules.*
