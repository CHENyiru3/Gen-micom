# CAMPAIGN_PROTOCOL.md — 新建/切换战役（prompt 工程化流程）

> **目标**：把“开新战役/切换战役”变成可重复、低出错的流程，并与热启动/增量存档完全兼容。

---

## 0) 目录与真源

- Engine（共享）：`engine/`（协议/机制/脚本）
- Cartridge（世界内容）：`cartridges/<cartridge_id>/`
- Template 卡带：`cartridges/template_card/`（所有新卡带的起点）
- Campaign（存档）：`campaigns/<campaign_id>/`
- 当前战役指针：`ACTIVE.md`

---

## 1) 自动化方式（推荐）

使用脚本：

```bash
python3 engine/scripts/campaign_manager.py new --id campaign_0002
python3 engine/scripts/campaign_manager.py switch --path campaigns/campaign_0001
```

### 用户无需运行脚本（对话式控制）

如果你在和 AI 对话，推荐直接发：
- `<新战役 campaign_0002>`
- `<切换战役 campaigns/campaign_0001>`

AI 会在后台执行脚本，并完成 `ACTIVE.md` 的更新。

---

## 2) 纯 prompt 手工方式（无脚本场景）

当用户说“新开战役”时，DM 必须按顺序执行（内部/工具层完成）：

1. 复制模板 `campaigns/_template` → `campaigns/<new_id>`
2. 更新 `ACTIVE.md` 为新路径
3. 更新新战役的 `CAMPAIGN.md`（cartridge_id/版本锁）
4. 运行 `<初始化>`（按 `engine/INIT_PROTOCOL.md` 完成落盘）

失败时：宁可停在“未切换成功”也不要写错 `ACTIVE.md`。
