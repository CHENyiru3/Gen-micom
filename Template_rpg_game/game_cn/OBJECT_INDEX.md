# OBJECT_INDEX.md — 活跃对象索引（热缓存，避免多文件扫描）

> **用途**：将"本回合/本会话真正需要的对象"压缩为一个索引页面，用于热启动和最小化每回合读取。
> **规则**：只存储"指针 + 1 行摘要"；详情保留在对象文件（NPC/任务/地点/地图）中。

---

## 活跃会话

- current: `sessions/CURRENT_SESSION.md`

---

## 活跃 PC

- pc: `characters/PCs/pc_current.md` — （未初始化）
- pet: `characters/PCs/pet_current.md` — （可选）

---

## 活跃地点目标

- （无）

---

## 活跃任务

- （无）

---

## 活跃 NPC

- （无）

---

## 活跃地图（可选）

- index: `maps/MAP_INDEX.md`
- （无）

---

## 备注

- 本文件通过每回合 `ARCHIVE_DELTA` patch 更新（不要重写整个页面）。
