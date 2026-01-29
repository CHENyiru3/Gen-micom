---
name: rpg-dm-governance-panel
description: Maintain the governance panel (territory, followers, army, income, governance clocks) for territory management gameplay.
---

# RPG DM Governance Panel

Use this skill when players engage in territory management, governance, or faction gameplay.

## Governance Panel Structure

The governance panel tracks:
- **Territory**: Controlled areas and settlements
- **Followers**: Loyal NPCs and their roles
- **Army**: Military forces and their status
- **Income**: Resources and revenue streams
- **Governance Clocks**: Time-based developments

## File Location

`GOVERNANCE_PANEL.md` in campaign root or `campaigns/<id>/root/`

## Data Structure

```yaml
territory:
  - id: "terr_001"
    name: "[Region Name]"
    type: [rural/urban/frontier]
    control: [full/partial/contested]
    population: [number]
    loyalty: [1-10]

followers:
  - id: "fol_001"
    name: "[Name]"
    role: [role]
    loyalty: [1-10]
    skills: []
    location: [terr_xxx]

army:
  - id: "army_001"
    name: "[Unit Name]"
    type: [infantry/cavalry/archer/etc.]
    size: [number]
    morale: [1-10]
    location: [terr_xxx]
    status: [ready/deployed/training]

income:
  - source: "[Source]"
    type: [tax/trade/resource]
    amount: [number]
    frequency: [daily/weekly/monthly]
    stability: [1-10]

clocks:
  - id: "clk_001"
    name: "[Clock Name]"
    total: [total]
    filled: [current]
    trigger: "[Event when filled]"
```

## Governance Actions

### Territory Management
- Claim territory: Control check (DC based on resistance)
- Develop territory: Resource investment
- Defend territory: Army positioning

### Follower Management
- Recruit followers: Social check or quest reward
- Assign roles: Based on skills
- Increase loyalty: Quest rewards, fair treatment

### Army Management
- Recruit soldiers: Cost + time
- Train army: Skill check
- Deploy army: Strategic decision
- Pay soldiers: Income deduction

### Income Management
- Collect taxes: Governance check
- Trade deals: Negotiation + time
- Resource extraction: Skill checks

## Governance Clocks

### Clock Types
- **Threat Clocks**: Countdown to danger
- **Development Clocks**: Countdown to improvements
- **Event Clocks**: Countdown to events
- **Relationship Clocks**: Countdown to relationship changes

### Clock Mechanics
- Each tick: Fill one segment
- Advance clock: Based on in-game events
- Trigger: When clock is full

## Quality Checklist

- [ ] All sections are populated
- [ ] Numbers are consistent
- [ ] Relationships are tracked
- [ ] Changes are documented
- [ ] Player actions affect panel state
