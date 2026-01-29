# CARTRIDGE.md — Nebelmark 1444 (CN)

cartridge_id: nebelmark_1444
version: 1.0.0
language: zh-CN

## entrypoints
- lore/INDEX.md
- locations/LOCATION_INDEX.md
- maps/MAP_INDEX.md
- quests/QUEST_LOG.md
- characters/NPCs/npc_roster.md
- characters/PCs/README.md

## routes
# 命令头 -> 优先检索范围（只读取索引/摘要/条目头部）
[LOOK]:
  - locations/LOCATION_INDEX.md
  - maps/MAP_INDEX.md
[ASK]:
  - characters/NPCs/npc_roster.md
  - lore/INDEX.md
[ACT]:
  - quests/QUEST_LOG.md
  - lore/INDEX.md
[FIGHT]:
  - engine/mechanics/COMBAT.md
  - engine/mechanics/STATE_PANEL_SPEC.md
[CAST]:
  - lore/INDEX.md
  - engine/mechanics/HOUSE_RULES.md
[MANAGE]:
  - quests/QUEST_LOG.md
  - lore/WORLD_STATE.md
[OOC]:
  - engine/mechanics/INDEX.md
  - engine/mechanics/GOVERNANCE_PANEL_SPEC.md

## aliases
# @handle: [别名列表]
@nebelheim_gate: ["雾城北门", "尼伯海姆北门", "城北门"]
@nebelmark_region: ["雾境地区", "内伯尔马克", "Nebelmark"]

## invariants
- 世界处于“雾境”影响下，迷雾现象长期存在。
- 统治与治理面板指标不会在单回合大幅跃迁。

## feature_flags
indicators: true
governance: true
fiction_sync: true
map_system: true
