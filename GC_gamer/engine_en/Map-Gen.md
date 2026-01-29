---
tags: [map, guide, protocol]
related: [cartridges/<id>/maps/MAP_INDEX.md, engine/HOT_START.md, engine/KERNEL_PROMPT.md]
---

# MAPS_GUIDE.md — Command-Line Map Generation and Archive Specification (Macro/Micro + Logic Save)
Version: v1.0
Purpose: Guide DM/AI to generate ASCII maps (macro and micro) in "command-line output" style, and **persistently save maps with their generation logic**, ensuring subsequent continuation consistency and retrievability (RAG).

---

## 0) Goals and Principles
### 0.1 Goals
1) Output maps in **pure text/command-line style** (ASCII), directly pasteable to terminal or documents.
2) Synchronously save:
   - Map body (rendered image)
   - Map data (parseable structured information)
   - Map logic (why drawn this way: constraints, derivations, sources, assumptions, undetermined points)
3) Support:
   - **Macro maps**: Regions/routes/faction boundaries/risk layers
   - **Micro maps**: City blocks/buildings/dungeons/combat grids

### 0.2 Constraints
- Maps must be consistent with White Day History/Mist History settings, economy/diplomacy, urban fabric.
- Maps allow "unexplored/unknown", and must use Fog-of-War to represent.
- Each map update must be traceable (diff / changelog).

---

## 1) Map Directory and File Structure (Must Obey)
Recommended to add to your settings repository:

```
/cartridges/<id>/maps/
MAP_INDEX.md
macro/
macro_0001_nebelmark_region.md
macro_0001_nebelmark_region.data.yaml
macro_0001_nebelmark_region.logic.md
micro/
micro_0001_nebelheim_city.md
micro_0001_nebelheim_city.data.yaml
micro_0001_nebelheim_city.logic.md
instances/
inst_YYYY-MM-DD_slug.md          # Single session temporary/reveal version (Fog changes)
inst_YYYY-MM-DD_slug.logic.md
```

### 1.1 MAP_INDEX.md (Index Must Be Maintained)
Each new map must register:
- map_id
- name
- type (macro/micro)
- scale
- coverage area
- current version
- last update time
- associated session / quest / location / faction tags

---

## 2) Map Types and Scale Specifications
### 2.1 Macro Maps (Macro)
Used for: Regional geography, roads, rivers, checkpoints, faction influence, risk premiums, weather/mist windows.
Recommended two scales (choose one or maintain both):
- **Hex mode**: 1 hex = 6 miles (~10km) or 12 miles (~20km)
- **Node mode**: Cities/forts/markets/ferries as nodes, road network as edges (suitable for political economy and passage control)

Macro maps must include:
- Transportation nodes (cities, forts, monasteries, checkpoints, bridges, markets)
- Road network types (official roads/dirt roads/trade routes/secret paths)
- Passage risk (RP 0-3)
- Price impact (PI 1-5, can mark on nodes)
- Mist active areas (Mist Zone: low/medium/high)

### 2.2 Micro Maps (Micro)
Used for: City blocks, key buildings, indoor scenes, dungeons, combat terrain.
Recommended scales:
- **City/block map**: Not forced grid, use block/street topology + intersection nodes
- **Dungeon/combat map**: Grid (1 square = 5 feet) or room nodes (room graph)

Micro maps must include:
- Entry/exit/bottleneck points
- Interactable objects (doors, stairwells, wells, secret passages, sentry posts)
- Visibility and illumination (bright/dim/dark)
- Noise/smell/foot traffic (optional but strongly recommended: especially important for street maps)
- Fog-of-War (unknown areas cannot be shown in full detail)

---

## 3) ASCII Rendering Specifications (Command-Line Style)
### 3.1 General Symbol Table (Recommended)
- Terrain:
  - `~` Water / rivers
  - `^` Mountain / high ground
  - `"` Farmland / vineyards
  - `,` Grassland / wasteland
  - `#` City walls / thick structures
  - `=` Official roads / main roads
  - `-` Small paths
  - `:` Trails / swamp boardwalks
  - `*` Mist active points / anomalous points
- Buildings/Nodes:
  - `C` City
  - `T` Tower/Outpost
  - `B` Bridge
  - `G` City Gate
  - `M` Market/Fair
  - `K` Keep/Castle
  - `A` Abbey/Church
  - `D` Dungeon entrance/Cellar
- Fog-of-War:
  - `?` Unexplored
  - `·` Explored but details unknown (hazy)
- Annotations:
  - Coordinate axes: row/col numbers or A1, B2...
  - Key points use `[@1]`, `[@2]` tags (correspond to data.yaml)

> Allowed to extend symbols by map type, but must write `Legend` at map file top.

### 3.2 Output Template (Required)
Each map output must follow this order:
1) Title + metadata (front matter)
2) Legend (symbol explanation)
3) Rendered map (ASCII block)
4) POI list (Points of Interest: number→meaning→status)
5) Logic summary (this update reason/source/undetermined points)

---

## 4) Map Data Model (Must Save as .data.yaml)
Each map must have a structured data file for RAG and consistency checking.

### 4.1 Unified YAML Fields
```yaml
map_id: "macro_0001"
name: "Nebelmark Region Map"
type: "macro"                 # macro | micro
scale:
  mode: "hex"                 # hex | node | grid
  hex_miles: 6                # if hex
  grid_ft: null               # if grid
coverage:
  center: "Nebelheim"
  bbox: "W-E: 60mi, N-S: 48mi"
version: "1.0.3"
updated: "YYYY-MM-DD"
tags: ["region:nebelmark", "era:1444", "mist:crack_phase"]
layers:
  terrain: true
  routes: true
  factions: true
  risk: true
  mist: true
fog:
  policy: "reveal_on_discovery"
  unexplored_symbol: "?"
nodes:
  - id: "@1"
    name: "Nebelheim"
    kind: "city"
    coord: "H7"              # hex or grid coordinate
    attributes:
      PI: 3
      Rumor: 1
      Heat: 0
      MistZone: "medium"
edges:
  - from: "@1"
    to: "@2"
    kind: "road"             # road | river | trail | secret
    travel_time: "6h"
    risk_RP: 2
pois:
  - id: "@7"
    name: "Linden Execution Ground"
    status: "known"          # known | rumored | hidden | destroyed
    hooks: ["vehm_mark", "ssgg_dagger"]
constraints:
  - "Nebelheim must be located near Rhine tributary"
  - "French winter camp 1-2 days march from city"
provenance:
  sources:
    - "session_1444_01_opening"
  assumptions:
    - "River surface partially frozen in winter"
  uncertainties:
    - "Black pine forest boundary not yet surveyed"
```

---

## 5) "Map Logic" File (Must Save as .logic.md)

Each map must have a logic explanation file, answering three types of questions:

1. **Why drawn this way** (historical/economic/military/terrain constraints)
2. **What's certain**, what's rumored/speculated
3. **How this map updates with plot**

### 5.1 Logic File Template

```md
# Logic — <map_id> <name>

## 1) Design Constraints (Hard Constraints)
- ...

## 2) Derivation Chain (Key Causality)
- Because A (French winter camp needs supply line) → Must have B (roads and village nodes) → Therefore placed at ...

## 3) Uncertainty and Fog Strategy
- Unexplored area: Keep ?; only reveal after player gains "surveying/rumor/sighting"
- Rumor annotations: Use status=rumored, don't draw details, just mark a point

## 4) Update Rules (Diff Principle)
- Only incrementally modify: Add POIs, reveal Fog, adjust RP/PI
- Don't redraw confirmed terrain (unless catastrophic event)

## 5) System Indicator Linkage
- Rumor≥2: New "patrol/ informants points" in city
- Debt increase: Mist active points * quantity increase or movement
```

---

## 6) Command-Line "Map Generation Command" Specifications (AI Operation Interface)

> This is not a shell you actually execute, but the "CLI-style protocol" you output to user/logs.
> Each time player or DM issues command, you output: `COMMAND` → `RESULT` → `ARCHIVE_DELTA`.

### 6.1 Command Set (Recommended Minimum)

* `map new <type> <name> --scale hex|node|grid --id <...>`
* `map render <map_id> --layer terrain,routes,fog,...`
* `map reveal <map_id> <coord|poi_id> --reason "<session clue>"`
* `map add-poi <map_id> "<poi name>" --coord <...> --status known|rumored|hidden`
* `map link <map_id> <from> <to> --kind road|trail|secret --risk <0-3> --time "<...>"`
* `map annotate <map_id> <poi_id> --note "<text>" --tags "..."`
* `map update-risk <map_id> <edge_or_region> --RP <0-3> --PI <1-5>`
* `map diff <map_id> --from <v> --to <v>` (output change summary)
* `map export <map_id> --format ascii|yaml|both`

### 6.2 Output Format (Strict)

Command echo:

```txt
$ map reveal micro_0001 A12 --reason "Player bought sewer route from executioner"
OK: Revealed cells: A12..A14
OK: Updated fog status: unexplored -> explored
```

Then give map render (or partial render), finally give ARCHIVE_DELTA (see section 7).

---

## 7) Save and Update: Must Write to Archive (ARCHIVE_DELTA)

Each time map changes (new/reveal/add-poi/link/update-risk), must append at reply end:

```md
<!-- ARCHIVE_DELTA
files:
  - path: cartridges/<id>/maps/MAP_INDEX.md
    patch: |
      - added: micro_0002_sewer.md (v1.0.0)
  - path: cartridges/<id>/maps/micro/micro_0002_sewer.md
    append: |
      ## v1.0.0 Render
      ...
  - path: cartridges/<id>/maps/micro/micro_0002_sewer.data.yaml
    patch: |
      - pois: ...
  - path: cartridges/<id>/maps/micro/micro_0002_sewer.logic.md
    append: |
      ## Update Reason
      ...
-->
```

**Mandatory Requirements**:

* `.md` (render), `.data.yaml` (structure), `.logic.md` (logic) triad is essential.
* Each update must bump `version`, and record "update reason and source" in `.logic.md` (session clue / NPC testimony / measured path).

---

## 8) Consistency and Validation Rules (Prevent "Drawing Forgetting")

Each time before updating map, AI must perform self-check (internally complete, present as summary):

1. **Topology consistency**: Are road connections broken? Are nodes isolated?
2. **Scale consistency**: Do travel time and distance match?
3. **Indicator consistency**: Do RP/PI/Heat/Rumor conflict with current plot status?
4. **Fog consistency**: Unexplored areas can't have detailed POIs; rumored POIs don't give precise structure.
5. **Cross-map consistency**: Macro node `Nebelheim` corresponds to micro city map entry/city gate coordinates.

If conflict found, must:

* Add `uncertainties` in `.logic.md` or correct derivation;
* Or generate "temporary instance map" (`/campaigns/<id>/maps/runtime/`) for this session, merge into main map after confirmation.

---

## 9) Generation Workflow (Recommended)

### 9.1 Macro Map Workflow (Region)

1. `map new macro "Nebelmark Region Map" --scale hex --id macro_0001`
2. Draw terrain skeleton (river, mountain, forest, main roads)
3. Place triangular game nodes (French/Imperial/Burgundy key touchpoints)
4. Mark RP/PI initial values and mist active areas
5. Fog: Only reveal player-known range, others `?`

### 9.2 Micro Map Workflow (City)

1. `map new micro "Nebelheim City Map" --scale node --id micro_0001`
2. Draw triple city defenses + refugee belt + guild street + Jewish quarter + church district + executioner bridge
3. Place key POIs (Town Hall, Wine Cellar, City Gate, Market, Monastery, Sewer Exit)
4. Bind each POI: faction, risk, available resources, typical encounters
5. Only reveal specific alleys/interior structures after player exploration

### 9.3 Dungeon/Combat Grid Workflow (Dungeon/Grid)

1. `map new micro "Sewer Section" --scale grid --id micro_0002`
2. Initially only draw entrance and first room, others `?`
3. Each time player advances: `map reveal` + update anomaly points `*`
4. Rooms must have: entry/exit/cover/light/interactable objects

---

## 10) Minimum Example (Micro: Block Topology Map)

```txt
MAP: Nebelheim (micro_0001)  TYPE: micro(node)  VER: 1.0.0
Legend: #City Wall  =Main St  -Alley  GGate  MMarket  AChurch  RTown Hall  JJewish Quarter  XExecutioner Bridge  ?Unexplored  *Anomaly

            ###########G###########
            #         =           #
            #   [A]===M===R       #
            #     -  ==  -        #
            #   J-?-==?- -        #
            #     -  ==  -    X   #
            #   [Shantytown & Moat]  -  #
            ###########G###########

POI:
[@1] A Main Cathedral District (known)
[@2] M Market (known)
[@3] R Town Hall & Wine Cellar (known)
[@4] J Jewish Quarter (rumored: locked at night;密集账房)
[@5] X Executioner Bridge (known: reputation cost high)
[*1] Anomaly Point (hidden: low probability in crack phase)
```

---

## 11) RAG Tag Suggestions (For Retrieval)

In each map front matter `tags`, include at least:

* `region:<...>` / `city:<...>` / `dungeon:<...>`
* `era:1444` / `mist:crack_phase` / `mist:threshold_crossing`
* `faction:france|empire|burgundy|church|guild|vehm|outcasts`
* `economy:PI3` `risk:RP2` (optional)

— End of MAPS_GUIDE.md —

> Note: This repo has created `cartridges/<id>/maps/` directory and `cartridges/<id>/maps/MAP_INDEX.md`, subsequent map updates are incrementally written via `ARCHIVE_DELTA` per section 7 of this file.
