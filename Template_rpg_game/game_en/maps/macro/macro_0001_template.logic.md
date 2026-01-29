# macro_0001_template — Template Region Map Logic

version: 0.1.0
updated: 2026-01-29

---

## Movement Logic

### Hex Travel
- Each hex represents 6 miles
- Standard movement: 1 hex per day (6 miles/day)
- Roads: 1.25 hexes per day
- Difficult terrain: 0.5 hexes per day

### Travel Calculations
```
Days = (Distance × Terrain Modifier) ÷ Speed
```

### Navigation
- Check: Survival (Wisdom)
- DC: 10 for familiar territory, 15 for unfamiliar, 20+ for trackless

### Getting Lost
- Failed navigation check by 5+: Wrong direction, lose 1 hour
- Failed navigation check by 10+: Significantly lost, lose half day

---

## Encounter Logic

### Encounter Trigger
- Roll: d100 at end of each travel period
- Base chance: 15%

### Encounter Modifiers
| Condition | Modifier |
|-----------|----------|
| Near settlement | -10% |
| Main road | -10% |
| Wilderness | +5% |
| Known dangerous area | +15% |

### Encounter Type Determination
| Roll | Type |
|------|------|
| 01-40 | Random encounter |
| 41-70 | Social encounter |
| 71-85 | Environmental |
| 86-100 | Nothing |

---

## Fog of War

### Visibility
- Explored hexes: Full visibility
- Adjacent to explored: Partial visibility
- Beyond: Hidden

### Exploration
- Mark hex as explored when:
  - Player explicitly explores
  - Travel through hex
  - Clear line of sight from height

---

## Resource Gathering

### Foraging
- Check: Survival (Wisdom)
- DC: 10 for abundant, 15 for normal, 20 for scarce
- Time: 1 hour per attempt

### Hunting
- Check: Survival (Wisdom) or Stealth
- DC: Based on prey
- Time: 2-4 hours

### Mining
- Check: Athletics or appropriate skill
- DC: Based on resource
- Time: Full day

---

## Plot Trigger Zones

### Zone Rules
- Certain hexes have plot triggers
- Triggers activate when entering hex
- Multiple entries may have different results

### Trigger Examples
| Hex | Trigger | Result |
|-----|---------|--------|
| 0000 | First entry | Plot hook 1 |
| 0005 | Any entry | Random event |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 0.1.0 | 2026-01-29 | Initial template |
