# CONTEXT_PACK.md — Context Pack Spec (Stable)

> **Purpose**: Compress "content next turn must remember" into a pasteable small package (HOT cache).
> **Goal**: Stable, short, small, machine-parseable; not carry world encyclopedia, not carry full rules.
> **tags**: [context, pack, schema, snapshot]

---
## CP::000 Hard Constraints
- **Total Length**: ≤ 25 lines (recommend ≤ 15 lines)
- **Fields**: Fixed key-value pairs (see CP::100), no new free paragraphs
- **Semantics**: Write only "current situation necessary information", not background history
- **Sources**: State/Event primarily; supplement 1 Canon/Mist conclusion if needed (≤1 line)

---
## CP::100 CONTEXT_PACK_NEXT (Machine Readable)
Use HTML comment block to avoid polluting narrative:
```md
<!-- CONTEXT_PACK_NEXT
t=...
loc=...
pc=...
grace=... debt=... rumor=... heat=...
hp=...
flags=...|...|...
quests=...|...|...
npcs=...|...|...
inventory=...,...,...
timers=...|...|...
hooks=...|...|...
-->
```
### Field Definitions (Fixed)
- `t`: In-game time (short)
- `loc`: Current location (short; can use stable ID or display name)
- `pc`: PC name (can include disguise identity)
- `grace/debt/rumor/heat`: Core indicator values
- `hp`: Optional
- `flags`: Key status markers (`|` separator; max 6)
- `quests`: Quest status (`|` separator; max 4)
- `npcs`: NPC relationship/status (`|` separator; max 4)
- `inventory`: Key items (`,` separator; max 5)
- `timers`: Countdown/clocks (`|` separator; max 3)
- `hooks`: Next turn hooks (`|` separator; max 5)

---
## CP::200 Production Rules (End of Each Turn)
1. First extract from this turn's "changes" (indicators/clocks/tasks/NPC/clues).
2. Then write content "player must make choice next step" into `hooks`.
3. If field overflows: First delete narrative descriptions, then delete low-priority objects, finally merge similar items.

---
## CP::900 Examples
Example collection: `mechanics/CONTEXT_PACK_EXAMPLES.md`

