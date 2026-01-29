# INIT_PROTOCOL.md — 初始化协议（空白战役 → 可玩）

> **目标**：让用户自定义角色和游戏偏好，并将这些偏好外置为"稳定数据"以供 DM 个性化和上下文压缩。
> **内核**：回合执行仍遵循 `KERNEL_PROMPT.md`；本文件只定义"如何持久化初始化"。
>
> **推荐流程（两阶段）**：先用对话收集步骤 A/B/C 的答案并确认摘要 → 然后 AI 自动执行 `python3 scripts/campaign_manager.py init ...` 持久化。支持 `--from answers.json` 导入 JSON 格式答案（JSON 键映射见第 1.1 节）。

---

## 0) 初始化输出（必须存在）

初始化完成后，必须存在且保持可 patch：

- 玩家偏好（稳定）：`PLAYER_PROFILE.md`
- PC 文件（稳定）：`characters/PCs/pc_current.md`
- Session 0 已切换：创建 `sessions/session_YYYY-MM-DD_<slug>.md`，patch `sessions/CURRENT_SESSION.md`
- 状态面板已填充：`STATE_PANEL.md`
- 热启动包已写入：`HOT_PACK.md` (`CONTEXT_PACK_NEXT`)
- DM 规划文件存在：`.DM_PLANNER.md`（隐藏，不向玩家暴露）

---

## 1) 初始化交互步骤（推荐 3 回合）

### 步骤 A：偏好与安全（OOC）
询问并写入 `PLAYER_PROFILE.md`：
- 叙事风格：写实/史诗/黑色幽默/恐怖强度
- 规则强度：规则优先/叙事优先/平衡
- 难度与宽容度：简单/标准/硬核；失败前进强度
- 节奏：快/中/慢；战斗频率
- 内容边界：禁忌/淡化/可接受范围（可选）

同时输出"偏好摘要"（≤8 行，使用 `KEY=VALUE`）以实现快速回合加载和压缩。

#### 快速预设（用户友好）

用户可以直接选择预设；AI 自动填充未指定字段：
- `PRESET=轻松叙事`：弱规则，温和后果，快节奏，战斗少
- `PRESET=标准冒险`：平衡，中等节奏，战斗适中
- `PRESET=硬核写实`：强规则，强后果，资源压力大，战斗少但危险
- `PRESET=悬疑调查`：调查优先，战斗少，线索密度高
- `PRESET=宗教恐怖`：恐怖强度高，经常出现圣地/异象，中-强后果

### 步骤 B：PC 创建（OOC → 角色）
询问并写入 `characters/PCs/pc_current.md`：
- 名字/称号/代词（可选）
- 身份原型（一句话）
- 动机（1-2 项）
- 2 个优点 + 1 个缺点（用于裁决和风格）
- 关键背景钩子（1 项，用于 DM 生成任务）
- 起始装备/资源偏好（轻量级）

### 步骤 C：开场选择（软路由）
让玩家从 2-3 个"开场钩子"中选择（与世界设定兼容，不绑定旧剧情线）。

完成后：
- 创建新的 session 文件并写入 `Decision: 初始化`（append）
- Patch `sessions/CURRENT_SESSION.md` 指向新文件
- Patch `STATE_PANEL.md`：时间/地点/指标初始化，空任务表，空时钟表
- Patch `HOT_PACK.md` 写入第一个 `CONTEXT_PACK_NEXT`

---

## 1.1) 初始化答案 → 持久化参数映射（适用于 AI/Agent）

`campaign_manager.py init` 支持两种输入模式：
- **命令行参数**：适合直接执行
- **JSON 答案文件**：`python3 scripts/campaign_manager.py init --from answers.json`（命令行 > JSON 优先级）

JSON 键（建议 snake_case）：

### 时间与会话
- `date` → `sessions/session_YYYY-MM-DD_<slug>.md`、`STATE_PANEL.md`、`HOT_PACK.md`
- `slug` → session 文件名 `<slug>`（如未提供，从 `pc_name`+`start_loc` 生成）

### 偏好（写入 `PLAYER_PROFILE.md` "偏好摘要"）
- `preset`（可选）：`轻松叙事` / `标准冒险` / `硬核写实` / `悬疑调查` / `宗教恐怖`
- `style` → `STYLE=...`
- `difficulty` → `DIFFICULTY=...`
- `rules` → `RULES=...`
- `pacing` → `PACING=...`
- `combat_freq` → `COMBAT_FREQ=...`
- `mystery_vs_action` → `MYSTERY_VS_ACTION=...`
- `lines_veils` → `LINES_VEILS=...`

### PC（写入 `characters/PCs/pc_current.md` 表格）
- `pc_name`（必需）
- `pc_archetype`
- `pc_drive`
- `pc_strengths`
- `pc_weakness`
- `pc_bg_hook`

### 开场（写入 `STATE_PANEL.md` / `HOT_PACK.md` / session Decision）
- `start_loc`
- `start_hook`

---

## 2) 上下文压缩策略（强制）

每回合只需要携带 1 行偏好：
- 从 `PLAYER_PROFILE.md` "偏好摘要" 复制 1 行到 `HOT_PACK.md` `flags`（例如 `STYLE=Realistic-HighPressure-InvestigationPriority`）

其他偏好详情只在"风格显著偏离/玩家修改偏好"时读取。
