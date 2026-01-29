# TRACKERS.md (Template)
Version: v1.1
Last Updated: 2026-01-29

> **Note**: This file is "manual recording/printing template".
> **Current Ground Truth**: Please use `STATE_PANEL.md` (player side) and `lore/WORLD_STATE.md` (backend) as authority; don't maintain "current values" here.

---

## Flux Indicator Tracking

### Grace (Divine Order Availability)

```
0  1  2  3  4  5  6  7  8  9  10
|  |  |  |  |  |  |  |  |  |  |
                    ↑
                 Current: _
```

- High → Miracles more available
- Low → Prayers silent, sanctuary leaking, uncanny increasing

### Debt (Human Collective Redemption Pressure)

```
0  1  2  3  4  5  6  7  8  9  10
|  |  |  |  |  |  |  |  |  |  |
                ↑
             Current: _
```

- High → Monsters/plagues/temptations increase, society more violent

### Rumor (Public Discussion Level)

```
0  1  2  3
|  |  |  |
        ↑
     Current: _
```

- ≥2 → Must attract investigation forces

### Heat (Power Institution Attention)

```
0  1  2  3
|  |  |  |
        ↑
     Current: _
```

---

## Economic Indicator Tracking

### PI (Price Index)

```
1  2  3  4  5
|  |  |  |  |
        ↑
     Current: _
```

### RP (Risk Premium)

```
0  1  2  3
|  |  |  |
    ↑
 Current: _
```

### Credit

```
-2  -1  0  +1  +2
 |   |  |   |   |
        ↑
     Current: _
```

---

## Street Indicator Tracking

| Indicator | Track | Current Value |
|-----------|-------|---------------|
| ViceMarket | [░░░░░░░░░░] | 1/3 |
| Violence | [░░░░░░░░░░] | 1/3 |
| PlaguePressure | [░░░░░░░░░░] | 1/3 |
| ScapegoatRisk | [░░░░░░░░░░] | 1/3 |
| CultActivity | [░░░░░░░░░░] | 1/3 |

---

## Diplomacy Clock Tracking

| Clock | Progress | Note |
|-------|----------|------|
| French Border Pressure | [░░░░░░] 2/6 | |
| Imperial Aid Hollowing | [░░░░░░] 2/6 | |
| Burgundy Infiltration | [░░░░░░] 2/6 | |
| Church Trial Gravity | [░░░░░░] 1/6 | |
| Trade Cutoff Risk | [░░░░░░] 1/6 | |
| Mist Threshold | [░░░░░░] 0/6 | 1444 Fracture Period |

---

## Player Resource Tracking

### Money
| Type | Quantity | Notes |
|------|----------|-------|
| Gold | - | |
| Silver | - | |
| Change | - | |

### Items
| Item | Use | Notes |
|------|-----|-------|
| - | - | - |

### Allies
| Name | Relationship | Notes |
|------|--------------|-------|
| - | - | - |

### Enemies
| Name | Relationship | Notes |
|------|--------------|-------|
| - | - | - |

---

## Todo

- [ ] If manual tracking needed: Fill "current value" at underscore (don't treat as system ground truth)

