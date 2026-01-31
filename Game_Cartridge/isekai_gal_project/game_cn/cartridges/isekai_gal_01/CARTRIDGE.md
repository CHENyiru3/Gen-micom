# CARTRIDGE.md — Isekai Gal: 小马利亚（异世界Galgame卡带）

cartridge_id: isekai_gal_01
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
@world_equestria: ["小马利亚","Equestria"]
@loc_ponyville: ["小马谷","Ponyville"]
@loc_canterlot: ["坎特洛特","Canterlot"]
@loc_everfree_forest: ["永恒自由森林","Everfree Forest"]
@loc_crystal_empire: ["水晶帝国","Crystal Empire"]
@map_ponyville_core: ["小马谷·核心区"]
@npc_twilight_sparkle: ["紫悦","Twilight Sparkle"]
@npc_applejack: ["苹果嘉儿","Applejack"]
@npc_rarity: ["珍奇","Rarity"]
@npc_fluttershy: ["柔柔","Fluttershy"]
@npc_rainbow_dash: ["云宝","Rainbow Dash"]
@npc_pinkie_pie: ["碧琪","Pinkie Pie"]
@npc_princess_celestia: ["宇宙公主","Celestia"]
@npc_princess_luna: ["月亮公主","Luna"]
@npc_princess_cadance: ["音韵公主","Cadance"]
@npc_queen_chrysalis: ["虫茧女王","Queen Chrysalis"]
@npc_queen_novo: ["诺沃女王","Queen Novo"]
@npc_derpy_hooves: ["德比","Derpy","Derpy Hooves","Ditzy Doo"]
@npc_lyra_heartstrings: ["莱拉","Lyra","Lyra Heartstrings"]

## invariants
- 本卡带为“异世界穿越 + 恋爱Galgame”内容卡带：只提供世界百科、机制与路由索引，不输出剧情推进结果。
- 物种边界：不引入动画未出现过的物种（可对“背景雌性小马”进行扩写与命名）。
- 地图边界：主要舞台为“小马利亚大陆”，允许多个城市与地区；跨界相关只作为 lore 设定与可选机制说明，不默认启用。

## feature_flags
indicators: true
governance: true
fiction_sync: true
map_system: true
