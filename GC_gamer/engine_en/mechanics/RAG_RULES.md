# RAG_RULES.md — Retrieval Augmented Generation Rules

> **Purpose**: RAG retrieval strategy, gate, snippet extraction specification
> **When to Retrieve**: When specific rules/data needed
> **tags**: [rag, retrieval, policy, context]

---

## RAG::001 Call Gate Strategy

### Default Strategy
- **Prohibit**: Automatically retrieve `campaigns/<id>/Writing/` directory
- **Prohibit**: Stuff entire table/section into context
- **On-demand retrieval**: Each ≤4 snippets, each ≤80 characters

### Allowed Trigger Retrieval Situations

| Trigger Condition | Retrieval Target | Snippet Limit |
|-------------------|------------------|---------------|
| Combat adjudication needed | `engine/mechanics/COMBAT.md` | 2 snippets |
| Social/investigation needed | `engine/mechanics/SOCIAL_INVESTIGATION.md` | 2 snippets |
| Survival check needed | `engine/mechanics/SURVIVAL.md` | 1 snippet |
| Governance settlement needed | `engine/mechanics/GOVERNANCE.md` | 3 snippets |
| Random encounter needed | `engine/mechanics/RANDOM_TABLES.md` | 1 snippet |
| Map info/drawing/consistency needed | `cartridges/<id>/maps/MAP_INDEX.md` + corresponding `cartridges/<id>/maps/**` | 3 snippets |
| Character network/character files needed | `cartridges/<id>/characters/` | 2 snippets |
| World knowledge needed | `cartridges/<id>/lore/CANON/*` | 2 snippets |
| Novel progress needed | `campaigns/<id>/Writing/Fiction_index.md` | 1 snippet |

---

## RAG::002 Snippet Extraction Rules

### Target Table/List Hit
```markdown
## COMBAT::initiative    ← Extract "Initiative Order" paragraph
## SURVIVAL::rest        ← Extract "Rest Rules" paragraph
```

### Prohibited Behaviors
- Extract complete table (only take relevant rows)
- Extract complete chapter (only take relevant paragraph header + key lines)
- Extract entire background encyclopedia paragraph

### Snippet Format Template
```markdown
> [File Path: Anchor]
> Summary: 1-sentence summary
> Content: Core rules (≤80 characters)
```

---

## RAG::003 Conflict Resolution

When multiple files provide conflicting information:

```
Priority: Event > State > Canon > Writing
```

1. Check `campaigns/<id>/sessions/session_*.md` (Event)
2. Check `campaigns/<id>/index.md` / `campaigns/<id>/WORLD_STATE.md` / `campaigns/<id>/STATE_PANEL.json` (State)
3. Check `cartridges/<id>/lore/CANON/*` (Canon)
4. Writing only used for "consistency check", not as setting source

---

## RAG::004 Retrieval Disable Words

The following situations **prohibit** triggering RAG:
- Immersive narrative description
- NPC dialogue generation
- Inner dialogue trigger
- Player free action adjudication (unless specific mechanism involved)

---

## RAG::005 Caching Strategy

### Long-term Cacheable (Static)
- `cartridges/<id>/lore/CANON/*` World setting
- `engine/mechanics/*.md` Rule files
- `engine/mechanics/RANDOM_TABLES.md` Random tables

### Refresh Each Session (Variable)
- `campaigns/<id>/index.md` Status snapshot
- `campaigns/<id>/sessions/session_*.md` Session records
- `campaigns/<id>/Writing/Fiction_index.md` Novel progress

---

## RAG::006 RAG Snippet Examples

**Scenario**: Player encounters suspicious person on street, needs to determine if random encounter triggers

```markdown
> [engine/mechanics/RANDOM_TABLES.md:21.1]
> Summary: Street encounter d10 random table
> Content: "Roll 10 to check street encounter. 1=Trauma trigger, 2=City guard search, 3=Mysterious note..."

> [engine/mechanics/SOCIAL_INVESTIGATION.md:INSIGHT]
> Summary: Insight check rules
> Content: "Insight DC=8+target Insight skill. Gap≥10 completely see through, 5-9 suspicious, <0 believe."
```
