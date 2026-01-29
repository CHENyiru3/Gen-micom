# CONTEXT_PACK_EXAMPLES.md — Context Pack Examples (Content/Examples, Allowed to Change)

> **Purpose**: Examples and historical compatibility; specification follows `mechanics/CONTEXT_PACK.md`.
> **Note**: This file can contain specific world content (location names, NPC names, quest names, etc.), therefore treated as "content package/examples".

---

## EX::001 Session Recovery Package (Example)

```md
<!-- CONTEXT_PACK_NEXT
t=1444-Fracture Period
loc=Nebelheim Cathedral Confession Basement Entrance
pc=Clermond(Pseudo-Theology Student)
grace=6 debt=4 rumor=2 heat=3
flags=Rumor>=2Investigation介入|Heat=3Being Watched
quests=quest_002:Explore Quarry(In Progress)|quest_004:Investigate Them(In Progress)
npcs=Marcus:Guilt|Elijah:Missing|Reinhold:Dead
inventory=Oil Lamp,Quarry Map,Basement Key
timers=Investigation介入(Triggered)|Fehm Court Tracking(In Progress)
hooks=Enter Basement|Confirm"Seven People"Clue|Handle Tracking
-->
```

---

## EX::010 Rule Quick Reference Package (Example: Combat/Social/Survival)

These examples belong to "optional cartridge blocks", loaded only when this turn triggers corresponding domain:
- Combat: `mechanics/COMBAT.md`
- Social/Investigation: `mechanics/SOCIAL_INVESTIGATION.md`
- Survival: `mechanics/SURVIVAL.md`

