# System.md — World Instance Router（入口，不含内核细节）

> **用途**：本世界实例的“入口/路由”文件：告诉内核去哪里读内容包与状态。  
> **稳定内核协议**：见 `engine/KERNEL_PROMPT.md`（回合管线、HUD、RAG、ARCHIVE_DELTA）。

---

## 0) 热启动（推荐入口）

按 `engine/HOT_START.md` 执行。

最小读取集合：
- `ACTIVE.md`
- `campaigns/<id>/CAMPAIGN.md`
- `cartridges/<id>/CARTRIDGE.md`
- `campaigns/<id>/HOT_PACK.md`
- `campaigns/<id>/PLAYER_PROFILE.md`
- `campaigns/<id>/OBJECT_INDEX.md`
- `campaigns/<id>/sessions/CURRENT_SESSION.md` → 对应 `campaigns/<id>/sessions/session_*.md` 末尾 Decision
- `campaigns/<id>/STATE_PANEL.md`
- `campaigns/<id>/index.md`（只读“下一步目标/指针”）

初始化入口：`engine/INIT_PROTOCOL.md`

---

## 1) 世界实例：内容包入口（会变）

### 1.1 状态（State）
- `campaigns/<id>/STATE_PANEL.md`（玩家可见常驻面板）
- `campaigns/<id>/index.md`（导航索引/短摘要）
- `campaigns/<id>/WORLD_STATE.md`（后台世界状态：指标、时钟、完整线索索引）
- `campaigns/<id>/GOVERNANCE_PANEL.md`（统治面板：领地/追随者/资产；可选）

### 1.2 事件（Event）
- `campaigns/<id>/sessions/SESSION_INDEX.md`
- `campaigns/<id>/sessions/session_*.md`

### 1.3 设定库（Canon/Mist）
- `cartridges/<id>/lore/INDEX.md`
- `cartridges/<id>/lore/CANON/*`
- `cartridges/<id>/lore/MIST/*`
- `cartridges/<id>/lore/MECHANICS/*`

### 1.4 对象库（NPC/地点/任务）
- `campaigns/<id>/characters/PCs/*`
- `cartridges/<id>/characters/NPCs/*`
- `campaigns/<id>/quests/QUEST_LOG.md`
- `cartridges/<id>/locations/LOCATION_INDEX.md`

### 1.6 地图（Maps，内容包）
- `cartridges/<id>/maps/MAP_INDEX.md`
- `cartridges/<id>/maps/macro/*`、`cartridges/<id>/maps/micro/*`、`campaigns/<id>/maps/runtime/*`

### 1.5 派生叙事（Writing）
- `campaigns/<id>/Writing/PIPELINE.md`
- `campaigns/<id>/Writing/Fiction_index.md`
- `campaigns/<id>/Writing/Fiction_par*.md`

> 默认：回合运行不读取 `Writing/`（除非玩家明确要求“写小说/对齐正文”）。

---

## 2) 输入协议入口

- 玩家输入协议：`engine/CLI_SPEC.md`
- 规则检索门禁：`engine/mechanics/RAG_RULES.md`
- 规则目录索引：`engine/mechanics/INDEX.md`

---

## 3) 兼容与历史

- 旧的“内核大而全提示词”已归档：`archive/System_legacy_2026-01-29.md`
- 存档以 `engine/ARCHIVE_DELTA.md` 为准；历史 session 内可能存在非标准“存档增量”段落，**不作为协议**。
