# PIPELINE.md — Novel Writing Pipeline

> **Purpose**: Session→novel conversion rules and process
> **tags**: [writing, pipeline, fiction, novel, workflow]

---

## PIPELINE::001 Core Principles

### Derived Nature
- Writing is Event's **derived layer**, not Canon
- Novel **never produces settings**, can only reference Event/State
- Novel **must align with session records**, cannot add Canon facts

### Truth Priority
```
State > Event > Canon > Writing
```

When novel description conflicts with State/Event, State/Event is standard, novel needs correction.

---

## PIPELINE::002 Writing Trigger Conditions

### Auto-Trigger
After each session ends, Decisions marked `→ Needs novel writing` automatically enter writing queue.

### Manual Trigger
- Player says "write novel" / "continue novel"
- Author says "check novel consistency"

---

## PIPELINE::003 Pre-Writing Checklist

1. Read `Fiction_index.md` (novel progress index)
2. Read recent relevant `sessions/session_*.md` (Decision records)
3. Read `index.md` (current state)
4. Read relevant NPC/location entries (if needed)

**Prohibit**: Read entire System/random tables

---

## PIPELINE::004 Writing Standards

### Perspective
- Clemond as main perspective (third-person limited)
- Can alternate other character perspectives (non-main)

### Style
- Publication-level Western fantasy/serious historical popular literature
- Strong visual imagery, natural dialogue, atmosphere building
- Inner voices trigger naturally

### Sync Requirements
- Stay synchronized with `index.md` state
- Consistent with session decisions
- Mark major turning points with `★` in `Fiction_index.md`

---

## PIPELINE::005 Writing Process

### Step 1: Gather Materials
- Extract Decisions marked `→ Needs novel writing` from session records
- Arrange in chronological order
- Identify key scenes and turning points

### Step 2: Plan Structure
- Determine chapter division
- Assign materials to each chapter
- Mark scenes needing expansion

### Step 3: Write Main Text
- Write by chapters
- Use inner dialogue system
- Maintain narrative consistency

### Step 4: Quality Check
- [ ] Main character perspective unified?
- [ ] Plot consistent with session records?
- [ ] Inner voices trigger naturally?
- [ ] World details accurate?
- [ ] Synchronized with index.md state?

### Step 5: Update Index
- Update `Fiction_index.md` progress
- Mark completed chapters
- Add pending content

---

## PIPELINE::006 File Naming Convention

```
/Writing/
├── Fiction_index.md          # Novel total index (required read)
├── Fiction_par1.md           # Part 1 (currently in progress)
├── Fiction_par2.md           # Part 2
├── Fiction_par3.md           # Part 3
└── CONTINUITY_ISSUES.md      # Consistency issue record (optional)
```

---

## PIPELINE::007 Conflict Handling

### When Conflicts Found
1. Record conflict in `CONTINUITY_ISSUES.md`
2. Mark conflict type:
   - State conflict (inconsistent state)
   - Event conflict (doesn't match session records)
   - Canon conflict (contradicts world setting)

### Resolve Conflicts
- Correct novel based on State/Event
- Record solution
- Mark as resolved

### Example
```markdown
# CONTINUITY_ISSUES.md

## Pending Resolution

| Date | Conflict | Type | Status |
|------|----------|------|--------|
| 2026-01-29 | Chapter 4 ending Marcus appearance doesn't match session record | Event | Pending Correction |

## Resolved
(None)
```

---

## PIPELINE::008 Index Sync Rules

### Fiction_index.md Must Include
- Novel overview (parts, status, word count)
- Core setting quick reference
- Completed chapter list
- Pending writing list
- Key turning point markers

### Update Timing
- Immediately update index when writing new content
- Must reference Fiction_index before each session

---

## PIPELINE::009 Prohibited Items

1. **Prohibit** adding Canon facts in novel
2. **Prohibit** changing NPC character baseline (see `engine/mechanics/NPC_GUIDELINES.md` and NPC files)
3. **Prohibit** modifying indicator values or rules
4. **Prohibit** introducing settings not appearing in sessions
5. **Prohibit** letting Writing serve as rule source

---

## PIPELINE::010 Example Flow

### Input (Session Record)
```markdown
## Decision: Explore Quarry
- Player input: `{Check the gloves on the ground}`
- Resolution: Discover Fehm Court gloves, balance symbol
→ Needs novel writing
```

### Output (Novel Paragraph)
```markdown
Clemond crouched down and picked up the discarded glove. The leather was worn, but the balance symbol on the cuff remained clearly visible—the emblem of the Fehm Court.

His fingers trembled slightly. Not from fear, but from anger.
```

### Update (Fiction_index.md)
```markdown
| Chapter 5 | Shadows of the Quarry | Discovered Fehm Court traces | 🔄 In Progress |
```
