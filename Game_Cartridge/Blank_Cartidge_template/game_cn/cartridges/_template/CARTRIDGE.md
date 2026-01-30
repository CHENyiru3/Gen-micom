# CARTRIDGE.md — Template Cartridge（卡带模板）

cartridge_id: template
version: 0.2.0
language: zh-CN

## entrypoints
- lore/INDEX.md
- locations/LOCATION_INDEX.md
- maps/MAP_INDEX.md
- quests/QUEST_LOG.md
- characters/NPCs/npc_roster.md
- characters/PCs/README.md
- ROUTES.md

## routes
（已迁移至 `ROUTES.md`）

## aliases
@template_loc: ["模板地点"]
@template_npc: ["模板NPC"]

## invariants
- 模板卡带可以扩展但默认提供一份最简百科。
- 所有新卡带必须在 `cartridge_version_lock` 中锁定版本。

## feature_flags
indicators: true
governance: true
fiction_sync: true
map_system: true
