# skills_repo

本目录用于存放**可安装到 Codex 系统级别**的 skills（稳定内核协议/工作流），与剧情内容解耦。

## 技能列表

- `rpg-dm-kernel-protocol`：跑团内核协议（HOT/WARM/COLD、HUD短码、RAG最小加载、ARCHIVE_DELTA 增量存档）
- `rpg-dm-content-pack-authoring`：内容包编写（cartridges lore/NPC/quests/locations），不改内核
- `rpg-dm-fiction-sync`：会话→小说同步（不产生新 Canon）
- `rpg-dm-maps`：地图内容包维护（三件套：render/data/logic + fog-of-war + 版本）
- `rpg-dm-governance-panel`：统治面板维护（资产/追随者/军队/收支/治理时钟）
- `rpg-dm-function-calling-local`：本地 function calling（JSON tool_calls + role whitelist + tools_runner）

## 安装方式（两选一）

### A) 直接复制（本机最简单）

把对应技能目录复制到：`~/.codex/skills/`

例如：
- `skills_repo/rpg-dm-kernel-protocol` → `~/.codex/skills/rpg-dm-kernel-protocol`

### B) 用 skill-installer（从 GitHub 仓库安装）

把整个 repo 推到 GitHub 后，可按“路径安装”：
- repo: `<owner>/<repo>`
- path: `skills_repo/rpg-dm-kernel-protocol`（或其他技能目录）

安装完成后需要 **Restart Codex** 以加载新 skills。
