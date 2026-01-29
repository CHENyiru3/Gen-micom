# SURVIVAL.md — Survival and Resource Rules

> **Purpose**: Daily consumption, physical condition, rest rules
> **When to Retrieve**: When player needs survival check or resource management
> **tags**: [survival, resource, consumption, rest, condition]

---

## SURVIVAL::consumption Daily Consumption

| Item | Price (Silver) |
|------|----------------|
| One day rations (bread/dried meat) | 2 |
| A pot of beer | 1 |
| One night lodging (hay) | 1 |
| One night lodging (inn) | 5-10 |
| A pound of candles | 3 |
| A pot of water | 0.5 |

---

## SURVIVAL::condition Physical Condition

| Status | Effect |
|--------|--------|
| **Hungry** | -1 all checks, -2 if 3 days without food |
| **Dehydrated** | -2 all checks, -3 if 2 days without water |
| **Fatigued** | -1 all checks, -2 if 1 night without sleep |
| **Injured/Sick** | -1~-3 (depending on severity) |

---

## SURVIVAL::rest Rest Rules

| Rest Type | Recovery | Requirements |
|-----------|----------|--------------|
| Short rest (1 hour) | Recover 1d6 HP | Safe location |
| Long rest (8 hours) | Recover full HP | Safe location, adequate food |
| Complete rest (24 hours) | Recover all status | Safe location, adequate food and water |

---

## SURVIVAL::travel Travel Rules

### Daily March
- Normal march: 8 hours/day, 24-32 km
- Forced march: 10 hours/day, 40-48 km (fatigue+1)
- Slow march: 6 hours/day, 16-20 km (safer)

### Supply Consumption
- Walking: Rations 2 silver/day
- Riding: Hay 1 silver/day + rations 2 silver/day

### Weather Impact

| Weather | Effect |
|---------|--------|
| Sunny | Normal march |
| Light rain | March speed -10% |
| Heavy rain/blizzard | March speed -30%, need lodging |
| Extreme weather | Must stop |

---

## SURVIVAL::hunger Hunger and Dehydration

### Hunger Stages

| Days | Status | Effect |
|------|--------|--------|
| 0-1 | Normal | No penalty |
| 2 | Mild hunger | -1 all checks |
| 3 | Moderate hunger | -1 all checks |
| 4+ | Severe hunger | -2 all checks, weakened |

### Dehydration Stages

| Days | Status | Effect |
|------|--------|--------|
| 0-1 | Normal | No penalty |
| 2 | Mild dehydration | -1 all checks |
| 3 | Moderate dehydration | -2 all checks |
| 4+ | Severe dehydration | -3 all checks, risk of unconsciousness |

---

## SURVIVAL::encumbrance Encumbrance Limits

| Load Level | Load Limit | Check Penalty |
|------------|------------|---------------|
| Light | ≤50 lbs | None |
| Medium | 51-100 lbs | -1 |
| Heavy | 101-150 lbs | -2 |
| Overloaded | >150 lbs | -5, cannot run |

---

## SURVIVAL::shelter Shelter

### Shelter Types

| Type | Protection Effect | Build Time | Material Cost |
|------|-------------------|------------|---------------|
| Open air | None | 0 | 0 |
| Rock shelter | Rain protection | 1 hour | 0 |
| Simple tent | Wind and rain protection | 2 hours | 5 silver |
| Shelter | Good protection | 8 hours | 20 silver |
| Inn | Best protection | - | 5-10 silver/night |

### Shelter Effects
- With shelter: Rest effects normal
- Without shelter: Long rest recovery halved, fatigue+1
