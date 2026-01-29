# micro_0001_template — Template Location Map Logic

version: 0.1.0
updated: 2026-01-29

---

## Movement Logic

### Node Travel
- Movement between nodes takes time based on:
  - Distance between nodes
  - Terrain type
  - Hazards present

### Movement Speed
| Speed | Time per Node |
|-------|---------------|
| Cautious | 10 minutes |
| Normal | 5 minutes |
| Hurried | 2 minutes |

### Difficult Terrain
- Difficult terrain doubles travel time
- Examples: rubble, water, dense vegetation

---

## Combat Rules

### Initiative
- Roll initiative when combat starts
- Use standard combat rules from `mechanics/COMBAT.md`

### Positioning
- Characters in same node can engage
- Characters in adjacent nodes can support
- Line of sight as described in node details

### Retreat
- Retreat to adjacent node: Bonus action
- During combat: Disengage required

---

## Exploration Rules

### Perception
- Passive Perception used by default
- Active Perception (Investigation): DC based on hidden elements

### Hidden Elements
| Element | DC | Notes |
|---------|-----|-------|
| Secret door | 15 | May have visual clues |
| Trap | 15-20 | Based on trap type |
| Hidden NPC | 18 | NPC is hiding |
| Clue | 12 | Depends on subtlety |

### Light
| Light Source | Bright | Dim |
|--------------|--------|-----|
| Torch | 20 ft | 20 ft |
| Candle | 5 ft | 5 ft |
| Darkvision | 60 ft | - |

---

## Encounter Logic

### Random Encounters
- Check: d6 every 3 nodes explored
- Roll ≥ 4: Encounter occurs

### Encounter Types
| Roll | Type |
|------|------|
| 1-2 | Monster |
| 3-4 | Hazard |
| 5-6 | Nothing |

### Hostile NPCs
- Hostile NPCs may be encountered in nodes
- Roll for surprise if applicable
- Use NPC stats from data file

---

## Trap Logic

### Triggering Traps
- Triggered by:
  - Walking into area
  - Touching object
  - Specific action

### Trap Saves
- Dexterity save to avoid
- DC based on trap type

### Disarming Traps
- Thieves' tools or appropriate skill
- DC = Trap DC + 5

---

## Secret Discovery

### Finding Secrets
- Investigation check
- DC varies by secret complexity
- May require specific actions

### Secret Types
| Type | DC | Method |
|------|-----|--------|
| Hidden door | 15 | Search or notice |
| Hidden message | 12 | Read carefully |
| Concealed item | 18 | Careful search |
| Plot secret | 20 | Research + investigation |

---

## Loot Distribution

### Treasure Placement
- Treasure in designated nodes
- May be hidden, guarded, or trapped

### Splitting Loot
- Players decide among themselves
- DM arbitrates disputes

### Magic Items
- Identified automatically
- Cursed items: Wisdom save to identify

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 0.1.0 | 2026-01-29 | Initial template |
