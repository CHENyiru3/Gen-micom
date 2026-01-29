# LOCATION_INDEX.md
Version: v1.0
Last Updated: 2026-01-29

---

## RAG_HEAD (4-6 line summary)

- City layers: Outer/Middle/Inner/Outside city.
- 12 existing locations, all pending exploration.
- @loc_020-022 are power/church core areas.
- @loc_030-032 are outside city and edge trading areas.

## Index field specification (compatible with template cartridge)

| Field | Description |
|-------|-------------|
| handle | Recommended @handle (stable reference) |
| id | Legacy ID (retained for compatibility) |
| name | Human-readable name |
| summary | One-line overview |
| status | Pending exploration/Visited/Established |

## Handle mapping (don't change original content)

| handle | id | name |
|--------|----|------|
| @loc_001 | loc_001 | Outer Shantytown |
| @loc_002 | loc_002 | City Gate Checkpoint |
| @loc_010 | loc_010 | Guild Street |
| @loc_011 | loc_011 | Market Square |
| @loc_012 | loc_012 | Tavern District |
| @loc_013 | loc_013 | Jewish Quarter |
| @loc_020 | loc_020 | Cathedral District |
| @loc_021 | loc_021 | City Hall |
| @loc_022 | loc_022 | Bishop's Palace |
| @loc_030 | loc_030 | Executioner's Bridge |
| @loc_031 | loc_031 | Linden Execution Ground |
| @loc_032 | loc_032 | Abandoned Quarry |

## Nebelheim City Structure

### Outer Layer
| ID | Location | Description | Status |
|----|----------|-------------|--------|
| loc_001 | Outer Shantytown | Refugees and poor gather, black market active | Pending exploration |
| loc_002 | City Gate Checkpoint | City guards enforce taxes and inspections | Pending exploration |

### Middle Layer
| ID | Location | Description | Status |
|----|----------|-------------|--------|
| loc_010 | Guild Street | Workshops and guild towers | Pending exploration |
| loc_011 | Market Square | Trade and rumor center | Pending exploration |
| loc_012 | Tavern District | Beer and information | Pending exploration |
| loc_013 | Jewish Quarter | Medicine and accounting | Pending exploration |

### Inner Layer
| ID | Location | Description | Status |
|----|----------|-------------|--------|
| loc_020 | Cathedral District | Power and faith center | Pending exploration |
| loc_021 | City Hall | Political decisions | Pending exploration |
| loc_022 | Bishop's Palace | Church authority | Pending exploration |

### Outside City
| ID | Location | Description | Status |
|----|----------|-------------|--------|
| loc_030 | Executioner's Bridge | Edge trading | Pending exploration |
| loc_031 | Linden Execution Ground | Vehm Court symbols | Pending exploration |
| loc_032 | Abandoned Quarry | Potential dungeon | Pending exploration |

---

## Location Detail Template

```md
## loc_XXX:
- **Name**:
- **Area**: Outer/Middle/Inner/Outside city
- **Description**:
- **Faction Control**:
- **Key NPCs**:
- **Entrance/Exit**:
- **Risk**:
- **Opportunity**:
- **Mist Connection**:
- **Exploration Status**: Unexplored/Visited/Established
```

---

## Established Locations

*(Filled after game starts)*

| ID | File Path | Exploration Status |
|----|-----------|-------------------|
| - | - | - |

---

## Todo

- [ ] Establish opening scene location details
- [ ] Supplement key location details
