# SOCIAL_INVESTIGATION.md — Social and Investigation Rules

> **Purpose**: Social checks, investigation actions, insight judgment
> **When to Retrieve**: When social interaction or investigation needed
> **tags**: [social, investigation, persuasion, deception, insight]

---

## SOCIAL::checks Social Checks

### Basic Formula
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

## SOCIAL::types Social Types

### Persuasion
- Used for: Request help, provide reasonable arguments, negotiate
- DC base: 10 (easy)~20 (hard)

### Deception
- Used for: Lying, disguising identity, misleading
- DC base: 12 (simple lie)~18 (complex lie)
- Target may perform "Insight" check

### Intimidation
- Used for: Threaten, pressure, interrogate
- DC base: 12 (timid target)~20 (tough guy)
- Failure may cause hostility

### Performance
- Used for: Attract attention, speech, disguise as specific identity
- DC base: 10 (ordinary)~25 (expert)

---

## SOCIAL::insight Insight Check

### Target DC
```
DC = 8 + target "Insight" skill + level/experience modifier
```

### Insight Timing
- After player lies
- NPC suspects player intent
- Conversation involves important secret

### Insight Results

| Gap | Result |
|-----|--------|
| ≥10 | Completely see through |
| 5-9 | Suspicious, further questioning |
| 0-4 | No obvious suspicion |
| <0 | Believe player (even when lying) |

---

## INVESTIGATION::observation Observation (Perception)

| Action | DC | Time |
|--------|-----|------|
| Glance at room | 10 | 1 round |
| Search carefully | 15 | 1 minute |
| Detailed inspection | 20 | 10 minutes |
| Look for hidden door/secret compartment | 25 | 30 minutes+ |

---

## INVESTIGATION::search Search (Investigation)

| Action | DC | Time |
|--------|-----|------|
| Track footprints | 12 | Variable |
| Analyze documents | 14 | 5 minutes |
| Decipher code | 18 | 15 minutes |
| Restore burned documents | 22 | 30 minutes+ |

---

## INVESTIGATION::time Time Pressure

| Situation | Time Pressure |
|-----------|---------------|
| Witness about to leave | -2 Insight DC, must be quick |
| Evidence may be destroyed | Search DC+2 |
| Must complete before curfew | Clear time limit |
| NPC has other urgent matters | Reduce social time |

---

## INVESTIGATION::risk Social Risk

| Action | Risk |
|--------|------|
| Lying in public | Heard, Rumor+1 |
| Threatening NPC with background | May retaliate, Heat+1 |
| Disguise identity exposed | May be arrested, Heat+2 |
| Bribery exposed | Wanted risk |

---

## INTERROGATION::rules Interrogation Rules

### Target Will Check

| Target | DC Base |
|--------|---------|
| Ordinary person | 10 |
| Trained soldier | 15 |
| Steadfast person | 20 |
| Fanatic | Cannot interrogate |

### Interrogation Methods

| Method | Modifier | Risk |
|--------|----------|------|
| Physical threat | +2 | Heat+1 |
| Monetary temptation | +2 | Need pay |
| Deception | +1 | Failure if exposed |
| Psychological pressure | +1 | Time+ |

### Consequences
- Success: Gain information
- Failure: Target silent or lying
- Serious failure: Target resists or dies
