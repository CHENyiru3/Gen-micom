# Location Index

> **Purpose**: Index of all locations in the game

---

## Locations

| Location ID | Name | Type | Region | Status |
|-------------|------|------|--------|--------|
| loc_0001 | [Location Name] | [Type] | [Region] | Active |

---

## Location Template

```markdown
## loc_XXX:
- **Name**:
- **Type**: [City/Town/Village/Dungeon/Ruin/etc.]
- **Region**: [Region ID]
- **Description**:
- **Points of Interest**:
- **NPCs**:
- **Connections**:
- **Secrets**:
```

---

## Creating New Locations

1. Create file in `locations/` directory
2. Use naming convention: `loc_[number]_[name].md`
3. Add entry to this index
4. Update `OBJECT_INDEX.md` when activated
