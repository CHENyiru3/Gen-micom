# MECHANICS/INDICATORS.md — Indicator System

> **Version**: v1.0 | **Last Updated**: 2026-01-29

---
tags: [mechanic, indicator]
related: [MIST/PHENOMENA.md]
---

# Indicator System

> **Purpose**: Define the indicators that track game state. Customize or remove as needed for your game.

---

## 0. Indicator Overview

| Indicator | Range | Description |
|-----------|-------|-------------|
| [Indicator 1] | 0-X | [Description] |
| [Indicator 2] | 0-X | [Description] |
| [Indicator 3] | 0-X | [Description] |

---

## 1. [Indicator Name]

### Description
[What does this indicator track?]

### Range
- 0 = [Minimum state]
- X = [Maximum state]

### Effects by Level
| Level | Effect |
|-------|--------|
| 0 | [Effect at 0] |
| 1 | [Effect at 1] |
| ... | ... |
| X | [Effect at max] |

### Changing the Indicator

#### Increases
| Trigger | Amount | Notes |
|---------|--------|-------|
| [Trigger 1] | +1 | [Notes] |
| [Trigger 2] | +2 | [Notes] |

#### Decreases
| Trigger | Amount | Notes |
|---------|--------|-------|
| [Trigger 1] | -1 | [Notes] |
| [Trigger 2] | -2 | [Notes] |

---

## 2. [Indicator Name]

### Description
[What does this indicator track?]

### Range
- 0 = [Minimum state]
- X = [Maximum state]

### Effects by Level
| Level | Effect |
|-------|--------|
| 0 | [Effect at 0] |
| 1 | [Effect at 1] |
| ... | ... |
| X | [Effect at max] |

### Changing the Indicator

#### Increases
| Trigger | Amount | Notes |
|---------|--------|-------|
| [Trigger 1] | +1 | [Notes] |
| [Trigger 2] | +2 | [Notes] |

#### Decreases
| Trigger | Amount | Notes |
|---------|--------|-------|
| [Trigger 1] | -1 | [Notes] |
| [Trigger 2] | -2 | [Notes] |

---

## 3. Using Indicators in Play

### Display
- Display indicator values in `STATE_PANEL.md`
- Update via `ARCHIVE_DELTA` each turn

### Reference
- DM references indicators during adjudication
- Include in `HOT_PACK.md` for context

### Milestones
- [Milestone 1]: [Effect]
- [Milestone 2]: [Effect]

---

## 4. Customization Guide

To customize indicators for your game:

1. **Add new indicators**: Add new sections following the template
2. **Remove indicators**: Remove sections that don't apply
3. **Modify ranges**: Adjust ranges to match your game's balance
4. **Add triggers**: Add new triggers for increasing/decreasing

---

## 5. Game Connections

### Related Mechanics
- [Mechanic 1]: [Connection]
- [Mechanic 2]: [Connection]

### Related Lore
- [Lore 1]: [Connection]
- [Lore 2]: [Connection]
