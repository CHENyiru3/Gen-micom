# ROLE_SYSTEMS.md — 角色分工与读取范围（CN）

> **目的**：把“创建内容 / 创建战役 / 运行主持”拆分为不同系统角色，限制读取范围，降低遗忘与漂移。

---

## 1) 角色总览（必须区分）

### A) 内容创作者（Content Author）
**目标**：创建/扩展卡带（世界设定、索引、对象库）。
**职责范围**：背景/基调/机制/世界规则/角色与地点库/路线框架。
**允许读取**：
- `cartridges/<id>/CARTRIDGE.md`
- `cartridges/<id>/lore/**`
- `cartridges/<id>/locations/**`
- `cartridges/<id>/characters/**`
- `cartridges/<id>/quests/**`
- `cartridges/<id>/maps/**`
**禁止读取**（避免被运行态污染）：`campaigns/**` 全部

### B) 战役创建者（Campaign Builder）
**目标**：复制模板、绑定卡带、初始化战役。
**职责范围**：补充细节、确定主线/支线骨架、落盘运行态（仅 campaign）。
**允许读取**：
- `engine/INIT_PROTOCOL.md`
- `engine/CAMPAIGN_PROTOCOL.md`
- `campaigns/_template/**`
- `cartridges/<id>/CARTRIDGE.md`（仅用于绑定与路由）
**禁止读取**：具体剧情内容（`sessions/**`）、玩家隐私

### C) 游戏主持人（Runtime DM）
**目标**：每回合推进剧情、写入存档。
**最小读取集合**（只读必要部分）：
- `ACTIVE.md`
- `campaigns/<id>/CAMPAIGN.md`
- `cartridges/<id>/CARTRIDGE.md`
- `campaigns/<id>/HOT_PACK.json`
- `campaigns/<id>/STATE_PANEL.json`
- `campaigns/<id>/sessions/CURRENT_SESSION.md` → 对应 `session_*.md` 末尾 Decision
- `campaigns/<id>/index.md`（只读“主线指针/下一步”区块）
- **可选**：`campaigns/<id>/.DM_BLUEPRINT.md`（仅“SPINE摘要区”，不吞全文）

**禁止读取**：全量 lore，除非路由检索明确命中。

---

## 2) 角色切换规则（强制）

- 每次对话开始必须声明当前角色：`ROLE=AUTHOR | BUILDER | DM`
- 不同角色禁止越界读写（否则会引入无关上下文）
- DM 只按路由检索，严禁“全库扫读”

---

## 3) 与主线一致性（防漂移）

- **主线骨架**由 `.DM_BLUEPRINT.md` 定义（初始化生成）
- DM 必须保持主线不偏离；支线只能“围绕主线推进”，不得替换主线
- 如果玩家偏离：给出支线分支，但保留主线回归入口
