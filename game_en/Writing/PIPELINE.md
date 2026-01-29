# PIPELINE.md — Novel Writing Pipeline

> **Purpose**: Session-to-novel conversion rules and workflow
> **tags**: [writing, pipeline, fiction, novel, workflow]

---

## PIPELINE::001 Core Principles

### Derived Nature
- Writing is the **derived layer** of Event, not Canon
- Novels **never produce settings**, can only cite Event/State
- Novels **must align with session records**, must not add Canon facts

### Ground Truth Priority
```
State > Event > Canon > Writing
```

When novel description conflicts with State/Event, State/Event prevails; novel needs correction.

---

## PIPELINE::002 Writing Trigger Conditions

### Automatic Trigger
After each session ends, Decisions marked `→ Write to Novel` automatically enter writing queue.

### Manual Trigger
- Player says "write novel" "continue novel"
- Author says "check novel consistency"

---

## PIPELINE::003 Pre-Writing Checklist

1. Read `Fiction_index.md` (novel progress index)
2. Read recent related `sessions/session_*.md` (Decision records)
3. Read `index.md` (current state)
4. Read related NPC/location entries (as needed)

**Prohibited**: Reading entire System/random tables

---

## PIPELINE::004 Writing Standards

### Perspective
- Clermond as main perspective (third-person limited)
- Can intercut other character perspectives (non-main)

### Style
- Publication-level Western fantasy/serious historical popular literature
- Strong visual imagery, natural dialogue, atmospheric ambiance
- Inner voice triggers naturally

### Synchronization Requirements
- Maintain synchronization with `index.md` state
- Consistent with session decisions
- Mark major turning points with `★` in `Fiction_index.md`

---

## PIPELINE::005 Writing Workflow

### Step 1: Gather Materials
- Extract Decisions marked `→ Write to Novel` from session records
- Arrange in chronological order
- Identify key scenes and turning points

### Step 2: Plan Structure
- Determine chapter division
- Allocate materials to chapters
- Mark scenes needing expansion

### Step 3: Write Main Text
- Write by chapters
- Use inner dialogue system
- Maintain narrative consistency

### Step 4: Quality Check
- [ ] Main character perspective unified?
- [ ] Plot consistent with session records?
- [ ] Inner voice naturally triggered?
- [ ] World-building details accurate?
- [ ] Synchronized with index.md state?

### Step 5: Update Index
- Update `Fiction_index.md` progress
- Mark completed chapters
- Add pending content

---

## PIPELINE::006 File Naming Conventions

```
/Writing/
├── Fiction_index.md          # Novel total index (mandatory read)
├── Fiction_par1.md           # Part 1 (currently in progress)
├── Fiction_par2.md           # Part 2
├── Fiction_par3.md           # Part 3
└── CONTINUITY_ISSUES.md      # Consistency issue record (optional)
```

---

## PIPELINE::007 Conflict Handling

### When Conflicts Discovered
1. Record conflict in `CONTINUITY_ISSUES.md`
2. Mark conflict type:
   - State conflict (inconsistent state)
   - Event conflict (inconsistent with session record)
   - Canon conflict (contradicts world-building)

### Resolve Conflicts
- Correct novel based on State/Event
- Record solution
- Mark as resolved

### Example
```markdown
# CONTINUITY_ISSUES.md

## Pending

| Date | Conflict | Type | Status |
|------|----------|------|--------|
| 2026-01-29 | Chapter 4 ending Marcus appearance inconsistent with session record | Event | Pending Correction |

## Resolved
(None)
```

---

## PIPELINE::008 Index Synchronization Rules

### Fiction_index.md Must Include
- Novel overview (parts, status, word count)
- Core setting quick reference
- Completed chapters list
- Pending content list
- Key turning point markers

### Update Timing
- Update index immediately after writing new content
- Must reference Fiction_index before each session round

---

## PIPELINE::009 Prohibitions

1. **Prohibited** adding Canon facts in novels
2. **Prohibited** changing NPC fundamental character (see `mechanics/NPC_GUIDELINES.md` and NPC files)
3. **Prohibited** modifying indicator values or rules
4. **Prohibited** introducing settings not appearing in session
5. **Prohibited** using Writing as rules source

---

## PIPELINE::010 Example Flow

### Input (Session Record)
```markdown
## Decision: Explore the Quarry
- Player input: `{Check the gloves on the ground}`
- Resolution: Discover Fehm Court gloves, scale symbol
→ Write to Novel
```

### Output (Novel Paragraph)
```markdown
Clermond crouched down and picked up the discarded glove. The leather was worn, but the scale symbol on the cuff remained clearly visible — the mark of the Fehm Court.

His fingers trembled slightly. Not from fear, but from anger.
```

### Update (Fiction_index.md)
```markdown
| Chapter 5 | Shadows of the Quarry | Discover Fehm Court Trace | In Progress |
```
