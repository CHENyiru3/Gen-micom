# README.md — RPG 游戏模板

这是一个**文件系统式 TTRPG 模板**，专为 LLM/DM 自动化设计。本模板提供完整的结构，可根据您自己的世界设定、机制和内容进行定制。

---

## 快速开始（使用本模板）

1. **复制本模板**以创建您的游戏
2. **阅读 Generate_game.md** 了解如何自定义本模板
3. **填写占位符设置**——用您自己的世界、角色和规则填充
4. **开始游戏**——在您的 LLM 会话中运行 `<初始化>`

---

## 0) 模板结构概览

```
game_cn/                    # 中文版本模板
├── KERNEL_PROMPT.md        # 稳定 DM 内核协议（怎么跑）
├── System.md               # 世界实例路由器
├── README.md               # 本文件
├── INIT_PROTOCOL.md        # 战役初始化
├── CLI_SPEC.md             # 玩家输入协议
├── HOT_START.md            # 恢复/继续程序
├── ARCHIVE_DELTA.md        # 增量存档规范
├── CONTINUITY_CHECK.md     # 会话结束漂移检查
├── CAMPAIGN_PROTOCOL.md    # 战役管理
├── HOT_PACK.md             # 下一回合上下文包
├── STATE_PANEL.md          # 玩家可见状态面板
├── OBJECT_INDEX.md         # 活跃对象索引
├── PLAYER_PROFILE.md       # 玩家偏好
├── Char.md                 # 角色系统
├── Map-Gen.md              # 地图生成笔记
├── lore/                   # 世界设定库
│   ├── INDEX.md            # 设定入口点
│   ├── CANON/              # 静态世界事实（自定义此项！）
│   ├── MIST/               # 超自然元素（自定义此项！）
│   └── MECHANICS/          # 游戏机制指标
├── mechanics/              # 游戏规则和系统
├── maps/                   # 地图内容（render/data/logic）
├── skills_repo/            # 可安装的 Codex 技能
├── campaigns/              # 战役存档
│   └── _template/          # 新战役模板
├── sessions/               # 会话记录
├── characters/             # 角色文件
├── quests/                 # 任务日志
├── locations/              # 地点文件
└── scripts/                # 自动化脚本
```

---

## 1) 文件分类

### 核心内核文件（稳定）
这些文件定义**游戏如何运行**，不应被修改：
- `KERNEL_PROMPT.md` — 回合管线、HUD、RAG、ARCHIVE_DELTA
- `System.md` — 世界实例路由器
- `CLI_SPEC.md` — 玩家输入协议
- `HOT_START.md` — 恢复程序
- `INIT_PROTOCOL.md` — 初始化流程
- `ARCHIVE_DELTA.md` — 存档格式
- `CONTINUITY_CHECK.md` — 漂移验证

### 游戏状态文件（运行时）
这些是**游戏中自动生成**的：
- `HOT_PACK.md` — 下一回合上下文（自动 patch）
- `STATE_PANEL.md` — 持久状态（自动 patch）
- `OBJECT_INDEX.md` — 活跃对象（自动 patch）
- `PLAYER_PROFILE.md` — 玩家偏好

### 内容文件（自定义！）
这些是您**定义世界的地方**：
- `lore/CANON/*` — 世界历史、地理、势力
- `lore/MIST/*` — 超自然规则和现象
- `mechanics/*` — 战斗、生存、社交规则
- `maps/*` — 地图数据和逻辑
- `characters/NPCs/*` — NPC 定义
- `locations/*` — 地点描述
- `quests/*` — 任务内容

---

## 2) HOT（热缓存）概念

模板使用 **HOT/WARM/COLD** 文件访问模式：

### HOT（每回合读取）
- `HOT_PACK.md` — 只含 `CONTEXT_PACK_NEXT`（≤25 行）
- `PLAYER_PROFILE.md` — 偏好摘要（≤8 行）
- `OBJECT_INDEX.md` — 活跃指针 + 1 行摘要
- `STATE_PANEL.md` — 只读变化的段落

### WARM（触发时读取）
- `mechanics/*.md` — 触发战斗/生存/社交时
- `lore/CANON/*` — 需要世界事实时
- `lore/MIST/*` — 需要超自然规则时
- `characters/NPCs/*` — NPC 出场时
- `maps/*` — 需要地图时

### COLD（很少读取）
- `Writing/Fiction_par*.md` — 派生叙事
- `.DM_SECRETS.md` / `.DM_PLANNER.md` — DM 幕后文件

---

## 3) 如何自定义

### 步骤一：定义您的世界
编辑 `lore/CANON/` 中的文件：
- `WORLD.md` — 地理、时代、主要地点
- `FACTIONS.md` — 组织、势力、权力中心
- `TIMELINE.md` — 历史事件

### 步骤二：添加超自然元素（可选）
编辑 `lore/MIST/` 中的文件：
- `PHENOMENA.md` — 魔法/奇异现象
- `CREATURES.md` — 怪物和实体

### 步骤三：自定义机制
编辑 `mechanics/` 中的文件：
- `HOUSE_RULES.md` — 掷骰规则、DC、修正值
- `COMBAT.md` — 战斗系统
- `SURVIVAL.md` — 生存机制
- `SOCIAL_INVESTIGATION.md` — 社交规则

### 步骤四：创建起始内容
- 添加 NPC 到 `characters/NPCs/`
- 添加地点到 `locations/`
- 添加任务到 `quests/`
- 在 `maps/` 中创建地图

---

## 4) 开始游戏

1. 发送 `<初始化>` 开始战役设置
2. 配置玩家偏好（写入 `PLAYER_PROFILE.md`）
3. 创建玩家角色（写入 `characters/PCs/pc_current.md`）
4. 选择开场钩子
5. 开始游戏！

---

## 5) 热启动（恢复）

当上下文丢失或需要恢复时：
1. 发送 `<热启动>` 或 `<继续>`
2. AI 首先读取 `HOT_PACK.md`
3. 从最近状态恢复上下文
4. 从中断处继续

---

## 6) 战役管理

- `<新战役 campaign_0002>` — 创建并切换到新战役
- `<切换战役 campaigns/campaign_0001>` — 切换到已有战役

战役存储在 `campaigns/<campaign_id>/` 中，彼此隔离。

---

*模板版本：1.0.0*
