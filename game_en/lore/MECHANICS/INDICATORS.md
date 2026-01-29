# MECHANICS/INDICATORS.md — Global Indicator System

> **Purpose**: Track four global indicators: Grace, Debt, Rumor, Heat
> **When to Retrieve**: Per-turn settlement, uncanny triggering, faction intervention
> **tags**: [mechanic, indicator, grace, debt, rumor, heat]
> **related**: [CANON/WORLD.md, MIST/PHENOMENA.md]

---

## IND::001 Four Global Indicators

| Indicator | Range | Meaning | High Value Effect | Low Value Effect |
|-----------|-------|---------|-------------------|------------------|
| **Grace** | 0-10 | Divine order availability | Blessings effective, sanctuary solid | Prayers silent, holy items失效, uncanny frequent |
| **Debt** | 0-10 | Collective redemption pressure | Monsters/dream plagues/temptations increase; society more violent | Relatively calm, Mist recedes |
| **Rumor** | 0-3 | City's discussion level of uncanny/spellcasting | Investigation forces must intervene | Uncanny can hide |
| **Heat** | 0-3 | City watch/monastery/inquisitor/Fehm Court attention | Direct intervention, pursuit, trial | Free action space |

---

## IND::002 Indicator Core Rules

### 2.1 Indicator Interaction Rules

```
 Debt+1 / Heat+1 ← Shortcut violence/magic abuse to solve key problems
 Debt-1 / Grace+1 ← Pay cost to save people/refuse temptation/protect innocents
 Rumor≥2 ← Must attract certain investigation/trial force intervention
```

### 2.2 Grace Threshold Effects

| Grace Value | Effect |
|-------------|--------|
| 8-10 | Blessing effective+1, sanctuary solid, healing spells+1 |
| 5-7 | Normal sanctuary protection, healing spells normal |
| 3-4 | Sanctuary may "leak", healing spells-1 |
| 1-2 | Prayers often unanswered, holy items partially ineffective |
| 0 | Grace cut off, uncanny can invade any sanctuary |

### 2.3 Debt Threshold Effects

| Debt Value | Effect |
|------------|--------|
| 8-10 | High dream plague occurrence, monster spawn+2, street violence surge |
| 5-7 | Medium monster spawn, temptation increases |
| 3-4 | Light monster spawn, occasional temptation |
| 1-2 | Relatively calm, Mist recedes |
| 0 | Mist field weakest, uncanny almost never appears |

### 2.4 Rumor Threshold Effects

| Rumor Value | Effect |
|-------------|--------|
| 3 | City-wide known, investigation forces must intervene, multiple factions attention |
| 2 | District spreading, investigation forces may intervene |
| 1 | Small circle whispers, needs specific trigger to escalate |
| 0 | No discussion, uncanny can hide |

### 2.5 Heat Threshold Effects

| Heat Value | Effect |
|------------|--------|
| 3 | Under pursuit, designated forces intervene, possible ambush/surround |
| 2 | Marked, investigators actively searching |
| 1 | Noticed, specific factions will verify identity |
| 0 | No attention, free action |

---

## IND::003 Indicator Change Trigger Table

### 3.1 Grace Changes

| Action | Grace Change |
|--------|--------------|
| Participate in orthodox rituals, donate to monastery | +1 |
| Successfully use holy items/blessed items | +1 (per item) |
| Witness orthodox miracle | +1 (per scene) |
| Protect innocents within sanctuary | +1 |
| **Grace Decrease**: | |
| Desecrate sanctuary, damage holy items | -2~-4 |
| Refuse to help believers | -1~-2 |
| Use contaminated "divine spells" | -3 |

### 3.2 Debt Changes

| Action | Debt Change |
|--------|-------------|
| **Debt Increase**: | |
| Kill innocents (no justification) | +2 |
| Torture prisoners, inflict cruel punishment | +2 |
| Use dark magic/summon extraplanar beings | +1~+3 |
| Make deals with uncanny | +2 |
| Abandon allies, watch them die | +1 |
| **Debt Decrease**: | |
| Sacrifice self to save others | -2 |
| Refuse temptation, hold principles | -1 |
| Avenge innocents | -1 |
| Expose truth of heresy/monster | -1 |

### 3.3 Rumor Changes

| Action | Rumor Change |
|--------|--------------|
| Publicly cast spells/use magic | +1 |
| Monster sighting (seen by many) | +1~+2 |
| Street fights, violent incidents | +1 |
| Boast about adventures in tavern | +1 |
| Seen by city watch/monastery contacting suspicious persons | +1 |
| **Rumor Control**: | |
| Destroy evidence, silence witnesses | -1 |
| Official debunking/reasonable explanation | -1 |
| Frame others | -1 |

### 3.4 Heat Changes

| Action | Heat Change |
|--------|-------------|
| **Heat Increase**: | |
| Witnessed at crime scene | +1 |
| NPC report/denunciation | +1~+2 |
| Possess prohibited/wanted items | +1 |
| Kill city watch/monk/official | +2 |
| Trigger Rumor multiple times | +1 |
| **Heat Decrease**: | |
| Hide, wait for things to blow over | -1 (per turn) |
| Successful bribery | -2 |
| Expose more important enemy | -1 |
| Gain faction protection | -2 |

---

## IND::004 Faction Intervention Thresholds

| Trigger Condition | Intervening Faction | Intervention Method |
|-------------------|---------------------|---------------------|
| Rumor≥2 + Heat≥1 | City watch/City militia | Patrol intensification, curfew, investigation |
| Rumor≥2 + Spellcasting related | Monastery investigators | Secret investigation, summons, trial |
| Rumor≥2 + Monster sighting | Fehm Court | Secret execution, pollution cleansing |
| Heat≥2 + Noble related | Imperial/French forces | Diplomatic pressure, wanted notices |
| Debt≥7 + Grace≤3 | Multiple uncanny events | Church purification extreme measures |
| Rumor=3 + Heat=3 | Multiple factions intervene | Complex conflict, campaign-level event |

---

## IND::005 Indicator and Uncanny Intensity

| Indicator Combination | Expected Uncanny Intensity |
|-----------------------|----------------------------|
| Grace≥7, Debt≤3, Rumor≤1 | Low uncanny spawn rate, occasional minor anomalies |
| Grace4-6, Debt4-6 | Medium uncanny spawn rate, repeatable anomaly locations |
| Grace≤3, Debt≥7, Rumor≥2 | High uncanny spawn rate, dungeon-level events |
| Grace≤2, Debt≥8, Rumor=3 | Threshold crossing event, regional uncanny outbreak |

---

## IND::006 Turn Settlement Template

```yaml
## Turn Indicator Settlement
Grace: X  # Divine order availability
Debt: Y   # Human redemption pressure
Rumor: Z  # Public discussion level
Heat: W   # Faction attention

## Turn Changes
- Grace: [+/-] (reason)
- Debt: [+/-] (reason)
- Rumor: [+/-] (reason)
- Heat: [+/-] (reason)

## Next Turn Expectation
- Uncanny spawn rate: [Low/Medium/High]
- Possible intervening factions: [list]
- Suggested focus points: [list]
```

---

## IND::007 Quick Reference Table

### Indicator Quick Reference

| Indicator | Range | Key Threshold | Core Meaning |
|-----------|-------|---------------|--------------|
| Grace | 0-10 | 5 (normal), 3 (danger), 0 (cut off) | Divine power availability |
| Debt | 0-10 | 5 (balanced), 7 (high risk), 10 (critical) | Redemption pressure and uncanny attraction |
| Rumor | 0-3 | 2 (intervention line), 3 (crisis) | Public attention and exposure risk |
| Heat | 0-3 | 2 (investigation line), 3 (pursuit) | Faction attention and intervention risk |

### Indicator Change Mnemonic

```
Spellcasting/monster sighting → Rumor+1
Violence/magic abuse → Debt+1 or Heat+1
Saving people/refusing temptation → Debt-1 or Grace+1
Rumor≥2 → Investigation forces must intervene
```

---

*MECHANICS/INDICATORS.md v1.0 - Chronicle of the Mist Frontier*
