# 迷雾边境编年史：瞬变（研究型跑团工程）

![Engine](https://img.shields.io/badge/Engine-Shared-2E86AB?style=flat-square)
![Cartridge](https://img.shields.io/badge/Cartridge-Hot--Swappable-3B8B3B?style=flat-square)
![Campaign](https://img.shields.io/badge/Campaign-Persistent-5C6BC0?style=flat-square)
![RAG](https://img.shields.io/badge/RAG-4x80%20%7C%208%E2%80%9312-8E44AD?style=flat-square)
![Language](https://img.shields.io/badge/Language-中文-555?style=flat-square)

**方法论关键词**：Engine / Cartridge / Campaign  
**目标**：在极小上下文预算下实现稳定推进、可恢复、可热插拔的长期文本跑团。

---

## 0) 结构与入口（统一路径）

| 层级 | 职责 | 位置 |
|------|------|------|
| Engine | 协议/规则/RAG/存档规范 | `engine/`（软链 → `GC_gamer/engine_cn/`） |
| Cartridge | 世界内容库 | `cartridges/<id>/` |
| Campaign | 运行态存档 | `campaigns/<id>/` |

入口指针：`ACTIVE.md`

---

## 1) 快速开始（新战役）

对话指令：`<初始化>`  
入口统一：先读 `engine/System.md` → 执行 `engine/INIT_PROTOCOL.md`  
写入目标：
- `campaigns/<id>/PLAYER_PROFILE.md`
- `campaigns/<id>/characters/PCs/pc_current.md`
- `campaigns/<id>/sessions/`
- `campaigns/<id>/STATE_PANEL.md`
- `campaigns/<id>/HOT_PACK.md`

---

## 2) 创建新卡带 / 新战役

**新卡带（模板起步）**  
复制：`cartridges/template_card/` → `cartridges/<new_card_id>/`  
更新：`CARTRIDGE.md`（routes/aliases/invariants/feature_flags）

**新战役（对话自动化）**  
发送：`<新战役 campaigns/<new_campaign>>`  
AI 自动：创建存档 + 绑定 `cartridge_id`

---

## 3) 热启动与恢复

指令：`<热启动>` 或 `<继续>`  
入口：`engine/System.md` → `engine/HOT_START.md`  
加载顺序：`ACTIVE.md` → `CAMPAIGN.md` → `CARTRIDGE.md` → `HOT_PACK.md`

---

## 4) 热插拔与进度切换

- 新卡带：按第 2 章创建  
- 切换存档：`<切换战役 campaigns/<old_campaign>>` → `<继续>`

---

## 5) 存档与小说同步

**存档**：每回合输出 `ARCHIVE_DELTA`（append/patch）  
**小说**：`Writing/PIPELINE.md` 由 session 决策同步，不参与回合输入

---

## 6) 方法论与设计约束

- 命令头路由：ACT / LOOK / ASK / FIGHT / CAST / MANAGE / OOC  
- RAG 限流：≤4 片段，≤80 字/段，ROUTE_FACTS 8–12  
- 索引摘要：所有索引文件顶部 `RAG_HEAD`  
- 热缓存：`HOT_PACK` ≤100 行  
- Engine 外置共享：`engine_cn` 统一复用
