# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 处理此仓库中的代码时提供指导。

这是一个**文件系统式 TTRPG 游戏模板**，专为 LLM/DM 自动化设计。模板提供完整的结构，可根据任何世界设定、机制和内容进行定制。

## 项目结构

```
/
├── KERNEL_PROMPT.md        # 稳定 DM 内核协议（怎么跑）
├── System.md               # 世界实例路由器 + 文件入口点
├── README.md               # 主用户指南
├── INIT_PROTOCOL.md        # 初始化协议
├── CLI_SPEC.md             # 玩家输入规范
├── HOT_START.md            # 恢复/继续程序
├── ARCHIVE_DELTA.md        # 增量存档规范
├── HOT_PACK.md             # 下一回合上下文包
├── STATE_PANEL.md          # 玩家可见的持久面板
├── OBJECT_INDEX.md         # 活跃对象索引
├── PLAYER_PROFILE.md       # 玩家偏好
├── Char.md                 # 角色系统概览
├── Map-Gen.md              # 地图生成笔记
└── lore/
    ├── INDEX.md            # 设定 RAG 入口点
    ├── WORLD_STATE.md      # 全局指标 + 动态状态
    ├── CANON/              # 阳光历史（静态世界事实）
    ├── MIST/               # 迷雾历史（超自然元素）
    └── MECHANICS/          # 游戏机制指标

/locations/                 # 地点文件
/characters/
    ├── PCs/                # 玩家角色记录
    ├── NPCs/               # NPC 名册和个人文件
/quests/                    # 任务日志和详情
/sessions/                  # 会话游玩记录
/mechanics/                 # 房规和追踪器
/skills_repo/               # 可安装的 Codex 技能
/maps/                      # 地图内容包
/scripts/                   # 自动化脚本
/campaigns/                 # 战役存档（每战役状态）
```

## 游戏会话

**如何运行会话（内核 vs 内容）**：
- 内核协议：`KERNEL_PROMPT.md`（稳定，永不改变）
- 世界实例/路由器：`System.md`
- 热启动：`HOT_START.md`（首先读取 `HOT_PACK.md`）
- 实时状态：`index.md` + `STATE_PANEL.md` + 最新的 `sessions/session_*.md`

**开始游戏**：
- 使用 `CLI_SPEC.md` 中的输入协议
- 遵循 `KERNEL_PROMPT.md` 中的回合管线
- 使用 `<初始化>` 命令初始化

**当前游戏状态**：查看 `index.md` 了解活跃任务日志、NPC 状态和指标。

## 使用此仓库

这是一个创意/叙事项目，包含用于 LLM 跑团的 markdown 文档：
- 不需要构建命令、测试或 linting
- 文件是游戏内容的 markdown 文档
- 与代码的关键区别：**KERNEL_PROMPT.md 是稳定 API** —— 不要在其中嵌入世界内容

## 关键参考文件

| 文件 | 用途 |
|------|------|
| `KERNEL_PROMPT.md` | 稳定 DM 内核协议 |
| `System.md` | 世界实例/路由器 + 文件入口点 |
| `HOT_START.md` | 稳定重启程序 |
| `HOT_PACK.md` | 最新重启上下文包 |
| `OBJECT_INDEX.md` | 活跃对象热缓存 |
| `ARCHIVE_DELTA.md` | 规范 delta-save |
| `CONTINUITY_CHECK.md` | 会话结束漂移检查清单 |
| `lore/WORLD_STATE.md` | 全局指标和动态世界状态 |
| `mechanics/HOUSE_RULES.md` | 掷骰规则、动作语法、约束 |
| `mechanics/STATE_PANEL_SPEC.md` | 稳定状态面板模式 |
| `sessions/session_*.md` | 会话游玩记录 |
| `Writing/Fiction_index.md` | 小说/叙事进度追踪 |

## HOT/WARM/COLD 模式

- **HOT**：每回合读取（`HOT_PACK.md`、`OBJECT_INDEX.md`、`STATE_PANEL.md` 摘要）
- **WARM**：触发时读取（`mechanics/*.md`、`lore/CANON/*`、`characters/NPCs/*`）
- **COLD**：很少读取（`Writing/`、`.DM_*` 文件）

## 自定义

自定义此模板时：
1. 阅读 `Generate_game.md` 了解完整说明
2. 编辑 `lore/CANON/` 文件设置世界
3. 编辑 `lore/MIST/` 文件设置超自然元素（如有）
4. 编辑 `mechanics/` 文件设置游戏规则
5. 编辑 `characters/NPCs/`、`locations/`、`quests/` 设置内容
