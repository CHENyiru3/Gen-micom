# lore/INDEX.md — Mist Frontier Setting Library Index

> **Version**: v1.1 | **Purpose**: RAG Retrieval Entry | **Last Updated**: 2026-01-29

---

## 0. Quick Navigation

| Player Question | Retrieval Anchor | Fragment Limit |
|-----------------|------------------|----------------|
| "How is the church in this era?" | `CANON/WORLD.md` + `tags: [church]` | ≤3 paragraphs |
| "What is the Fehm Court?" | `CANON/FACTIONS.md` + `tags: [vehm]` | ≤2 paragraphs |
| "Nebelhheim structure?" | `MIST/LAESURAE.md` + `tags: [city, urban]` | ≤2 paragraphs |
| "Who is Charles VII?" | `CANON/FACTIONS.md` + `tags: [npc, france]` | ≤1 paragraph |
| "How to use Grace?" | `MECHANICS/INDICATORS.md` | ≤1 paragraph |
| "What uncanny phenomena are there?" | `MIST/PHENOMENA.md` | ≤3 paragraphs |

---

## 1. Directory Structure

```
lore/
├── INDEX.md              ← You are here
├── CANON/                ← Daylight History (unchangeable)
│   ├── WORLD.md          ← World framework (map/era/factions)
│   ├── FACTIONS.md       ← Six factions details
│   └── TIMELINE.md       ← 1444-1446 major events
├── MIST/                 ← Mist History (explorable)
│   ├── LAESURAE.md       ← City appearance and street environment
│   └── PHENOMENA.md      ← Strange creatures and uncanny phenomena
└── MECHANICS/            ← Mechanics settings
    ├── INDICATORS.md     ← Four indicator rules (Grace/Debt/Rumor/Heat)
    └── RANDOM_TABLES.md  ← Random encounter tables
```

---

## 2. CANON Layer (Daylight History)

### 2.1 WORLD.md — World Framework

| Tag | Content |
|-----|---------|
| `tags` | [canon, world, geography, era] |
| `related` | [FACTIONS.md, TIMELINE.md] |

**Quick Reference Anchors**:
- Mist Frontier: Nebelmark, located on left bank of upper Rhine
- Capital City: Nebelheim
- Era: 1444 (Fracture Period)
- Design Pillars: Daylight History not overturned, fantasy appears as "seepage", divine punishment and redemption coexist

### 2.2 FACTIONS.md — Six Factions

| Tag | Content |
|-----|---------|
| `tags` | [canon, faction, france, empire, burgundy, church, vehm] |
| `related` | [WORLD.md, TIMELINE.md] |

**Faction Quick Reference**:
- Kingdom of France: Valois dynasty, Charles VII, mercenary export
- Holy Roman Empire: Hollow crown, center powerless
- Duchy Burgundy: Philip the Good, infiltration strategy
- Church: Basel Council, authority fragile
- Fehm Court: Secret trial system, Mist History faction
- Flayers: Mercenary consortium

### 2.3 TIMELINE.md — Major Events

| Tag | Content |
|-----|---------|
| `tags` | [canon, timeline, history] |
| `related` | [FACTIONS.md, WORLD.md] |

**Key Nodes**:
- 1429: Clement VIII abdicates
- 1444: Fracture Period start, individual strange incidents increase
- 1445/46: Threshold crossing (Flux occurs), Mist stabilizes

### 2.4 Char.md — 1444 Rhine Crisis Character Network (Extended canon)

| Tag | Content |
|-----|---------|
| `tags` | [canon, character-network, rhine_crisis, era:1444] |
| `related` | [CANON/WORLD.md, CANON/FACTIONS.md, CANON/TIMELINE.md] |

**Purpose**:
- When player/DM needs "1444 Rhine Crisis character relationship network, faction projections, available adventure hooks", retrieve small fragments of this file (≤2 paragraphs).

---

## 3. MIST Layer (Mist History)

### 3.1 LAESURAE.md — City Appearance and Street Environment

| Tag | Content |
|-----|---------|
| `tags` | [mist, location, city, urban, vice] |
| `related` | [PHENOMENA.md, WORLD.md] |

**Districts**:
- Outer shantytowns and refugee zones: Hungry siege
- Guild street and workshop zone: Noise, craftsmanship, calculation
- Markets and taverns: Rumor engine
- Jewish lane and accounting houses: Swords of text
- Cathedral district and monasteries: Light and decay coexist
- Executioner Bridge and城外 outskirts: Cursed necessary evil

### 3.2 PHENOMENA.md — Strange Creatures and Uncanny Phenomena

| Tag | Content |
|-----|---------|
| `tags` | [mist, creature, phenomenon, religion, heresy] |
| `related` | [LAESURAE.md, INDICATORS.md] |

**Strange Creatures**:
- Penitence Bird, Confession Slug, Stigmata Beggar
- Seven Candle Child, Salt Ash Monk, Mist Court Debater

**Fracture Period Phenomena**:
- Dream Plague, Fog Marks, Leaking Sanctuary, Displaced Ledger
- Daggers in Trees, Wild Hunt Afterimages

---

## 4. MECHANICS Layer (Mechanics)

### 4.1 INDICATORS.md — Four Indicator System

| Tag | Content |
|-----|---------|
| `tags` | [mechanic, indicator, grace, debt, rumor, heat] |
| `related` | [PHENOMENA.md] |

**Indicators**:
| Indicator | Range | Meaning |
|-----------|-------|---------|
| Grace | 0-10 | Divine order availability |
| Debt | 0-10 | Human redemption pressure |
| Rumor | 0-3 | Public discussion of uncanny |
| Heat | 0-3 | Power institution attention |

**Core Rules**:
- Public spell casting/monster sighting → Rumor+1
- Rumor≥2 → Investigation forces must intervene
- Violence/magic abuse → Debt+1
- Saving people/refusing temptation → Debt-1 or Grace+1

### 4.2 RANDOM_TABLES.md — Random Encounter Tables

| Tag | Content |
|-----|---------|
| `tags` | [random, encounter, table, urban, travel, dream] |
| `related` | [MIST/LAESURAE.md] |

**Encounter Types**:
- Street encounters d10 (risk, clue, environment)
- Night encounters d8 (mysterious, uncanny, alertness)
- Dream fragments d6 (trauma, rift, omen)

---

## 5. RAG Retrieval Rules

| Trigger Condition | Action |
|-------------------|--------|
| Player asks world-building question | Retrieve CANON/ files, output ≤3 fragments |
| Player asks mechanic question | Retrieve MECHANICS/ files, output ≤1 fragment |
| Player asks uncanny phenomenon | Retrieve MIST/PHENOMENA.md, output ≤3 fragments |
| Player asks city environment | Retrieve MIST/LAESURAE.md, output ≤2 fragments |
| Player asks NPC background | Retrieve CANON/FACTIONS.md or NPCs/, output ≤2 fragments |

**Prohibited**: Stuffing entire tables/chapters into context

---

## 6. File Template

Use this template for new setting files:

```md
---
tags: [canon|mist|mechanic, main_tag, secondary_tag]
related: [related_file.md]
---

# File Title

## 0. Quick Reference Anchors
- Key concept 1
- Key concept 2

## 1. Core Settings
(Main text, searchable by RAG fragments)

## 2. Game Connections
- Related locations: loc_xxx
- Related quests: quest_xxx
- Related NPCs: npc_xxx
```

---

*INDEX.md v1.1 - Chronicle of the Mist Frontier*
