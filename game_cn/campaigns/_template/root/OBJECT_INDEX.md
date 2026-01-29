# OBJECT_INDEX.md — 活跃对象索引（热缓存，避免多文件扫描）

> **用途**：把“当前回合/当前会话真正需要的对象”压成一页索引，供热启动与每回合最小读取。  
> **规则**：只存“指针 + 1 行摘要”；详情仍在对象文件中（NPC/Quest/Location/Map）。

---

## Active Session

- current: `sessions/CURRENT_SESSION.md`

---

## Active PC

- pc: `characters/PCs/pc_current.md` — （未初始化）
- pet: `characters/PCs/pet_current.md` — （可选）

---

## Active Location Targets

- (none)

---

## Active Quests

- (none)

---

## Active NPCs

- (none)

---

## Active Maps (optional)

- index: `maps/MAP_INDEX.md`
- (none)

---

## Notes

- 本文件每回合用 `ARCHIVE_DELTA` patch 更新（不要重写整页）。

