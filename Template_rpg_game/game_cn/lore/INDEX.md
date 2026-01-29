# lore/INDEX.md — Setting Library Index

> **Version**: v1.0 | **Purpose**: RAG Retrieval Entry | **Last Updated**: 2026-01-29

---

## 0. Quick Navigation

| Player Question | Retrieval Anchor | Fragment Limit |
|-----------------|------------------|----------------|
| "Tell me about the world" | `CANON/WORLD.md` | ≤3 paragraphs |
| "Who are the major factions?" | `CANON/FACTIONS.md` | ≤3 paragraphs |
| "What is the history?" | `CANON/TIMELINE.md` | ≤2 paragraphs |
| "Are there supernatural elements?" | `MIST/PHENOMENA.md` | ≤3 paragraphs |
| "How do indicators work?" | `MECHANICS/INDICATORS.md` | ≤1 paragraph |

---

## 1. Directory Structure

```
lore/
├── INDEX.md              ← You are here
├── WORLD_STATE.md        ← Backend world state (indicators, clocks, clues)
├── CANON/                ← Static world facts (your world setting)
│   ├── WORLD.md          ← World framework (geography, era)
│   ├── FACTIONS.md       ← Factions and organizations
│   └── TIMELINE.md       ← Historical events
├── MIST/                 ← Supernatural elements (optional)
│   ├── PHENOMENA.md      ← Supernatural phenomena
│   └── CREATURES.md      ← Creatures and entities
└── MECHANICS/            ← Mechanics settings
    └── INDICATORS.md     ← Indicator system rules
```

---

## 2. CANON Layer (Static World Facts)

### 2.1 WORLD.md — World Framework

| Tag | Content |
|-----|---------|
| `tags` | [canon, world, geography, era] |
| `related` | [FACTIONS.md, TIMELINE.md] |

**Quick Reference Anchors**:
- World name and general description
- Major geographic regions
- Political divisions
- Current era/age

### 2.2 FACTIONS.md — Factions and Organizations

| Tag | Content |
|-----|---------|
| `tags` | [canon, faction, organization] |
| `related` | [WORLD.md, TIMELINE.md] |

**Quick Reference**:
- List all major factions
- Brief description of each
- Their goals and methods

### 2.3 TIMELINE.md — Historical Events

| Tag | Content |
|-----|---------|
| `tags` | [canon, timeline, history] |
| `related` | [FACTIONS.md, WORLD.md] |

**Key Events**:
- Ancient history
- Recent events
- Current situation

---

## 3. MIST Layer (Supernatural Elements - Optional)

### 3.1 PHENOMENA.md — Supernatural Phenomena

| Tag | Content |
|-----|---------|
| `tags` | [mist, phenomenon, supernatural] |
| `related` | [CREATURES.md] |

**Contents**:
- Types of supernatural phenomena
- How they manifest
- Effects on the world

### 3.2 CREATURES.md — Creatures and Entities

| Tag | Content |
|-----|---------|
| `tags` | [mist, creature, entity, monster] |
| `related` | [PHENOMENA.md] |

**Contents**:
- Supernatural creatures
- Their abilities
- How to deal with them

---

## 4. MECHANICS Layer (Mechanics)

### 4.1 INDICATORS.md — Indicator System

| Tag | Content |
|-----|---------|
| `tags` | [mechanic, indicator] |
| `related` | [PHENOMENA.md] |

**Indicators**:
| Indicator | Range | Meaning |
|-----------|-------|---------|
| [Custom] | 0-X | Customizable for your game |

---

## 5. RAG Retrieval Rules

| Trigger Condition | Action |
|-------------------|--------|
| Player asks world-building question | Retrieve CANON/ files, output ≤3 fragments |
| Player asks mechanic question | Retrieve MECHANICS/ files, output ≤1 fragment |
| Player asks supernatural question | Retrieve MIST/ files, output ≤3 fragments |
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

*INDEX.md v1.0 - RPG Game Template*
