# RAG_RULES.md — Retrieval Augmented Generation Rules

> **Purpose**: RAG retrieval strategy, gatekeeping, fragment extraction spec
> **When to Retrieve**: When specific rules/data needed
> **tags**: [rag, retrieval, policy, context]

---

## RAG::001 Call Gate Strategy

### Default Strategy
- **Prohibit**: Automatically retrieve `Writing/` directory
- **Prohibit**: Stuff entire tables/paragraphs into context
- **On-demand retrieval**: Each ≤6 fragments, each paragraph ≤120 characters

### Allowed Trigger Retrieval

| Trigger Condition | Retrieval Target | Fragment Limit |
|-------------------|------------------|----------------|
| Need combat adjudication | `mechanics/COMBAT.md` | 2 paragraphs |
| Need social/investigation | `mechanics/SOCIAL_INVESTIGATION.md` | 2 paragraphs |
| Need survival check | `mechanics/SURVIVAL.md` | 1 paragraph |
| Need governance settlement | `mechanics/GOVERNANCE.md` | 3 paragraphs |
| Need random encounter | `mechanics/RANDOM_TABLES.md` | 1 paragraph |
| Need map info/drawing/consistency | `maps/MAP_INDEX.md` + corresponding `maps/**` | 3 paragraphs |
| Need character network/Rhine crisis background | `Char.md` | 2 paragraphs |
| Need world-building knowledge | `Background*.md` | 2 paragraphs |
| Need novel progress | `Writing/Fiction_index.md` | 1 paragraph |

---

## RAG::002 Fragment Extraction Rules

### Hit Target Table/List
```markdown
## COMBAT::initiative    ← Extract "initiative order" paragraph
## SURVIVAL::rest        ← Extract "rest rules" paragraph
```

### Prohibited Actions
- Extract entire tables (only take relevant rows)
- Extract entire chapters (only take relevant paragraph lead + key lines)
- Extract entire background encyclopedia paragraphs

### Fragment Format Template
```markdown
> [File Path: Anchor]
> Summary: 1-sentence summary
> Content: Core rule (≤120 characters)
```

---

## RAG::003 Conflict Resolution

When multiple files provide conflicting information:

```
Priority: Event > State > Canon > Writing
```

1. Check `sessions/session_*.md` (Event)
2. Check `index.md` / `lore/WORLD_STATE.md` / `STATE_PANEL.md` (State)
3. Check `Background*.md` (Canon)
4. Writing only used for "consistency check", not as setting source

---

## RAG::004 Retrieval Prohibition Words

The following situations **prohibit** triggering RAG:
- Immersive narrative description
- NPC dialogue generation
- Inner dialogue triggering
- Player free action adjudication (unless involving explicit mechanism)

---

## RAG::005 Caching Strategy

### Long-term Cacheable (Static)
- `Background*.md` world-building settings
- `mechanics/*.md` rule files
- `mechanics/RANDOM_TABLES.md` random tables

### Refresh Each Session (Variable)
- `index.md` status snapshot
- `sessions/session_*.md` session records
- `Fiction_index.md` novel progress

---

## RAG::006 RAG Fragment Example

**Scenario**: Player encounters suspicious person on street, need to determine if random encounter triggers

```markdown
> [mechanics/RANDOM_TABLES.md:21.1]
> Summary: Street encounter d10 random table
> Content: "Roll 10 check street encounter. 1=trauma trigger, 2=city watch search, 3=mysterious note..."

> [mechanics/SOCIAL_INVESTIGATION.md:INSIGHT]
> Summary: Insight check rules
> Content: "Insight DC=8+target insight skill. Gap ≥10 completely see through, 5-9 suspicious, <0 believe."
```

