# System.md — World Instance Router（入口，不含内核细节）

> **用途**：本世界实例的“入口/路由”文件：告诉内核去哪里读内容包与状态。  
> **稳定内核协议**：见 `engine/KERNEL_PROMPT.md`（回合管线、HUD、RAG、ARCHIVE_DELTA）。
> **角色分工**：见 `engine/ROLE_SYSTEMS.md`（AUTHOR/BUILDER/DM 的读取范围）。  
> **角色入口**：`engine/System_AUTHOR.md` / `engine/System_BUILDER.md` / `engine/System_DM.md` / `engine/System_SAVE_READ.md`  
> **速记入口**：`engine/ROLE_ENTRY.md`

---

## 0) 热启动（推荐入口）

按 `engine/HOT_START.md` 执行。

最小读取集合：
- `ACTIVE.md`
- `campaigns/<id>/CAMPAIGN.md`
- `cartridges/<id>/CARTRIDGE.md`
- `campaigns/<id>/HOT_PACK.md`
- `campaigns/<id>/PLAYER_PROFILE.md`
- `campaigns/<id>/characters/PCs/pc_current.md`
- `campaigns/<id>/OBJECT_INDEX.md`
- `campaigns/<id>/sessions/CURRENT_SESSION.md` → 对应 `campaigns/<id>/sessions/session_*.md` 末尾 Decision
- `campaigns/<id>/STATE_PANEL.md`
- `campaigns/<id>/index.md`（只读“下一步目标/指针”）

初始化入口：`engine/INIT_PROTOCOL.md`

---

## 0.1 输出节奏规则（信息控制）

- **允许无发现/无推进**：普通查看/尝试应以“无发现”收束为常态。
- **失败前进仅限有明确风险**：只有存在代价或威胁时才使用“失败前进”。
- **若无发现**：必须明确写“无关键线索/无新进展”，并给出合理原因（概率/视线/遮挡/时间/噪声/误判）。

## 0.2 用户指南提示（仅一次）

- 每次新建/读取战役后：若 `HOT_PACK.md` 中 `guide_shown` 为空或为 `0`，必须输出**一次**简短用户指南。
- 输出后将 `guide_shown=1` 写回 `HOT_PACK.md`（通过 ARCHIVE_DELTA patch）。

## 0.3 读档一致性规则（防幻觉）

- **读档/继续阶段禁止新增事实**：恢复时只能重述 `*_快照.md` 与 `HOT_PACK.md` 已有信息。
- **不得生成新线索/新NPC/新地点/新文本**；若缺信息，提示“未记录/需要玩家行动触发”。
- **恢复输出必须标记为“读档摘要”**，不作为新剧情推进。

## 0.4 风格一致性（防漂移）

- 叙事输出必须遵循 `engine/KERNEL_PROMPT.md` 的“固定叙事样式”。
- **读档/继续时不得改变写作风格与格式**：保持段落分区、判定块、结果表、动作尾的固定结构。

## 0.5 角色分工入口（强制）

每次对话开始先声明角色：
- `ROLE=AUTHOR`（卡带内容创作者）
- `ROLE=BUILDER`（战役创建者）
- `ROLE=DM`（运行主持）

角色与读取范围详见 `engine/ROLE_SYSTEMS.md`，严禁越界读写。

---

## 1) 世界实例：内容包入口（会变）

### 1.1 状态（State）
- `campaigns/<id>/STATE_PANEL.md`（玩家可见常驻面板）
- `campaigns/<id>/index.md`（导航索引/短摘要）
- `campaigns/<id>/WORLD_STATE.md`（后台世界状态：指标、时钟、完整线索索引）
- `campaigns/<id>/GOVERNANCE_PANEL.md`（统治面板：领地/追随者/资产；可选）

### 1.2 事件（Event）
- `campaigns/<id>/sessions/SESSION_INDEX.md`
- `campaigns/<id>/sessions/session_YYYY_Name_压缩.md` (压缩摘要)
- `campaigns/<id>/sessions/session_YYYY_Name_快照.md` (保存点)

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

## 3) 输出协议（重要）

### 双通道输出规则

**每次剧情推进必须同时执行：**

1. **写入MD文件** - 持久化记录剧情进展到 `sessions/session_*.md`
2. **输出到对话** - 在CLI界面展示给用户（用户看不到MD文件内容）

**格式要求**：
- MD文件：按 `session_*.md` 格式规范，记录完整剧情片段
- 对话输出：精选关键场景 + 玩家可选行动菜单

### 会话压缩与重建（强制）

**目标**：把「可运行上下文」压到最小，保证长期游玩不爆 token。

- 运行时只引用：`*_快照.md`（snapshot）
- 压缩版：`*_压缩.md`（compressed）

**递归压缩规则（每回合结束）**：
1. 将“上一轮之前的全部历史”压缩写入 → `session_YYYY_名称_压缩.md`
2. 保留“上一轮 + 本轮”的**未压缩**内容写入 → `session_YYYY_名称_快照.md`
3. 在 `SESSION_INDEX.md` 中只指向最新 **快照** 文件

**对话引用约束**：
- 对话中仅引用 `*_快照.md` 与 `HOT_PACK.md`
- `*_压缩.md` 仅在用户要求回溯时引用

### 回合结束清单

**每轮对话结束时必须按顺序执行以下所有步骤：**

1. [ ] 写入 session MD（记录行动与结果）
2. [ ] 更新 STATE_PANEL.md（指标、NPC、线索、时钟）
3. [ ] 更新 HOT_PACK.md（上下文包）
4. [ ] 在对话中输出场景摘要 + 可选行动
5. [ ] 显示 HUD 短码菜单（如有交互对象）
6. [ ] **递归压缩“上一轮之前历史”（*_压缩.md）**（强制执行）
7. [ ] **生成快照（含上一轮+本轮，*_快照.md）并更新 SESSION_INDEX.md**（强制执行）

> ⚠️ 压缩步骤 6-7 是**强制性的**，不可跳过，否则会导致 token 无限增长。

---

## 4) 上下文压缩协议（强制执行）

### 4.1 Session 文件结构（双文件制）

每个 session 采用递归双文件结构：

```
session_YYYY_名称_压缩.md   ← 摘要版（多回合累积）
session_YYYY_名称_快照.md   ← 当前运行快照
```

### 4.2 压缩时机

**每轮对话结束时必须执行**：
- 递归压缩“上一轮之前历史”（*_压缩.md）
- 更新快照（保留上一轮+本轮未压缩内容，*_快照.md）

### 4.3 压缩规则

**摘要保留内容**：
- 核心Decision（决策点）
- 关键事件（1-5条）
- NPC及关系
- 线索列表
- 状态变化（指标/时钟）

**删除内容**：
- 冗长的内心独白
- 重复的对话细节
- 场景描写（保留关键信息即可）

### 4.4 Session 文件命名

统一为：
- `session_YYYY_名称_压缩.md`
- `session_YYYY_名称_快照.md`

### 4.5 强制检查点

在每轮对话的「回合结束清单」中：

- [ ] 生成 *_压缩.md
- [ ] 生成 *_快照.md
- [ ] 对话只引用 *_快照.md
- [ ] 不保留完整对话文件
