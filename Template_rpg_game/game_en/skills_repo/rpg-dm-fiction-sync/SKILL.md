---
name: rpg-dm-fiction-sync
description: Synchronize session play records into polished fiction/novel format without producing new Canon (world settings).
---

# RPG DM Fiction Sync

Use this skill when you need to convert session records into polished fiction/novel format.

## What This Skill Does

1. Reads session records from `sessions/session_*.md`
2. Transforms gameplay into narrative prose
3. Maintains continuity with existing fiction
4. Produces `Writing/Fiction_par*.md` files

## What This Skill Does NOT Do

- Create new world settings (use content authoring skill)
- Change established Canon
- Invent new facts about the world
- Resolve plot threads (leave to gameplay)

## Fiction Writing Guidelines

### Style Requirements
- **Tense**: Past tense (standard narrative)
- **POV**: Third person, omniscient narrator
- **Tone**: Match the game's established tone
- **Focus**: Player character actions and consequences

### Structure
- Opening: Set scene (2-4 sentences)
- Body: Key events in chronological order
- Closing: End at natural pause point

### Voice
- Descriptive but not purple prose
- Action-driven narrative
- Show emotions through behavior
- Balance description and action

## Process

1. Read session records (decisions, player input, DM narration)
2. Identify key moments to highlight
3. Write prose version of events
4. Check against session record for accuracy
5. Add to `Writing/Fiction_par*.md`

## Output Format

```markdown
# Fiction_par[N].md — [Session Title]

> **Session**: session_YYYY-MM-DD_slug.md
> **Date**: YYYY-MM-DD
> **Word Count**: X words

---

## Opening

[Narrative description]

## Key Events

### Event 1
[Narrative]

### Event 2
[Narrative]

### Event 3
[Narrative]

## Resolution

[Narrative ending]

## Character Development

- [PC Name]: [Development note]
```

## Quality Checklist

- [ ] Events match session record
- [ ] Prose flows naturally
- [ ] Tone is consistent
- [ ] No new Canon introduced
- [ ] Character voices are distinct
- [ ] Scene descriptions are vivid but concise
