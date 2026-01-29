# SOCIAL_INVESTIGATION.md — Social and Investigation Rules

> **Purpose**: Social checks, investigation actions, insight judgments
> **When to Retrieve**: When social interaction or investigation needed
> **tags**: [social, investigation, persuasion, deception, insight]

---

## SOCIAL::Checks Social Checks

### Base Formula
```
1d20 + modifier vs target DC
```

### Modifier Sources

| Factor | Modifier |
|--------|----------|
| Charisma base | +0~+3 |
| Disguise identity bonus | +1~+3 |
| Bribe/gift | +2~+5 |
| Knowledge advantage | +1~+3 |
| Disadvantage (time pressure, etc.) | -1~-3 |

---

## SOCIAL::Types Social Types

### Persuasion
- Use for: Request help, provide reasonable arguments, negotiate
- Base DC: 10 (easy) ~20 (difficult)

### Deception
- Use for: Lie, disguise identity, mislead
- Base DC: 12 (simple lie) ~18 (complex lie)
- Target may make "Insight" check

### Intimidation
- Use for: Threaten, pressure, interrogate
- Base DC: 12 (timid target) ~20 (tough guy)
- Failure may cause hostility

### Performance
- Use for: Attract attention, speech, impersonate specific identity
- Base DC: 10 (ordinary) ~25 (expert)

---

## SOCIAL::Insight Insight Check

### Target DC
```
DC = 8 + target "Insight" skill + level/experience modifier
```

### Insight Timing
- After player lies
- NPC suspects player intent
- Dialogue involving important secrets

### Insight Results

| Gap | Result |
|-----|--------|
| ≥10 | Completely see through |
| 5-9 | Suspicious, further questioning |
| 0-4 | No obvious suspicion |
| <0 | Believe player (even when lying) |

---

## INVESTIGATION::Observation Observation (Perception)

| Action | DC | Time |
|--------|-----|------|
| Scan room | 10 | 1 round |
| Careful search | 15 | 1 minute |
| Detailed examination | 20 | 10 minutes |
| Look for hidden door/secret compartment | 25 | 30 minutes+ |

---

## INVESTIGATION::Search Search (Investigation)

| Action | DC | Time |
|--------|-----|------|
| Track footprints | 12 | Variable |
| Analyze documents | 14 | 5 minutes |
| Decode cipher | 18 | 15 minutes |
| Restore burned documents | 22 | 30 minutes+ |

---

## INVESTIGATION::Time Time Pressure

| Situation | Time Pressure |
|-----------|---------------|
| Witness about to leave | -2 Insight DC, must be quick |
| Evidence may be destroyed | Search DC+2 |
| Must complete before curfew | Time limit clear |
| NPC has other urgent matters | Reduce social time |

---

## INVESTIGATION::Risk Social Risk

| Action | Risk |
|--------|------|
| Lie in public | Heard, Rumor+1 |
| Threat NPC with background | May be retaliated, Heat+1 |
| Disguise identity exposed | May be arrested, Heat+2 |
| Bribery exposed | Wanted risk |

---

## INTERROGATION::Rules Interrogation Rules

### Target Will Check

| Target | Base DC |
|--------|---------|
| Ordinary person | 10 |
| Trained soldier | 15 |
| Will-strong person | 20 |
| Fanatic | Cannot interrogate |

### Interrogation Methods

| Method | Modifier | Risk |
|--------|----------|------|
| Physical threat | +2 | Heat+1 |
| Monetary temptation | +2 | Need to pay |
| Deception | +1 | Fail if exposed |
| Psychological pressure | +1 | Time+ |

### Consequences
- Success: Gain information
- Failure: Target silent or lying
- Severe failure: Target resists or dies

