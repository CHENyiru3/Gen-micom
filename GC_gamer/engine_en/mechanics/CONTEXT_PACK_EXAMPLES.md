# CONTEXT_PACK_EXAMPLES.md — Context Pack Examples (Content/Samples, Allow Changes)

> **Purpose**: Examples and historical compatibility; specification follows `engine/mechanics/CONTEXT_PACK.md`.
> **Note**: This file can contain specific world content (location names, NPC names, quest names, etc.), therefore treated as "content pack/samples".

---

## EX::001 Session Recovery Package (Example)

```md
<!-- CONTEXT_PACK_NEXT
t=1444-Crack Phase
loc=Nebelheim Cathedral Confession Room Basement Entrance
pc=Clemond (Fake Theology Student)
grace=6 debt=4 rumor=2 heat=3
flags=Rumor>=2 Investigation Involved|Heat=3 Being Watched
quests=quest_002:Explore Quarry (in progress)|quest_004:Investigate Them (in progress)
npcs=Marcus:Guilty|Elias:MIA|Reinhold:Dead
inventory=Oil Lamp,Quarry Map,Basement Key
timers=Investigation Involved (Triggered)|Fehm Court Tracking (in progress)
hooks=Enter Basement|Confirm "Seven People" Clue|Handle Tracking
-->
```

---

## EX::010 Rule Quick Reference Package (Example: Combat/Social/Survival)

These examples belong to "optional cartridge blocks", only load when this turn triggers corresponding domain:
- Combat: `engine/mechanics/COMBAT.md`
- Social/Investigation: `engine/mechanics/SOCIAL_INVESTIGATION.md`
- Survival: `engine/mechanics/SURVIVAL.md`
