# TRACKERS.md — Trackers (Templates)
Version: v1.1
Last Updated: 2026-01-29

> **Note**: This file is a "manual recording/printing template".
> **Current Source of Truth**: Please use `campaigns/<id>/STATE_PANEL.json` (player side) and `campaigns/<id>/WORLD_STATE.md` (backend) as the standard; do not maintain "current values" here.

---

## Transient Indicator Tracking

### Grace (Divine Order Availability)

```
0  1  2  3  4  5  6  7  8  9  10
|  |  |  |  |  |  |  |  |  |  |
                    ↑
                 Current: _
```

- High → Miracles more obtainable
- Low → Prayers silent, sanctuary leaky, omens increase

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

### Heat (Power Institution Attention Level)

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

| Clock | Progress | Description |
|-------|----------|-------------|
| French border pressure | [░░░░░░] 2/6 | |
| Imperial aid hollowing | [░░░░░░] 2/6 | |
| Burgundy infiltration | [░░░░░░] 2/6 | |
| Church trial gravity | [░░░░░░] 1/6 | |
| Trade cutoff risk | [░░░░░░] 1/6 | |
| Mist threshold | [░░░░░░] 0/6 | 1444 Crack Phase |

---

## Player Resource Tracking

### Money
| Type | Quantity | Notes |
|------|----------|-------|
| Gold coins | - | |
| Silver coins | - | |
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

- [ ] If manual tracking needed: Fill "current value" at underscore (do not treat as system source of truth)
