# PIPELINE.md — Novel Writing Pipeline

> **Purpose**: Session-to-Novel conversion rules and workflow
> **tags**: [writing, pipeline, fiction, novel, workflow]

---

## PIPELINE::001 Core Principles

### Derivative Nature
- Writing is an **derivative layer** of Event, not Canon
- Novels **never produce setting**, can only cite Event/State
- Novels **must align with session records**, cannot add Canon facts

### Truth Source Priority
```
State > Event > Canon > Writing
```

When novel description conflicts with State/Event, State/Event prevails; novel needs correction.

---

## PIPELINE::002 Writing Triggers

### Auto-Trigger
After each session, Decisions marked `→ needs novelization` automatically enter the writing queue.

### Manual Trigger
- Player says "write novel" / "continue novel"
- Author says "check novel consistency"

---

## PIPELINE::003 Pre-Writing Checklist

1. Read `Fiction_index.md` (novel progress index)
2. Read recent relevant `sessions/session_*.md` (Decision records)
3. Read `index.md` (current state)
4. Read relevant NPC/location entries (as needed)

**Prohibited**: Reading entire System/random tables

---

## PIPELINE::004 Writing Standards

### Perspective
-克莱蒙德 as main perspective (third-person limited)
- Can alternate other character perspectives (non-primary)

### Style
- Publication-level Western fantasy/serious historical popular literature
- Strong visual imagery, natural dialogue, atmosphere building
- Inner voice triggers naturally

### Sync Requirements
- Stay synchronized with `index.md` status
- Consistent with session decisions
- Major turning points marked with `★` in `Fiction_index.md`

---

## PIPELINE::005 Writing Workflow

### Step 1: Collect Materials
- Extract Decisions marked `→ needs novelization` from session records
- Arrange in chronological order
- Identify key scenes and turning points

### Step 2: Plan Structure
- Determine chapter division
- Assign materials to each chapter
- Mark scenes needing expansion

### Step 3: Write Main Text
- Write by chapter
- Use inner dialogue system
- Maintain narrative consistency

### Step 4: Quality Check
- [ ] Is main perspective unified?
- [ ] Does plot match session records?
- [ ] Is inner voice naturally triggered?
- [ ] Are world-building details accurate?
- [ ] Is it synchronized with index.md?

### Step 5: Update Index
- Update `Fiction_index.md` progress
- Mark completed chapters
- Add pending content

---

## PIPELINE::006 File Naming Convention

```
/Writing/
├── Fiction_index.md          # Novel total index (required read)
├── Fiction_par1.md           # Volume 1 (currently in progress)
├── Fiction_par2.md           # Volume 2
├── Fiction_par3.md           # Volume 3
└── CONTINUITY_ISSUES.md      # Consistency issue record (optional)
```

---

## PIPELINE::007 Conflict Handling

### When Conflict Found
1. Record conflict in `CONTINUITY_ISSUES.md`
2. Mark conflict type:
   - State conflict (status inconsistency)
   - Event conflict (inconsistent with session records)
   - Canon conflict (contradicts world-building)

### Resolve Conflicts
- Correct novel based on State/Event
- Record solution
- Mark as resolved

### Example
```markdown
# CONTININUITY_ISSUES.md

## Pending Resolution

| Date | Conflict | Type | Status |
|------|----------|------|--------|
| 2026-01-29 | Chapter 4 ending Marcus appearance inconsistent with session record | Event | Pending correction |

## Resolved
(None)
```

---

## PIPELINE::008 Index Sync Rules

### Fiction_index.md Must Include
- Novel overview (volume count, status, word count)
- Core setting quick reference
- Completed chapters list
- Pending content list
- Key turning points marked

### Update Timing
- Update index immediately after writing new content
- Must reference Fiction_index before each session

---

## PIPELINE::009 Prohibitions

1. **Prohibited** adding Canon facts in novels
2. **Prohibited** changing NPC fundamental character (see `mechanics/NPC_GUIDELINES.md` and NPC files)
3. **Prohibited** modifying indicator values or rules
4. **Prohibited** introducing settings not appearing in session
5. **Prohibited** using Writing as rule source

---

## PIPELINE::010 Example Flow

### Input (Session Record)
```markdown
## Decision: Explore Quarry
- Player input: `{check the gloves on the ground}`
- Resolution: Found Vehm Court gloves, scale symbol
→ Needs novelization
```

### Output (Novel Paragraph)
```markdown
克莱蒙德 knelt down and picked up the discarded glove. The leather was worn, but the scale symbol on the cuff remained clear — the mark of the Vehm Court.

His fingers trembled slightly. Not from fear. From anger.
```

### Update (Fiction_index.md)
```markdown
| Chapter 5 | Shadows of the Quarry | Discovered Vehm Court traces | 🔄 In Progress |
```

