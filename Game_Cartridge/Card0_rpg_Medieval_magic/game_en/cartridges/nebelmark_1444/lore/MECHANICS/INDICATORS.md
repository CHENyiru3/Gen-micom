# MECHANICS/INDICATORS.md — Global Indicator System

> **Purpose**: Track four global indicators—Grace, Debt, Rumor, Heat
> **When to Retrieve**: Turn settlement, monster trigger, faction intervention
> **tags**: [mechanic, indicator, grace, debt, rumor, heat]
> **related**: [CANON/WORLD.md, MIST/PHENOMENA.md]

---

## IND::001 Four Global Indicators

| Indicator | Range | Meaning | High Value Effect | Low Value Effect |
|-----------|-------|---------|-------------------|------------------|
| **Grace** | 0-10 | Divine order availability | Blessing effective, sanctuary solid, healing +1 | Prayer silent, relics partially失效, anomalies frequent |
| **Debt** | 0-10 | Collective redemption pressure | Monsters/dream plagues/temptations increase; society more violent | Relatively calm, mist recedes |
| **Rumor** | 0-3 | City's discussion level of weirdness/spellcasting | Investigation forces must intervene | Weirdness can hide |
| **Heat** | 0-3 | Watch/Church/Judge/Vehm Court attention | Direct intervention, pursuit, trial | Free action space |

---

## IND::002 Indicator Core Rules

### 2.1 Indicator Interaction Rules

```
 Debt+1 / Heat+1 ← Quick-path violence/magic abuse to solve key problems
 Debt-1 / Grace+1 ← Bear cost to save people/refuse temptation/protect innocent
 Rumor≥2 ← Must attract certain investigation/trial force intervention
```

### 2.2 Grace Threshold Effects

| Grace Value | Effect |
|-------------|--------|
| 8-10 | Blessing effective+1, sanctuary solid, healing spells+1 |
| 5-7 | Normal sanctuary protection, healing spells normal |
| 3-4 | Sanctuary may "leak," healing spells-1 |
| 1-2 | Prayer often unanswered, relics partially ineffective |
| 0 | Grace severed, weirdness can invade any sanctuary |

### 2.3 Debt Threshold Effects

| Debt Value | Effect |
|------------|--------|
| 8-10 | High dream plague frequency, monster spawn+2, street violence surges |
| 5-7 | Medium monster spawn, temptations increase |
| 3-4 | Light monster spawn, occasional temptation |
| 1-2 | Relatively calm, mist recedes |
| 0 | Mist field weakest, weirdness barely appears |

### 2.4 Rumor Threshold Effects

| Rumor Value | Effect |
|-------------|--------|
| 3 | Citywide knowledge, investigation forces must intervene, multiple factions watching |
| 2 | District spreading, investigation forces may intervene |
| 1 | Limited whispers, needs specific trigger to escalate |
| 0 | No discussion, weirdness can hide |

### 2.5 Heat Threshold Effects

| Heat Value | Effect |
|------------|--------|
| 3 | Being pursued, specified forces intervene, possible ambush/surround |
| 2 | Marked, investigators actively search |
| 1 | Noticed, specific factions verify identity |
| 0 | No attention, free action |

---

## IND::003 Indicator Change Trigger Table

### 3.1 Grace Changes

| Action | Grace Change |
|--------|--------------|
| Participate in orthodox rituals, donate to monastery | +1 |
| Successfully use holy relic/blessed item | +1 (per item) |
| Witness orthodox miracle | +1 (per scene) |
| Protect innocent in sanctuary | +1 |
| **Grace Decline**: | |
| Desecrate sanctuary, damage holy relic | -2~-4 |
| Refuse to help believer | -1~-2 |
| Use contaminated "divine magic" | -3 |

### 3.2 Debt Changes

| Action | Debt Change |
|--------|-------------|
| **Debt Increase**: | |
| Kill innocent without justification | +2 |
| Torture prisoner, cast cruel punishment | +2 |
| Use dark magic/summon extraplanar being | +1~+3 |
| Make deal with weirdness | +2 |
| Abandon ally, refuse to help | +1 |
| **Debt Decrease**: | |
| Sacrifice self to save others | -2 |
| Refuse temptation, hold principles | -1 |
| Avenge innocent | -1 |
| Expose heresy/monster truth | -1 |

### 3.3 Rumor Changes

| Action | Rumor Change |
|--------|--------------|
| Cast spells publicly/monster sighting (seen by many) | +1 |
| Street fight, violence | +1 |
| Brag about adventures in tavern | +1 |
| Seen by watch/monastery contacting suspicious person | +1 |
| **Rumor Control**: | |
| Destroy evidence, silence witnesses | -1 |
| Official debunking/plausible explanation | -1 |
| Frame someone else | -1 |

### 3.4 Heat Changes

| Action | Heat Change |
|--------|-------------|
| **Heat Increase**: | |
| Seen at crime scene | +1 |
| Reported/denounced by NPC | +1~+2 |
| Possess contraband/wanted items | +1 |
| Kill watch/monk/official | +2 |
| Trigger Rumor multiple times | +1 |
| **Heat Decrease**: | |
| Hide waiting for storm to pass | -1 (per turn) |
| Bribe successfully | -2 |
| Expose more important enemy | -1 |
| Gain faction protection | -2 |

---

## IND::004 Faction Intervention Thresholds

| Trigger Condition | Intervention Faction | Intervention Method |
|-------------------|---------------------|---------------------|
| Rumor≥2 + Heat≥1 | Watch/City Militia | Patrol strengthening, curfew, investigation |
| Rumor≥2 + Spellcasting related | Monastery Investigators | Secret investigation, summons, trial |
| Rumor≥2 + Monster sighting | Vehm Court | Secret execution, pollution clearing |
| Heat≥2 + Noble related | Empire/France Factions | Diplomatic pressure, wanted posters |
| Debt≥7 + Grace≤3 | Multiple weird events | Church purification extreme measures |
| Rumor=3 + Heat=3 | Multiple factions intervene | Complex conflict, campaign-level events |

---

## IND::005 Indicator and Monster Intensity

| Indicator Combination | Expected Monster Intensity |
|----------------------|---------------------------|
| Grace≥7, Debt≤3, Rumor≤1 | Low monster spawn rate, occasional minor anomalies |
| Grace4-6, Debt4-6 | Medium monster spawn rate, repeatable anomalous locations |
| Grace≤3, Debt≥7, Rumor≥2 | High monster spawn rate, dungeon-level events |
| Grace≤2, Debt≥8, Rumor=3 | Threshold crossing events, regional monster outbreak |

---

## IND::006 Turn Settlement Template

```yaml
## Turn Indicator Settlement
Grace: X  # Divine order availability
Debt: Y   # Human redemption pressure
Rumor: Z  # Public discussion level
Heat: W   # Faction attention level

## Turn Changes
- Grace: [+/-] (reason)
- Debt: [+/-] (reason)
- Rumor: [+/-] (reason)
- Heat: [+/-] (reason)

## Next Turn Expectations
- Monster spawn rate: [low/medium/high]
- Possible intervention factions: [list]
- Suggested focus points: [list]
```

---

## IND::007 Quick Reference Table

### Indicator Quick Reference

| Indicator | Range | Key Threshold | Core Meaning |
|-----------|-------|---------------|--------------|
| Grace | 0-10 | 5 (normal), 3 (danger), 0 (severed) | Divine power availability |
| Debt | 0-10 | 5 (balanced), 7 (high risk), 10 (critical) | Redemption pressure and weird attraction |
| Rumor | 0-3 | 2 (intervention line), 3 (crisis) | Public attention and exposure risk |
| Heat | 0-3 | 2 (investigation line), 3 (pursuit) | Faction attention and intervention risk |

### Indicator Change Mnemonic

```
Spellcasting/Monster sighting → Rumor+1
Violence/Magic abuse → Debt+1 or Heat+1
Save people/Refuse temptation → Debt-1 or Grace+1
Rumor≥2 → Investigation forces must intervene
```

---

*MECHANICS/INDICATORS.md v1.0 - Chronicles of the Misty Border*
