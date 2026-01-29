# CAMPAIGN_PROTOCOL.md — 战役管理协议

> **用途**：如何创建、切换和管理战役
> **核心原则**：战役之间相互隔离；core（机制、设定、地图）是共享的

---

## 0) 战役目录结构

```
campaigns/
├── _template/              # 新战役的模板
│   ├── root/               # 战役根文件（符号链接到根目录）
│   ├── characters/         # 角色文件
│   ├── quests/             # 任务文件
│   ├── sessions/           # 会话文件
│   └── Writing/            # 写作文件
├── campaign_0001/          # 第一个战役
│   ├── root/               # 战役特定的根文件
│   ├── characters/
│   ├── quests/
│   ├── sessions/
│   └── Writing/
└── campaign_0002/          # 第二个战役
    └── ...
```

---

## 1) 创建新战役

### 方法 A：使用控制指令（推荐）

发送：`<新战役 campaign_XXXX>`

AI 将：
1. 从 `_template` 创建目录结构
2. 初始化空白状态文件
3. 更新 `CURRENT_CAMPAIGN.md` 指向新战役
4. 重建符号链接

### 方法 B：使用 Python 脚本

```bash
python3 scripts/campaign_manager.py new --id campaign_XXXX
```

---

## 2) 切换战役

### 方法 A：使用控制指令（推荐）

发送：`<切换战役 campaigns/campaign_XXXX>`

AI 将：
1. 更新 `CURRENT_CAMPAIGN.md` 指向目标战役
2. 重建符号链接到目标战役

### 方法 B：使用 Python 脚本

```bash
python3 scripts/campaign_manager.py switch --path campaigns/campaign_XXXX
```

---

## 3) 符号链接管理

以下路径是符号链接，指向 `campaigns/<current>/`：

| 路径 | 指向 |
|------|-----------|
| `sessions/` | `campaigns/<current>/sessions/` |
| `quests/` | `campaigns/<current>/quests/` |
| `characters/` | `campaigns/<current>/characters/` |
| `Writing/` | `campaigns/<current>/Writing/` |
| `STATE_PANEL.md` | `campaigns/<current>/root/STATE_PANEL.md` |
| `HOT_PACK.md` | `campaigns/<current>/root/HOT_PACK.md` |
| `OBJECT_INDEX.md` | `campaigns/<current>/root/OBJECT_INDEX.md` |
| `PLAYER_PROFILE.md` | `campaigns/<current>/root/PLAYER_PROFILE.md` |
| `GOVERNANCE_PANEL.md` | `campaigns/<current>/root/GOVERNANCE_PANEL.md` |
| `.DM_SECRETS.md` | `campaigns/<current>/root/.DM_SECRETS.md` |
| `.DM_PLANNER.md` | `campaigns/<current>/root/.DM_PLANNER.md` |

---

## 4) 当前战役跟踪

当前活跃战役记录在 `CURRENT_CAMPAIGN.md` 中：

```markdown
# CURRENT_CAMPAIGN.md

campaign_id: campaign_0001
campaign_path: campaigns/campaign_0001
created: 2026-01-29
last_switched: 2026-01-29
```
