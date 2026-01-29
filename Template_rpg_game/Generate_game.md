# Generate_game.md — Game Template Generation Guide

> **Purpose**: This guide explains how to transform this template into a complete, playable game card using your own world setting, prompts, and content.
> **Prerequisites**: Read `game_en/README.md` or `game_cn/README.md` first to understand the template structure.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Step 1: Define Your World](#2-step-1-define-your-world)
3. [Step 2: Customize Mechanics](#3-step-2-customize-mechanics)
4. [Step 3: Create Content](#4-step-3-create-content)
5. [Step 4: Add Maps](#5-step-4-add-maps)
6. [Step 5: Create Starting Campaign](#6-step-5-create-starting-campaign)
7. [Step 6: Test Your Game](#7-step-6-test-your-game)
8. [Template Variables Reference](#8-template-variables-reference)
9. [File-by-File Guide](#9-file-by-file-guide)

---

## 1. Overview

This template provides a complete structure for an AI-driven TTRPG game. To create your own game, you need to:

1. **Fill in the blanks** in lore files (`lore/CANON/`)
2. **Customize rules** in mechanics files (`mechanics/`)
3. **Create content** (NPCs, locations, quests)
4. **Design maps** using the map templates
5. **Configure the starting campaign**

The process is designed to be **modular** — you can start playing with minimal customization and expand over time.

---

## 2. Step 1: Define Your World

### 2.1 Core World Questions

Before filling in templates, answer these questions:

| Question | Your Answer |
|----------|-------------|
| What is your world's name? | |
| What genre is it? (Fantasy, Sci-Fi, Horror, etc.) | |
| What is the current era/age? | |
| What are the major regions? | |
| What are the major factions? | |
| What supernatural elements exist (if any)? | |
| What is the technological/magical level? | |
| What are the major conflicts? | |

### 2.2 Fill In World Files

#### `lore/CANON/WORLD.md` (Most Important)

This is your **primary world definition file**. Fill in all sections:

```markdown
# YOUR_WORLD_NAME

## 0. Quick Reference Anchors
- World Type: [Your answer]
- Major Regions: [List]
- Current Era: [Your answer]
- Key Theme: [Your answer]

## 1. Core Settings
[Write 2-3 paragraphs about your world]

### 1.1 Geography
[Describe major geographic features]

### 1.2 Political Structure
[Describe major powers and their relationships]
```

#### `lore/CANON/FACTIONS.md`

List all major factions:

```markdown
## 1. Major Factions

### Faction: [Faction Name]
**ID**: fac_001
**Type**: [Government/Religion/Criminal/Mercantile/Military]
**Alignment**: [Good/Neutral/Evil]
**Influence**: [Local/Regional/National/Global]

#### Overview
[Brief description]

#### Goals
- [Primary goal]
- [Secondary goal]

#### Methods
[How they pursue goals]
```

#### `lore/CANON/TIMELINE.md`

Create a timeline of major historical events:

```markdown
## 1. Ancient History

| Year | Event | Significance |
|------|-------|--------------|
| [Year] | [Event] | [Why it matters] |
```

### 2.3 Optional: Add Supernatural Elements

If your game has supernatural elements, fill in `lore/MIST/`:

- `PHENOMENA.md` — Types of supernatural phenomena
- `CREATURES.md` — Supernatural creatures

If your game is purely mundane, you can leave these files mostly empty or remove the `MIST/` folder.

---

## 3. Step 2: Customize Mechanics

### 3.1 Core Rules File

Edit `mechanics/HOUSE_RULES.md` to define your game's rules:

```markdown
## 0) Dice System

### Basic Roll Formula
- **Attribute Check**: `1d20 + Attribute Modifier` vs DC
- **Skill Check**: `1d20 + Skill Bonus` vs DC

[Customize the rules for your game]
```

### 3.2 Combat System

Edit `mechanics/COMBAT.md`:

```markdown
## 3) Attack Rolls

### Attack Roll Formula
```
1d20 + Ability Modifier + Proficiency Bonus
```

[Add your game's combat rules, weapons, armor, etc.]
```

### 3.3 Other Mechanics Files

| File | What to Customize |
|------|-------------------|
| `SURVIVAL.md` | Survival rules (food, water, shelter) |
| `SOCIAL_INVESTIGATION.md` | Social interaction and investigation rules |
| `RAG_RULES.md` | Retrieval rules (usually leave as-is) |
| `TRACKERS.md` | Templates for manual tracking |

### 3.4 Indicator System

Edit `lore/MECHANICS/INDICATORS.md` to define game-specific indicators:

```markdown
## 1. [Your Indicator Name]

### Description
[What does this indicator track?]

### Range
- 0 = [Minimum]
- X = [Maximum]

### Effects by Level
| Level | Effect |
|-------|--------|
| 0 | [Effect] |
| X | [Effect] |
```

---

## 4. Step 3: Create Content

### 4.1 Create NPCs

Create individual NPC files in `characters/NPCs/`:

**Template**:
```markdown
---
tags: [npc, character]
---

# [NPC Name]

## Basic Information

| Field | Value |
|-------|-------|
| ID | npc_[name] |
| Name | [Name] |
| Faction | [Faction ID] |
| Role | [Role] |

## Public Identity

[Description that players can learn]

## Secret Information

### Hidden Agenda
[What they're really up to]

### Secrets
- **Easy to discover**: [Secret 1]
- **Hard to discover**: [Secret 2]
```

### 4.2 Create Locations

Create location files in `locations/`:

**Template**:
```markdown
---
tags: [location, place]
---

# [Location Name]

## Overview

**Type**: [City/Town/Dungeon/etc.]
**Region**: [Region ID]
**Population**: [Number]

## Description

[Atmospheric description]

## Points of Interest

| POI | Description | Notes |
|-----|-------------|-------|
| | | |

## NPCs

| NPC | Role | Description |
|-----|------|-------------|
| | | |

## Secrets

- [Secret 1]
```

### 4.3 Create Quests

Create quest files or add to `quests/QUEST_LOG.md`:

**Template**:
```markdown
## quest_XXX:

- **Title**: [Quest Name]
- **Type**: [Main/Side/Background]
- **Status**: [Active]
- **Client**: [Who gave the quest]
- **Objectives**:
  1. [Objective 1]
  2. [Objective 2]
- **Rewards**:
  - Experience: [Amount]
  - Gold: [Amount]
  - Items: [Items]
- **Time Limit**: [None or time period]
- **Consequences**:
  - Success: [What happens]
  - Failure: [What happens]
```

---

## 5. Step 4: Add Maps

### 5.1 Create a Regional Map

1. Copy macro template:
   ```bash
   cp maps/macro/macro_0001_template.md maps/macro/macro_0001_[region].md
   cp maps/macro/macro_0001_template.data.yaml maps/macro/macro_0001_[region].data.yaml
   cp maps/macro/macro_0001_template.logic.md maps/macro/macro_0001_[region].logic.md
   ```

2. Fill in the render file (`macro_0001_[region].md`)

3. Update the data file (`macro_0001_[region].data.yaml`)

4. Update the logic file if needed

5. Register in `maps/MAP_INDEX.md`

### 5.2 Create a Location Map

1. Copy micro template:
   ```bash
   cp maps/micro/micro_0001_template.md maps/micro/micro_0001_[location].md
   cp maps/micro/micro_0001_template.data.yaml maps/micro/micro_0001_[location].data.yaml
   cp maps/micro/micro_0001_template.logic.md maps/micro/micro_0001_[location].logic.md
   ```

2. Fill in the render file with room descriptions

3. Update the data file with nodes, NPCs, hazards, treasure

4. Update the logic file if needed

5. Register in `maps/MAP_INDEX.md`

---

## 6. Step 5: Create Starting Campaign

### 6.1 Create Campaign Directory

```bash
python3 scripts/campaign_manager.py new --id campaign_0001
```

Or manually:
```bash
cp -r campaigns/_template campaigns/campaign_0001
```

### 6.2 Configure Starting State

Edit `campaigns/campaign_0001/root/STATE_PANEL.md`:

```markdown
## Time

| Date | Season | Special Date |
|------|--------|--------------|
| [Start Date] | [Season] | - |

## [Your Indicators]

| Indicator | Current | Max | Notes |
|-----------|---------|-----|-------|
| [Indicator] | [Value] | [Max] | |
```

### 6.3 Create Opening Session

Edit `campaigns/campaign_0001/sessions/session_0001_start.md`:

```markdown
# Session 1: [Session Title]

> **Date**: YYYY-MM-DD

## Decision: Campaign Start

- Real time: YYYY-MM-DD
- In-world time: [Start Date]
- Player input: Character creation complete
- Resolution: Campaign begins at [Starting Location]
- Starting location: [Location ID]
- Opening hook: [Brief description of starting situation]
```

---

## 7. Step 6: Test Your Game

### 7.1 Quick Test Checklist

- [ ] All template placeholders are replaced
- [ ] World files are filled in
- [ ] At least one NPC exists
- [ ] At least one location exists
- [ ] Combat rules are defined
- [ ] Starting campaign is configured
- [ ] Map is registered in MAP_INDEX.md

### 7.2 Play Test

1. Start an LLM session with the game files
2. Send `<Initialize>`
3. Complete character creation
4. Test basic interactions (movement, conversation)
5. Test combat if applicable
6. Verify `ARCHIVE_DELTA` is being written

### 7.3 Common Issues

| Issue | Solution |
|-------|----------|
| LLM doesn't know world info | Ensure lore files are in correct location |
| Combat rules unclear | Simplify HOUSE_RULES.md and COMBAT.md |
| Game state not persisting | Check `ARCHIVE_DELTA` format |
| NPC behavior inconsistent | Add clearer NPC motivation sections |

---

## 8. Template Variables Reference

### Placeholder Markers

| Marker | Meaning | Replace With |
|--------|---------|--------------|
| `[Your ...]` | Your custom content | World-specific content |
| `[Custom]` | Optional game element | Game-specific element or remove |
| `[Template]` | File to be copied | Use cp command |
| `fac_XXX` | Faction ID | Your faction ID (e.g., fac_kingdom) |
| `npc_XXX` | NPC ID | Your NPC ID |
| `loc_XXX` | Location ID | Your location ID |
| `quest_XXX` | Quest ID | Your quest ID |
| `map_XXX` | Map ID | Your map ID |

### ID Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Faction | `fac_[name]` | `fac_kingdom` |
| NPC | `npc_[name]` | `npc_marcus` |
| Location | `loc_[name]` | `loc_tavern` |
| Quest | `quest_[name]` | `quest_save_village` |
| Map | `[type]_[number]_[name]` | `macro_0001_region` |

---

## 9. File-by-File Guide

### Core Files (Do Not Modify)

These files define **how the game runs** and should remain stable:

| File | Purpose |
|------|---------|
| `KERNEL_PROMPT.md` | Turn pipeline, HUD, RAG, ARCHIVE_DELTA |
| `System.md` | World instance router |
| `CLI_SPEC.md` | Player input protocol |
| `HOT_START.md` | Resume procedure |
| `INIT_PROTOCOL.md` | Initialization flow |
| `ARCHIVE_DELTA.md` | Save format |
| `CONTINUITY_CHECK.md` | Drift verification |
| `mechanics/RAG_RULES.md` | Retrieval rules |

### Template Files (Fill In)

These files contain **your world content**:

| File | Fill In |
|------|---------|
| `lore/CANON/WORLD.md` | World geography, regions, overview |
| `lore/CANON/FACTIONS.md` | Major organizations and their goals |
| `lore/CANON/TIMELINE.md` | Historical events |
| `lore/MIST/PHENOMENA.md` | Supernatural phenomena (optional) |
| `lore/MECHANICS/INDICATORS.md` | Game indicators |
| `mechanics/HOUSE_RULES.md` | Dice rules, DCs, modifiers |
| `mechanics/COMBAT.md` | Combat system |
| `mechanics/SURVIVAL.md` | Survival rules |
| `mechanics/SOCIAL_INVESTIGATION.md` | Social rules |
| `maps/macro/*.md` | Regional map descriptions |
| `maps/micro/*.md` | Location map descriptions |

### Content Files (Create)

These files are **created during game development**:

| File | When to Create |
|------|----------------|
| `characters/NPCs/npc_*.md` | When you have NPCs |
| `locations/loc_*.md` | When you have locations |
| `quests/QUEST_LOG.md` | When you have quests |
| `maps/macro/*.data.yaml` | When creating macro maps |
| `maps/micro/*.data.yaml` | When creating micro maps |
| `campaigns/*/root/*.md` | When starting campaigns |

---

## Quick Start Checklist

- [ ] Copy template to your game directory
- [ ] Fill in `lore/CANON/WORLD.md`
- [ ] Fill in `lore/CANON/FACTIONS.md`
- [ ] Customize `mechanics/HOUSE_RULES.md`
- [ ] Create at least one NPC
- [ ] Create at least one location
- [ ] Create starting campaign with `campaign_manager.py`
- [ ] Test with `<Initialize>`

---

*Template Generation Guide v1.0*
