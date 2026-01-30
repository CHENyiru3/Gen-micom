# INIT_PROTOCOL.md — 初始化协议（空白战役 → 可玩）

> **目标**：让用户自定义角色与游玩偏好，并把这些偏好外置成"稳定数据"，用于 DM 个性化与上下文压缩。
> **内核**：回合运行仍以 `KERNEL_PROMPT.md` 为准；本文件只定义"初始化如何落盘"。
>
> **推荐流程（两段式）**：先用对话收集 Step A/B/C 的答案并确认摘要 → 再由 AI 输出 **JSON tool_calls** 调用 `init_campaign` 进行落盘（JSON keys 映射见 §1.1）。

---

## 0) 初始化产物（必须落盘）

初始化完成后，必须存在并保持可 patch：

- 玩家偏好（稳定）：`campaigns/<id>/PLAYER_PROFILE.md`
- PC 档案（稳定）：`campaigns/<id>/characters/PCs/pc_current.md`
- 0 号会话已切换：创建 `campaigns/<id>/sessions/session_YYYY-MM-DD_<slug>.md`，并 patch `campaigns/<id>/sessions/CURRENT_SESSION.md`
- 状态面板已填充：`campaigns/<id>/STATE_PANEL.json`
- 热启动包已写入：`campaigns/<id>/HOT_PACK.json`（`CONTEXT_PACK_NEXT`）
- DM 规划文件存在：`.DM_PLANNER.md`（隐藏，不对玩家泄露）
- **主线蓝图存在**：`campaigns/<id>/.DM_BLUEPRINT.md`（主线/关键人物/关系网）
- **主线面板存在**：`campaigns/<id>/MAINLINE_PANEL.json`

---

## 1) 初始化交互步骤（建议 3 回合完成）

> **推荐执行方式（两段式）**：  
> 先用对话把 Step A/B/C 的答案收集齐并确认摘要 → 再由 AI 输出 JSON tool_calls 调用 `init_campaign` 落盘（确保产物齐全且格式稳定）。

### Step A：偏好与安全（OOC）
询问并写入 `campaigns/<id>/PLAYER_PROFILE.md`：
- 叙事风格：写实/史诗/黑色幽默/恐怖浓度
- 规则强度：规则优先/叙事优先/折中
- 难度与容错：轻松/标准/硬核；失败前进强度
- 节奏：快/中/慢；战斗频率
- 内容边界：禁忌/淡化/可接受范围（可选）

输出时同时给“偏好摘要”（≤8 行，使用 `KEY=VALUE`），便于每回合快速加载与压缩。

#### 快速预设（用户友好）

用户可以直接选一个预设，AI 自动填充未给出的字段：
- `PRESET=轻松叙事`：规则弱、后果温和、节奏快、战斗少
- `PRESET=标准冒险`：折中、节奏中、战斗中
- `PRESET=硬核写实`：规则强、代价强、资源压力高、战斗少但危险
- `PRESET=悬疑调查`：调查优先、战斗低、线索密度高
- `PRESET=宗教恐怖`：恐怖浓度高、圣所/异象频繁、代价中到强

### Step B：PC 创建（OOC → 角色）
询问并写入 `campaigns/<id>/characters/PCs/pc_current.md`：
- 名字/称呼/性别代词（可选）
- 身份原型（1 句话）
- 驱动力（1–2 条）
- 2 个强项 + 1 个弱点（用于裁决与风格）
- 关键背景钩子（1 条，供 DM 生成任务）
- 起始装备/资源偏好（轻量）

### Step C：开局选择（软路由）
让玩家从 2–3 个“开局钩子”选择（与世界设定兼容，但不绑定旧剧情）。

完成后：
- 创建新 session 文件并写入 `Decision: 初始化`（append）
- Patch `campaigns/<id>/sessions/CURRENT_SESSION.md` 指向新文件
- Patch `campaigns/<id>/STATE_PANEL.json`：时间/地点/指标初始化、任务空表、时钟空表
- Patch `campaigns/<id>/HOT_PACK.json` 写入首个 `CONTEXT_PACK_NEXT`
- Patch `campaigns/<id>/MAINLINE_PANEL.json`（写入主线状态）

### Step D：主线蓝图生成（幕后，强制）
基于 **世界设定 + 玩家偏好** 生成幕后大纲（不展示给玩家）：
- 2–4 条主线剧情（每条 1 句）
- 5–8 个关键 NPC（姓名/立场/关系）
- 关键冲突与主题（2–4 条）
- 关系网（最多 8 条边，A—关系—B）
- 变体空间：可替换的支线入口（2–3 条）

写入 `campaigns/<id>/.DM_BLUEPRINT.md`，并在 `HOT_PACK.json` 顶部写入 4–6 行 **SPINE 摘要**（≤6 行）：
```
SPINE:
- 主线1…
- 主线2…
KEY_NPCS: A, B, C
THEME: ...
```

---

## 1.1) 初始化答案 → 落盘参数映射（给 AI/Agent）

`campaign_manager.py init` 支持两种输入：
- **命令行参数**：适合直接执行
- **JSON 答案文件**：`python3 scripts/campaign_manager.py init --from answers.json`（参数优先级：命令行 > JSON）

JSON keys（建议全用 snake_case）：

### 时间与会话
- `date` → `campaigns/<id>/sessions/session_YYYY-MM-DD_<slug>.md`、`campaigns/<id>/STATE_PANEL.json`、`campaigns/<id>/HOT_PACK.json`
- `slug` → session 文件名 `<slug>`（未给则由 `pc_name`+`start_loc` 生成）

### 偏好（写入 `campaigns/<id>/PLAYER_PROFILE.md` “偏好摘要”）
- `preset`（可选）：`轻松叙事` / `标准冒险` / `硬核写实` / `悬疑调查` / `宗教恐怖`
- `style` → `STYLE=...`
- `difficulty` → `DIFFICULTY=...`
- `rules` → `RULES=...`
- `pacing` → `PACING=...`
- `combat_freq` → `COMBAT_FREQ=...`
- `mystery_vs_action` → `MYSTERY_VS_ACTION=...`
- `lines_veils` → `LINES_VEILS=...`

### PC（写入 `campaigns/<id>/characters/PCs/pc_current.md` 表格）
- `pc_name`（必填）
- `pc_archetype`
- `pc_drive`
- `pc_strengths`
- `pc_weakness`
- `pc_bg_hook`

### 开局（写入 `campaigns/<id>/STATE_PANEL.json` / `campaigns/<id>/HOT_PACK.json` / session 的 Decision）
- `start_loc`
- `start_hook`

---

## 2) 上下文压缩策略（必须）

每回合只需要从偏好中携带 1 行：
- 从 `campaigns/<id>/PLAYER_PROFILE.md` 的“偏好摘要”复制 1 行到 `campaigns/<id>/HOT_PACK.json` 的 `flags`（例如 `STYLE=写实-高压-调查优先`）

其余偏好细节只在“风格明显偏离/玩家修改偏好”时再读。
