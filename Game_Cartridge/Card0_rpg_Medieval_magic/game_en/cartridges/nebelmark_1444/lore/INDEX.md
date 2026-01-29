# lore/INDEX.md — Mist Border Setting Library Index

> **Version**: v1.1 | **Purpose**: RAG retrieval entry | **Last Updated**: 2026-01-29

## RAG_HEAD (4-6 line summary)

- Canon: WORLD/FACTIONS/TIMELINE are daytime history source of truth.
- Mist: LAESURAE/PHENOMENA are explorable mist settings.
- Mechanics: INDICATORS is four-indicator rules entry.
- Keyword retrieval prioritizes locating from this index table.

## Index field specification (compatible with template cartridge)

| Field | Description |
|-------|-------------|
| handle | Recommended @handle (stable reference) |
| file | Target file |
| tags | Key tags |
| summary | One-line purpose description |

## Handle mapping (don't change original content)

| handle | file | summary |
|--------|------|---------|
| @lore_world | CANON/WORLD.md | World framework |
| @lore_factions | CANON/FACTIONS.md | Faction details |
| @lore_timeline | CANON/TIMELINE.md | Timeline |
| @lore_city | MIST/LAESURAE.md | City appearance |
| @lore_phenomena | MIST/PHENOMENA.md | Mist phenomena |
| @lore_indicators | MECHANICS/INDICATORS.md | Indicator rules |

---

## 0. Quick Navigation

| Player Question | Retrieval Anchor | Fragment Limit |
|-----------------|------------------|----------------|
| "How is the church in this era?" | `CANON/WORLD.md` + `tags: [church]` | ≤3 fragments |
| "What is the Vehm Court?" | `CANON/FACTIONS.md` + `tags: [vehm]` | ≤2 fragments |
| "What is Nebelheim structure?" | `MIST/LAESURAE.md` + `tags: [city, urban]` | ≤2 fragments |
| "Who is Charles VII?" | `CANON/FACTIONS.md` + `tags: [npc, france]` | ≤1 fragment |
| "How does Grace work?" | `MECHANICS/INDICATORS.md` | ≤1 fragment |
| "What strange phenomena exist?" | `MIST/PHENOMENA.md` | ≤3 fragments |

---

## 1. Directory Structure

```
lore/
├── INDEX.md              ← You are here
├── CANON/                ← Daytime history (unchangeable)
│   ├── WORLD.md          ← World framework (map/era/factions)
│   ├── FACTIONS.md       ← Six factions details
│   └── TIMELINE.md       ← 1444-1446 major events
├── MIST/                 ← Mist history (explorable)
│   ├── LAESURAE.md       ← City appearance and street environment
│   └── PHENOMENA.md      ← Imaginary creatures and strange phenomena
└── MECHANICS/            ← Mechanics settings
    ├── INDICATORS.md     ← Four indicator rules (Grace/Debt/Rumor/Heat)
    └── RANDOM_TABLES.md  ← Random encounter tables
```

---

## 2. CANON Layer (Daytime History)

### 2.1 WORLD.md — World Framework

| Tags | Content |
|------|---------|
| `tags` | [canon, world, geography, era] |
| `related` | [FACTIONS.md, TIMELINE.md] |

**Quick anchors**:
- Mist Border: Nebelmark, left bank of upper Rhine
- Main city: Nebelheim
- Era: 1444 (Crack Phase)
- Design pillars: Daytime history not overturned, fantasy appears as "seepage", divine punishment and redemption coexist

### 2.2 FACTIONS.md — Six Factions

| Tags | Content |
|------|---------|
| `tags` | [canon, faction, france, empire, burgundy, church, vehm] |
| `related` | [WORLD.md, TIMELINE.md] |

**Faction quick reference**:
- Kingdom of France: Valois dynasty, Charles VII, mercenary export
- Holy Roman Empire: Hollow crown, central powerlessness
- Duchy of Burgundy: Philip the Good, infiltration strategy
- Church: Council of Basel, fragile authority
- Vehm Court: Secret judgment system, mist history faction
- Skinners: Mercenary consortium

### 2.3 TIMELINE.md — Major Events

| Tags | Content |
|------|---------|
| `tags` | [canon, timeline, history] |
| `related` | [FACTIONS.md, WORLD.md] |

**Key nodes**:
- 1429: Clement VIII abdicated
- 1444: Crack Phase begins, individual anomalies increase
- 1445/46: Threshold crossing (transience occurs), mist stabilizes

### 2.4 Char.md — 1444 Rhine Crisis Character Network (Extended canon)

| Tags | Content |
|------|---------|
| `tags` | [canon, character-network, rhine_crisis, era:1444] |
| `related` | [CANON/WORLD.md, CANON/FACTIONS.md, CANON/TIMELINE.md] |

**Purpose**:
- When player/DM needs "1444 Rhine crisis character relationship network, faction projection, available adventure hooks", retrieve small snippets (≤2 fragments) from this file.

---

## 3. MIST Layer (Mist History)

### 3.1 LAESURAE.md — City Appearance and Street Environment

| Tags | Content |
|------|---------|
| `tags` | [mist, location, city, urban, vice] |
| `related` | [PHENOMENA.md, WORLD.md] |

**Districts**:
- Outer shantytown and refugee belt: Hungry siege
- Guild street and workshop belt: Noise, craft, and calculation
- Market and tavern: Rumor engine
- Jewish quarter and accounting: Sword of text
- Cathedral district and monasteries: Light and decay coexist
- Executioner's Bridge and outside city edge: Cursed necessary evil

### 3.2 PHENOMENA.md — Imaginary Creatures and Strange Phenomena

| Tags | Content |
|------|---------|
| `tags` | [mist, creature, phenomenon, religion, heresy] |
| `related` | [LAESURAE.md, INDICATORS.md] |

**Imaginary creatures**:
- Penitent Lark, Confessional Slug, Stigmata Mendicant
- Candleborne Children, Ash-Salt Friar, Mist Court Advocate

**Crack Phase phenomena**:
- Dream Plague, Mist Mark, Leaky Sanctuary, Displaced Ledger
- Dagger on Tree, Wild Hunt Afterimage

---

## 4. MECHANICS Layer (Mechanics)

### 4.1 INDICATORS.md — Four Indicator System

| Tags | Content |
|------|---------|
| `tags` | [mechanic, indicator, grace, debt, rumor, heat] |
| `related` | [PHENOMENA.md] |

**Indicators**:
| Indicator | Range | Meaning |
|-----------|-------|---------|
| Grace | 0-10 | Divine order availability |
| Debt | 0-10 | Human redemption pressure |
| Rumor | 0-3 | Public discussion of anomalies |
| Heat | 0-3 | Faction attention level |

**Core rules**:
- Public spellcasting/monster sightings → Rumor+1
- Rumor≥2 → Investigation forces must intervene
- Violence/abuse of magic → Debt+1
- Saving people/refusing temptation → Debt-1 or Grace+1

### 4.2 RANDOM_TABLES.md — Random Encounter Tables

| Tags | Content |
|------|---------|
| `tags` | [random, encounter, table, urban, travel, dream] |
| `related` | [MIST/LAESURAE.md] |

**Encounter types**:
- Street encounters d10 (risk, clue, environment)
- Night encounters d8 (mystery, weird, alert)
- Dream fragments d6 (trauma, rift, omen)

---

## 5. RAG Retrieval Rules

| Trigger Condition | Action |
|-------------------|--------|
| Player asks world question | Retrieve CANON/ files, output ≤3 fragments |
| Player asks mechanic question | Retrieve MECHANICS/ files, output ≤1 fragment |
| Player asks strange phenomena | Retrieve MIST/PHENOMENA.md, output ≤3 fragments |
| Player asks city environment | Retrieve MIST/LAESURAE.md, output ≤2 fragments |
| Player asks NPC background | Retrieve CANON/FACTIONS.md or NPCs/, output ≤2 fragments |

**Prohibit**: Stuff entire table/chapter into context

---

## 6. File Templates

New setting files please use this template:

```md
---
tags: [canon|mist|mechanic, main_tag, sub_tag]
related: [related_file.md]
---

# File Title

## 0. Quick Anchor
- Key concept 1
- Key concept 2

## 1. Core Setting
(Text, retrievable by RAG fragments)

## 2. Game Connection
- Related locations: loc_xxx
- Related quests: quest_xxx
- Related NPCs: npc_xxx
```

---

*INDEX.md v1.1 - Chronicles of the Misty Border*
