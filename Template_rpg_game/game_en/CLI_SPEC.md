# CLI_SPEC.md — Player Command-Line Input Spec

> **Version**: v2.0 | **Purpose**: Player input protocol | **Goal**: Reduce ambiguity, improve retrieval hit rate

---

## A) Basic Format

One input = one `[Tag]{content}` or `[Tag]"content"` combination:

```txt
[Action]{Check locked door, observe door frame structure}
[Dialogue]"Who are you?"
[Combat]{Pre-emptive, ambush creature at door}
[Management]{Check backpack}
[Inner]{Scholar}  ← Trigger inner voice
<OOC> What's the DC?
```

### Special Control Instructions (Don't Enter Story)

- **`<Initialize>`**: Start new campaign initialization. Flow: Use dialogue to collect preferences/PC/opening hook first → after confirmation, automatically execute `python3 scripts/campaign_manager.py init ...` to persist. **Supports `--from answers.json`** to import JSON-format answers (JSON keys mapping see INIT_PROTOCOL.md §1.1).
- `<New campaign campaign_0002>`: Create and switch to new campaign (AI executes script and symbolic link switch)
- `<Switch campaign campaigns/campaign_0001>`: Switch to existing campaign (AI executes symbolic link switch)
- `<Hot Start>` / `<Continue>`: Resume and continue per `HOT_START.md`

**Dual System**:
- `[Tag]`: Tell DM your action type (recommended)
- `@domain /cmd`: System internal routing (optional; use when you want to explicitly "load which rules/materials")

---

## B) Tag Details

| Tag | Alias | Purpose | When to Use |
|-----|-------|---------|-------------|
| `[Action]` | `[a]` | Do things | Move/investigate/cast/spell/sneak/picklock/use items |
| `[Dialogue]` | `[d]` | Speak | Just speaking doesn't count as action, DM may ask to supplement `[Action]` |
| `[Combat]` | `[cb]` | Fight | Enter/continue combat actions |
| `[Management]` | `[m]` | Logistics | Items/rest/money/governance panel |
| `[Inner]` | `[i]` | Inner | Choose: Scholar/Trauma/Doubt/Weariness/Alertness |
| `[OOC]` | `<OOC>` | Ask rules | Rules/system/setting questions |

### Examples

```txt
[Action]{Check locked door, look for pry marks}
[Dialogue]"Father, who were those seven people?"
[Combat]{Sleep spell covering door, then retreat}
[Management]{Rest 1 hour, recover HP}
[Inner]{Scholar} ← Trigger scholar's inner voice
<OOC> What's the DC for this lock?
```

---

## C) @domain Domain Tags (Optional, System Internal Use)

If player wants to explicitly specify scene type, can add `@domain` before tag:

```txt
@scene [Action]{Move to basement}
@invest [Action]{Systematically investigate bloodstains}
@social [Dialogue]{Ask the priest}
@combat [Combat]{Combat round}
@manage [Management]{Inventory items}
```

**Why add @domain?** Like FC game changing cartridges — tell system what rules and materials to load; but you can play without it, DM will auto-infer and prompt.

| Domain | Alias | Trigger Scene |
|--------|-------|---------------|
| `@scene` | `@sc` | Move/observe/general actions |
| `@social` | `@so` | NPC dialogue/negotiation |
| `@invest` | `@iv` | Systematic investigation/reasoning |
| `@combat` | `@cb` | Combat encounter |
| `@manage` | `@ma` | Supplies/trading/rest/faction |

---

## D) Alias System (You Don't Need to Remember IDs)

**You only need to use natural language**, system will automatically map to correct ID:

| You Can Write | System Recognizes As |
|---------------|----------------------|
| "Quarry" / "Locked door" / "Basement" | Auto-map to `loc_xxx` |
| "Father Marcus" / "Elijah" / "Marcus" | Auto-map to `npc_xxx` |
| "Explore Quarry" / "Investigate Them" | Auto-map to `quest_xxx` |

If ambiguity occurs, DM gives you **HUD short code menu** to choose.

---

## E) HUD Short Code Menu

At end of each turn, DM outputs HUD short code menu:

```markdown
[Interactive Targets]
L1: Locked door (rusted iron lock) | L2: Tool shed (abandoned)
N1: Elijah (allied) | N2: Reinhold (new acquaintance)
I1: Gloves (Fehm Court) | I2: Oil lamp
Q1: Explore Quarry | Q2: Investigate Them
```

**You can input directly using short codes**:

```txt
[Action]{Talk to N1}
[Action]{Check I1}
[Action]{Go to L2}
```

**Short Code Rules**:
- `L#` Location point (Location target)
- `N#` NPC
- `I#` Item/Clue (Item)
- `Q#` Quest (Quest)

> Compatibility: `P#` in old documents treated as alias for `L#` (DM will auto-recognize).

---

## F) Inner Dialogue System

Trigger inner voice with `[Inner]{Select: xxx}`:

| Option | Trigger Condition |
|--------|-------------------|
| `[Inner]{Scholar}` | Knowledge/reasoning/observation |
| `[Inner]{Trauma}` | Family/famine/Prussia related |
| `[Inner]{Doubt}` | Faith/church/God related |
| `[Inner]{Weariness}` | Travel/hunger/cold |
| `[Inner]{Alertness}` | Danger/sneaking |
| `[Inner]{Emotion}` | Emotional fluctuations: attraction/intimacy/shame/jealousy/longing/loss |
| `[Inner]{Holy Spirit}` | Prayer/confession/moral choices/uncanny omens/sanctuary atmosphere triggered |

Example: `[Inner]{Scholar}` → DM inserts scholar's inner monologue

---

## G) Risk and DC Reference

| risk | DC Range | Failure Cost |
|------|----------|--------------|
| `low` | 10-12 | Light (time/small noise/small resource) |
| `mid` | 13-16 | Medium (Rumor/Heat rise/injury/lose resource) |
| `high` | 17-20+ | Heavy (legal consequences/Debt+/plot twist) |

---

## H) Quick Examples

### 1) Pick lock
```
[Action]{Check locked door, look for pry marks} --risk mid
```

### 2) Ask NPC
```
[Dialogue]"Father, who were those seven people?"
```

### 3) Systematic investigation
```
[Action]{Check ground bloodstains, infer how long ago someone came} --risk mid --intent "Find evidence of recent visitor"
```

### 4. Recall clue
```
<OOC> Recall clues about fracture movement patterns
```

### 5) Combat round
```
[Combat]{Sleep spell covering door, then retreat 5 meters}
```

### 6) Use item
```
[Action]{Light oil lamp, illuminate passage} --intent "Illumination"
```

### 7) Check status
```
[Management]{Status}
```

### 8) Use HUD short codes (recommended)
```
[Action]{Talk to N1}
```

### 9) Inner trigger
```
[Inner]{Scholar} ← DM will auto-insert scholar voice
```

---

## I) Player-Friendly Rules

1. **Use natural language**: Say "locked door" not `loc_xxx`
2. **Add [Tag]**: Let me know what type you're trying to do
3. **Need help**: Look at HUD short code menu, copy-paste directly
4. **OOC questions**: Use `<OOC>` tag
5. **New campaign**: Use `<Initialize>` to start configuration (character and preferences)

---

*CLI_SPEC.md v2.0 - RPG Game Template*
