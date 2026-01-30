# CARTRIDGE.md — card_gal_test

cartridge_id: card_gal_test
version: 0.1.0
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

---

# GALGAME_CARTRIDGE_SEED v2

## 主题
轻松异世界冒险（偏Re:从零类氛围，但更轻松）+ 多女主可攻略 + Gal对话镜头语言

## 模式
- 单Agent
- 低上下文（FC时代）
- 强制类命令行
- 支持"补充:"热补丁

## 命令协议
- [SCENE] 场景/时间/地点控制（START / NEXT / TRAVEL / TIME+）
- [SAY] 玩家对白（对某角色或泛指）
- [ACT] 玩家行动（不代演玩家）
- [LOOK] 观察/检查
- [ASK] 提问/让NPC解释
- [TALK] 指定对话对象（建议 @句柄）
- [CHOICE] 做出明确选择（A/B/C…）
- [INV] 背包/金钱/道具使用
- [OOC] 规则/工程/存档/纠错
- 继续场景：仅此一条不需要命令头

## @句柄规范
- 女主使用短句柄（2-3字）：如 @莉亚 @米娅 @塞拉
- 玩家可用 [TALK] @莉亚 / [SAY] @米娅 "……" 来精确定位

## 热补丁
以「补充：」开头立即生效，覆盖之前设定（除非违反硬规则）

## 内容边界
- 允许：恋爱向剧情、日常相处、暧昧、拥抱、亲吻、调情、告白、同居、结婚、冒险同伴羁绊
- 可输出露骨性描写：用暗示处理，不写细节
- 禁止：未成年暗示、强迫/非自愿、以及明显露骨的性行为细节

## 女主模板
- handle: @名字（2-3字）
- archetype: 元气/傲娇/冷淡/天然/大小姐/学者/骑士等
- vibe: 轻松关键词3个
- hook: 初遇事件一句话
- affection: 0~100（初始 5~15）
- flags: 2-4个特征
- taboo: 1条绝不踩的雷
