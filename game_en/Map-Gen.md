---
tags: [map, guide, protocol]
related: [maps/MAP_INDEX.md, HOT_START.md, KERNEL_PROMPT.md]
---

# MAPS_GUIDE.md — Command-Line Map Generation and Save Spec (Macro/Micro + Logic Save)
Version: v1.0
Purpose: Guide DM/AI to generate ASCII maps (macro and micro) in "command-line output" style, and **persistently save maps and their generation logic**, ensuring subsequent continuation consistency and retrievability (RAG).

---

## 0) Goals and Principles
### 0.1 Goals
1) Output maps (ASCII) in **pure text/command-line style**, can be pasted directly into terminal or documents.
2) Sync save:
   - Map body (rendering)
   - Map data (parseable structured information)
   - Map logic (why drawn this way: constraints, derivations, sources, assumptions, undetermined points)
3) Support:
   - **Macro maps**: Regions/routes/faction boundaries/risk layers
   - **Micro maps**: City blocks/buildings/dungeons/combat grids

### 0.2 Constraints
- Maps must be consistent with Daylight History/Mist History settings, economy/diplomacy, city fabric.
- Maps allow "unexplored/unknown", must be represented with Fog-of-War.
- Each map update must be traceable (diff / changelog).

---

## 1) Map Directory and File Structure (Must Follow)
Recommend adding to your setting repository:

```
/maps/
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
inst_YYYY-MM-DD_slug.md          # Single session temporary/reveal version (Fog change)
inst_YYYY-MM-DD_slug.logic.md
```

### 1.1 MAP_INDEX.md (Index Must Be Maintained)
Each new map must register:
- map_id
- Name
- Type (macro/micro)
- Scale
- Coverage
- Current version
- Last update time
- Associated session / quest / location / faction tags

---

## 2) Map Type and Scale Specs
### 2.1 Macro Maps (macro)
Used for: Regional geography, roads, rivers, checkpoints, faction influence, risk premium, weather/Mist window.
Recommend two scales (choose one or maintain both):
- **Hex mode**: 1 hex = 6 miles (~10km) or 12 miles (~20km)
- **Node mode**: Cities/fortresses/markets/ferry crossings as nodes, road network as edges (suitable for political economy and passage control)

Macro maps must include:
- Transportation nodes (city, fort, monastery, checkpoint, bridge, fair)
- Road network types (official road/dirt road/trade route/secret path)
- Passage risk (RP 0-3)
- Price influence (PI 1-5, can annotate at nodes)
- Mist active zones (Mist Zone: low/medium/high)

### 2.2 Micro Maps (micro)
Used for: City blocks, key buildings, indoor scenes, dungeons, combat terrain.
Recommended scales:
- **City/block map**: Not mandatory grid, use block/street topology + intersection nodes
- **Dungeon/combat map**: Grid (1 square = 5 ft) or room nodes (room graph)

Micro maps must include:
- Entrances/exits/bottleneck points
- Interactive objects (doors, stairs, wells, secret passages, sentry posts)
- Visibility and lighting (bright/dim/dark)
- Noise/smell/foot traffic (optional but strongly recommended: especially important for street maps)
- Fog-of-War (unknown areas cannot be shown凭空)

---

## 3) ASCII Rendering Specs (Command-Line Style)
### 3.1 Common Symbol Table (Recommended)
- Terrain:
  - `~` Water / River
  - `^` Mountain / High slope
  - `"` Farmland / Vineyard
  - `,` Grassland / Wasteland
  - `#` City wall / Thick structure
  - `=` Official road / Main road
  - `-` Small path
  - `:` Trail / Wetland boardwalk
  - `*` Mist active point / Anomaly point
- Building/Node:
  - `C` City
  - `T` Tower/Sentry
  - `B` Bridge
  - `G` City Gate
  - `M` Market/Fair
  - `K` Fortress/Castle
  - `A` Abbey/Church
  - `D` Dungeon access/Cellar
- Fog-of-War:
  - `?` Unexplored
  - `·` Explored but details unknown (hazy)
- Annotations:
  - Coordinate axis: Row/col numbers or A1, B2...
  - Key points use `[@1]`, `[@2]` tags (corresponding to data.yaml)

> Allowed to extend symbols by map type, but must write `Legend` at map file top.

### 3.2 Output Template (Must)
Each map output must follow this order:
1) Title + metadata (front matter)
2) Legend (symbol explanation)
3) Rendering (ASCII block)
4) POI list (Points of Interest: number→meaning→status)
5) Logic summary (this update reason/new info source/undetermined points)

---

## 4) Map Data Model (Must Save as .data.yaml)
Each map must have a structured data file for RAG and consistency verification.

### 4.1 Unified YAML Fields
```yaml
map_id: "macro_0001"
name: "Nebelmark Region Map"
type: "macro"                 # macro | micro
scale:
  mode: "hex"                 # hex | node | grid
  hex_miles: 6                # If hex
  grid_ft: null               # If grid
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
    coord: "H7"              # hex or grid coord
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
  - "Nebelheim must be near Rhine tributary"
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

Each map must have a logic explanation file answering three questions:

1. **Why drawn this way** (history/economy/military/terrain constraints)
2. **What's certain**, what's rumor/speculation
3. **How this map updates with plot**

### 5.1 Logic File Template

```md
# Logic — <map_id> <name>

## 1) Design Constraints (Hard Constraints)
- ...

## 2) Derivation Chain (Key Causality)
- Because A (French winter camp needs supply line) → Must have B (roads and village nodes) → Therefore placed at ...

## 3) Uncertainties and Fog Strategy
- Unexplored area: Keep ?; only reveal when player gains "survey/rumor/sighting"
- Rumor annotations: Use status=rumored, don't draw details, just mark a point

## 4) Update Rules (Diff Principle)
- Only incremental modifications: add POIs, reveal Fog, adjust RP/PI
- Don't redraw confirmed terrain (unless catastrophic event)

## 5) System Indicator Linkage
- Rumor≥2: Add "patrol/informant points" in city
- Debt rises: Mist active points * quantity increase or move
```

---

## 6) Command-Line "Map Generation Command" Spec (AI Operation Interface)

> This is not shell you actually execute, but "CLI-style protocol" you output to user/log.
> Each time player or DM issues command, you output: `COMMAND` → `RESULT` → `ARCHIVE_DELTA`.

### 6.1 Command Set (Recommended Minimum)

* `map new <type> <name> --scale <hex|node|grid> --id <...>`
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

Then give map rendering (or partial rendering), finally give ARCHIVE_DELTA (see section 7).

---

## 7) Save and Update: Must Write to Save (ARCHIVE_DELTA)

Each time map changes (new/reveal/add-poi/link/update-risk), must append at end:

```md
<!-- ARCHIVE_DELTA
files:
  - path: maps/MAP_INDEX.md
    patch: |
      - added: micro_0002_sewer.md (v1.0.0)
  - path: maps/micro/micro_0002_sewer.md
    append: |
      ## v1.0.0 Render
      ...
  - path: maps/micro/micro_0002_sewer.data.yaml
    patch: |
      - pois: ...
  - path: maps/micro/micro_0002_sewer.logic.md
    append: |
      ## Update Reason
      ...
-->
```

**Mandatory Requirements**:

* `.md` (render), `.data.yaml` (structure), `.logic.md` (logic) three-piece set indispensable.
* Each update must bump `version`, and record "update reason and source" in `.logic.md` (session clue / NPC testimony / measured path).

---

## 8) Consistency and Verification Rules (Prevent "forgot while drawing")

Before each map update, AI must perform self-check (completed internally, present as summary):

1. **Topology consistency**: Any road connection breaks? Any nodes isolated?
2. **Scale consistency**: Do travel time and distance match?
3. **Indicator consistency**: Do RP/PI/Heat/Rumor conflict with current plot status?
4. **Fog consistency**: Unexplored areas can't have detail POIs; rumored POIs don't get precise structure.
5. **Cross-map consistency**: Macro node `Nebelheim` corresponds to micro city map entrance/gate coordinates.

If conflict found, must:

* Add `uncertainties` in `.logic.md` or fix derivation;
* Or generate "temporary instance map" (/maps/instances/) for this session, merge into main map after confirmation.

---

## 9) Generation Workflow (Recommended)

### 9.1 Macro Map Workflow (Region)

1. `map new macro "Nebelmark Region Map" --scale hex --id macro_0001`
2. Draw terrain skeleton (river, mountain, forest, main roads)
3. Place triangular game nodes (French/Imperial/Burgundy key touchpoints)
4. Annotate RP/PI initial values and Mist active zones
5. Fog: Only reveal player-known range, rest `?`

### 9.2 Micro Map Workflow (City)

1. `map new micro "Nebelheim City Map" --scale node --id micro_0001`
2. Draw triple city defenses + refugee belt + guild street + Jewish lane + cathedral district + executioner bridge
3. Place key POIs (town hall, cellar, city gate, market, monastery, sewer outlet)
4. Bind each POI: faction, risk, obtainable resources, typical encounters
5. Only reveal specific alleys/internal structures after player exploration

### 9.3 Dungeon/Combat Grid Workflow (Dungeon/Grid)

1. `map new micro "Sewer Section" --scale grid --id micro_0002`
2. Initially only draw entrance and first room, rest `?`
3. Each time player advances a section: `map reveal` + update anomaly points `*`
4. Rooms must have: entrance/exit/cover/lighting/interactive objects

---

## 10) Minimum Example (Micro: Block Topology Map)

```txt
MAP: Nebelheim (micro_0001)  TYPE: micro(node)  VER: 1.0.0
Legend: #city wall  =main street  -alley  Ggate  Mmarket  Achurch  Rtown hall  JJewish lane  Xexecutioner bridge  ?unexplored  *anomaly

            ###########G###########
            #         =           #
            #   [A]===M===R       #
            #     -  ==  -        #
            #   J-?-==?- -        #
            #     -  ==  -    X   #
            #   [shantytown & outer moat]  -  #
            ###########G###########

POI:
[@1] A Cathedral District (known)
[@2] M Market (known)
[@3] R Town Hall and Cellar (known)
[@4] J Jewish Lane (rumored: locked at night; dense accounting houses)
[@5] X Executioner Bridge (known: high reputation cost)
[*1] Anomaly Point (hidden: low probability in fracture period)
```

---

## 11) RAG Tag Suggestions (For Retrieval)

In each map front matter `tags`, include at least:

* `region:<...>` / `city:<...>` / `dungeon:<...>`
* `era:1444` / `mist:crack_phase` / `mist:threshold_crossing`
* `faction:france|empire|burgundy|church|guild|vehm|outcasts`
* `economy:PI3` `risk:RP2` (optional)

— End of MAPS_GUIDE.md —

> Note: This repo has created `maps/` directory and `maps/MAP_INDEX.md`, subsequent map updates follow section 7 of this file via `ARCHIVE_DELTA` incremental writes.
