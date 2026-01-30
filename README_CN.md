# Gen-micom

本仓库实现"游戏机（Engine）+ 卡带（Cartridge）+ 存档（Campaign）"三层结构，强调小上下文、可热插拔、可持久化的文字跑团体系。

当前入口：
- **共享引擎（Engine）**：`GC_gamer/engine_cn/`
- **卡带与存档（Cartridge/Campaign）**：`Game_Cartridge/Blank_Cartidge_template/game_cn/`

---

## 1) 架构思路（游戏机 / 卡带 / 存储）

- **游戏机（Engine）**：稳定协议与机制，不携带世界内容
  - 位于：`GC_gamer/engine_cn/`（中文）
  - 位于：`GC_gamer/engine_en/`（英文）
- **卡带（Cartridge）**：世界设定与内容库（lore / locations / quests / characters / maps）
  - 位于：`Game_Cartridge/Blank_Cartidge_template/game_cn/cartridges/<id>/`
- **存档（Campaign）**：当前游戏运行态（HOT_PACK / STATE_PANEL / sessions / PCs）
  - 位于：`Game_Cartridge/Blank_Cartidge_template/game_cn/campaigns/<id>/`

入口指针：`Game_Cartridge/Blank_Cartidge_template/game_cn/ACTIVE.md`

---

## 2) 创建游戏（新卡带 / 新战役）

### 2.1 新卡带（从模板卡带起步）

1. 复制 `Game_Cartridge/Blank_Cartidge_template/game_cn/cartridges/_template/`
   → `Game_Cartridge/Blank_Cartidge_template/game_cn/cartridges/<new_card_id>/`
2. 编辑 `CARTRIDGE.md`：填写 routes / aliases / invariants / feature_flags
3. 填充最小内容索引（lore/locations/quests/characters/maps）

### 2.2 新战役（存档）

> **推荐方式（对话自动化）**：由 AI/Agent 执行脚本与文件修改，你只需对话指令即可。

对话中发送：
```
<新战役 campaigns/<new_campaign>>
```

AI 会自动完成：
- 执行 `campaign_manager.py new`
- 修改 `campaigns/<new_campaign>/CAMPAIGN.md`（设置 `cartridge_id=<new_card_id>` 并锁定版本）

---

## 3) 开始游戏（初始化）

进入卡带后执行初始化（对话自动化）：
- 发送 `<初始化>`（AI 会先读取 `GC_gamer/engine_cn/System.md` 作为入口，再按 `INIT_PROTOCOL.md` 执行落盘）
- 初始化会写入：
  - `campaigns/<id>/PLAYER_PROFILE.md`
  - `campaigns/<id>/characters/PCs/pc_current.md`
  - `campaigns/<id>/sessions/`（创建首个 session）
  - `campaigns/<id>/STATE_PANEL.md`
  - `campaigns/<id>/HOT_PACK.md`

---

## 3.1 对话命令入口约定（统一入口）

以下命令均先读取 `GC_gamer/engine_cn/System.md` 作为入口路由，然后再读取对应协议文件：
- `<初始化>` → `GC_gamer/engine_cn/INIT_PROTOCOL.md`
- `<新战役 ...>` / `<切换战役 ...>` → `GC_gamer/engine_cn/CAMPAIGN_PROTOCOL.md`
- `<热启动>` / `<继续>` → `GC_gamer/engine_cn/HOT_START.md`

---

## 4) 存档与恢复（热启动）

### 存档（自动）
- 每回合输出 `ARCHIVE_DELTA`，自动 append/patch：
  - `sessions/<current>.md`
  - `HOT_PACK.md`
  - `STATE_PANEL.md`
  - `OBJECT_INDEX.md`

### 恢复（热启动）
- 读取顺序见 `GC_gamer/engine_cn/HOT_START.md`
- 对话中发送：`<热启动>` 或 `<继续>`
- **入口一致性**：会先读取 `GC_gamer/engine_cn/System.md`，再按 `HOT_START.md` 指定顺序加载（含 `ACTIVE.md` → `CAMPAIGN.md` → `CARTRIDGE.md` → `HOT_PACK.md`）。

---

## 5) 热插拔新卡带（换卡带 / 恢复进度）

### 切换卡带
1. 复制或创建新卡带
2. 发送 `<新战役 campaigns/<new_campaign>>`（AI 自动创建并绑定 cartridge）
3. `ACTIVE.md` 会由 AI 自动更新

### 恢复旧进度
切回旧 campaign：
```
<切换战役 campaigns/<old_campaign>>
```
再 `<继续>` 即可恢复。

---

## 6) 小说更新（Fiction Sync）

小说管线位于：
`campaigns/<id>/Writing/PIPELINE.md`

原则：
- 正文不作为回合运行依赖
- 仅从 `sessions/` 与 `STATE_PANEL.md` 同步关键决策
- 需要时由 DM/脚本触发更新

---

## 7) Prompt 优化工程与设计

已完成的关键优化：
- **命令头路由**：`[ACT]/[LOOK]/[ASK]/[FIGHT]/[CAST]/[MANAGE]/[OOC]`
- **HOT_PACK 最小化**：≤100 行，严格控制上下文
- **RAG 限流**：≤4 片段，每段 ≤80 字，ROUTE_FACTS 8–12 条
- **索引头部摘要（RAG_HEAD）**：索引文件顶部 4–6 行摘要
- **句柄系统**：@handle + aliases，减少玩家记忆负担
- **Engine 外置**：`GC_gamer/engine_cn` / `engine_en` 统一复用

设计目标：
- 极小 token 预算下稳定推进
- 世界设定与运行态分离
- 可持续热插拔卡带与存档恢复

## 说明书：玩家交互指南
命令头（行首必须）
标签	用途	示例
[ACT] / [行动]	做事	[ACT]{检查锁门}
[LOOK] / [观察]	观察	[LOOK]{观察人群}
[ASK] / [对话]	说话	[ASK]"你是谁？"
[FIGHT] / [战斗]	打架	[FIGHT]{先发制人}
[CAST] / [施法]	施法	[CAST]{祈祷}
[MANAGE] / [管理]	后勤	[MANAGE]{检查背包}
[OOC]	规则/系统	[OOC] DC是多少？
内心对话

[ACT]{内心: 学者}     ← 知识/推理时
[ACT]{内心: 怀疑}     ← 信仰/教会相关
[ACT]{内心: 圣灵}     ← 祈祷/异象时
短码菜单
每回合结束会显示菜单，可用短码直接输入：


[ACT]{与 N1 交谈}     ← N1 = 第一个NPC
[ACT]{去 L2}          ← L2 = 第二个地点
快速示例

[ACT]{观察广场上的人群} --risk low
[ASK]"他们犯了什么罪？"
[ACT]{内心: 学者} ← 触发学者内心独白
