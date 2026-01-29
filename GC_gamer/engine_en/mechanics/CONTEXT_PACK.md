# CONTEXT_PACK.md — Context Pack Specification (Stable)

> **Purpose**: Compress "content that next turn must remember" into a pasteable small package (HOT cache).
> **Goal**: Stable, short, small, machine-parseable; does not carry world encyclopedia, does not carry full text rules.
> **tags**: [context, pack, schema, snapshot]

---

## CP::000 Hard Constraints
- **Total length**: ≤ 25 lines (suggest ≤ 15 lines)
- **Fields**: Fixed key-value pairs (see CP::100), no new free-form paragraphs
- **Semantics**: Only write "current situation necessary information", not background history
- **Source**: State/Event primarily; if necessary, supplement 1 Canon/Mist conclusion (≤1 line)

---

## CP::100 CONTEXT_PACK_NEXT (Machine-Readable)
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
- `flags`: Key status markers (`|` separated; max 6)
- `quests`: Quest status (`|` separated; max 4)
- `npcs`: NPC relationship/status (`|` separated; max 4)
- `inventory`: Key items (`,` separated; max 5)
- `timers`: Countdown/clocks (`|` separated; max 3)
- `hooks`: Next turn hooks (`|` separated; max 5)

---

## CP::200 Production Rules (End of Each Turn)
1. First extract from this turn's "changes" (indicators/clocks/quest/NPC/clues).
2. Then write content "player must make choices next turn" into `hooks`.
3. If fields overflow: First delete narrative descriptions, then delete low-priority objects, finally merge similar items.

---

## CP::900 Examples
Example set: `engine/mechanics/CONTEXT_PACK_EXAMPLES.md`
