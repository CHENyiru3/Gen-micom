# CLI_SPEC.md — Mist Frontier: Player Command Line Input Specification

> **Version**: v3.0 | **Purpose**: Player Input Protocol | **Goal**: Reduce ambiguity, improve retrieval hit rate

---

## A) Required Command Headers (Line Start)

Player input must start with a command header (at line start), otherwise it will not advance the story, only return error prompts + examples:

```
[ACT]  Action/Move/Investigation/Stealth
[LOOK] Observe/Inspect/Search
[ASK]  Talk/Ask/Negotiate
[FIGHT] Combat Actions
[CAST] Casting/Ritual/Supernatural Abilities
[MANAGE] Logistics/Rest/Supplies/Governance Panel
[OOC]  Rules/System Questions
```

Compatible aliases (automatically mapped to the above command headers):
- `[行动]` / `[ACT]` → `[ACT]`
- `[对话]` / `[Talk]` → `[ASK]`
- `[战斗]` / `[Fight]` → `[FIGHT]`
- `[管理]` / `[Manage]` → `[MANAGE]`
- `<OOC>` → `[OOC]`

## B) Basic Format

One input = One `[tag]{content}` or `[tag]"content"` combination:

```txt
[ACT]{Check the locked door, observe the door frame structure}
[ASK]"Who are you?"
[FIGHT]{Pre-emptive strike, ambush the creature at the door}
[MANAGE]{Check backpack}
[OOC] What is the DC?
```

### Special Control Instructions (Not in Story)

- **`<初始化>` / `<initialize>`**: Start new campaign initialization. Process: collect preferences/PC/opening hooks → confirm → output **JSON tool_calls** to run `init_campaign` (JSON keys mapping see INIT_PROTOCOL.md §1.1).
- `<新战役 campaign_0002>` / `<new campaign campaign_0002>`: Create/switch campaign (AI outputs JSON tool_calls for `copy_template` + `bind_campaign` + `set_active`)
- `<切换战役 campaigns/campaign_0001>` / `<switch campaign campaigns/campaign_0001>`: Switch to existing campaign (AI outputs JSON tool_calls for `set_active`)
- `<热启动>` / `<continue>` / `<hot start>`: Resume and continue per `HOT_START.md`

**Dual-Layer System**:
- `[tag]`: Tell the DM your action type (recommended)
- `@domain /cmd`: Internal system routing (optional; use when you want to explicitly "load which rules/content")

---

## C) Tag Detailed Explanation (Command Headers)

| Tag  | Alias | Purpose | When to Use |
|------|-------|---------|-------------|
| `[ACT]` | `[行动]` / `[Action]` | Action | Move/investigate/stealth/picklock/use items |
| `[LOOK]` | `[观察]` / `[Observe]` | Observe | Careful inspection/search/view diagrams |
| `[ASK]` | `[对话]` / `[Talk]` | Speak | Talk/ask/negotiate |
| `[FIGHT]` | `[战斗]` / `[Fight]` | Combat | Enter/continue combat actions |
| `[CAST]` | `[施法]` / `[Cast]` | Cast | Spells/rituals/supernatural abilities |
| `[MANAGE]` | `[管理]` / `[Manage]` | Logistics | Items/rest/money/governance panel |
| `[OOC]` | `<OOC>` | Ask Rules | Rules/system/lore questions |

### Examples

```txt
[ACT]{Check the locked door for pry marks}
[ASK]"Father, who are those seven people?"
[FIGHT]{Sleep spell covering the door, then retreat}
[MANAGE]{Rest 1 hour, recover HP}
[OOC] What is the DC for this lock?
```

---

## C) @domain Domain Tags (Optional, Internal Use)

If the player wants to explicitly specify scene type, add `@domain` before the tag:

```txt
@scene [ACT]{Move to the basement}
@invest [ACT]{Systematically investigate the bloodstains}
@social [ASK]{Talk to the father}
@combat [FIGHT]{Combat turn}
@manage [MANAGE]{Inventory check}
```

**Why add @domain?** Like changing FC game cartridges — tell the system which rules and content to load; but you can play without it, the DM will automatically infer and prompt.

| Domain | Alias | Triggered Scene |
|--------|-------|-----------------|
| `@scene` | `@sc` | Move/observe/general action |
| `@social` | `@so` | NPC conversation/negotiation |
| `@invest` | `@iv` | Systematic investigation/reasoning |
| `@combat` | `@cb` | Combat encounter |
| `@manage` | `@ma` | Supplies/trading/rest/territory |

---

## D) Alias System (You Don't Need to Remember IDs)

**You only need to use natural language**, the system will automatically match to the correct ID:

| You Can Write | System Recognizes As |
|---------------|---------------------|
| "Quarry" / "Locked door" / "Basement" | Auto-mapped to `loc_xxx` |
| "Father Marcus" / "Elias" / "Marcus" | Auto-mapped to `npc_xxx` |
| "Explore the quarry" / "Investigate them" | Auto-mapped to `quest_xxx` |

If there's ambiguity, the DM will give you a **HUD short code menu** to choose from.

---

## E) HUD Short Code Menu

At the end of each turn, the DM outputs a HUD short code menu:

```markdown
[Interactive Targets]
L1: Locked door (rusted iron lock) | L2: Tool shed (abandoned)
N1: Elias (allied) | N2: Reinhold (new acquaintance)
I1: Gloves (Fehm Court) | I2: Oil lamp
Q1: Explore the quarry | Q2: Investigate them
```

**You can input directly using short codes**:

```txt
[ACT]{Talk to N1}
[ACT]{Check I1}
[ACT]{Go to L2}
```

**Short Code Rules**:
- `L#` Location target
- `N#` NPC
- `I#` Item/Clue
- `Q#` Quest

> Compatibility: `P#` in old documents is treated as an alias for `L#` (DM will auto-recognize).

---

## F) Inner Dialogue System

When triggering inner voices, use `[ACT]{inner: xxx}`:

| Option | Trigger Condition |
|--------|-------------------|
| `[ACT]{inner: scholar}` | Knowledge/reasoning/observation |
| `[ACT]{inner: trauma}` | Family/famine/Prussia-related |
| `[ACT]{inner: doubt}` | Faith/church/God-related |
| `[ACT]{inner: weariness}` | Travel/hunger/cold |
| `[ACT]{inner: alertness}` | Danger/stealth |
| `[ACT]{inner: emotion}` | Emotional fluctuations (attraction/intimacy/shame/jealousty/longing/loss, etc.) |
| `[ACT]{inner: holy_spirit}` | Pray/confession/moral choices/omen signs/sacred atmosphere |

Example: `[ACT]{inner: scholar}` → DM inserts scholar's inner monologue

---

## G) Risk and DC Reference

| risk | DC Range | Failure Cost |
|------|----------|--------------|
| `low` | 10-12 | Light (time/small noise/small resources) |
| `mid` | 13-16 | Medium (Rumor/Heat up/injury/resource loss) |
| `high` | 17-20+ | Heavy (legal consequences/Debt+/plot twist) |

---

## H) Quick Examples

### 1) Pick Lock
```
[ACT]{Check the locked door for pry marks} --risk mid
```

### 2) Ask NPC
```
[ASK]"Father, who are those seven people?"
```

### 3) Systematic Investigation
```
[ACT]{Check the floor bloodstains, infer how long ago someone was here} --risk mid --intent "Find evidence of recent visitors"
```

### 4) Recall Clue
```
[OOC] Recall clues about rift movement patterns
```

### 5) Combat Turn
```
[FIGHT]{Sleep spell covering the door, then retreat 5 meters}
```

### 6) Use Item
```
[ACT]{Light the oil lamp, illuminate the passage} --intent "Illumination"
```

### 7) Check Status
```
[MANAGE]{status}
```

### 8) Use HUD Short Codes (Recommended)
```
[ACT]{Talk to N1}
```

### 9) Inner Trigger
```
[ACT]{inner: scholar} ← DM automatically inserts scholar voice
```

---

## I) Player-Friendly Rules

1. **Use natural language**: Say "locked door" instead of `loc_xxx`
2. **Add command headers**: Let me know what type of action you want
3. **Need help?**: Look at HUD short code menu, copy-paste directly
4. **OOC questions**: Use `[OOC]` tag
5. **New campaign**: Use `<initialize>` to start configuration (character and preferences)

---

*CLI_SPEC.md v3.0 - Mist Frontier Chronicle: Transience*
