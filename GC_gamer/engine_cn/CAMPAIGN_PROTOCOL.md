# CAMPAIGN_PROTOCOL.md — 新建/切换战役（prompt 工程化流程）

> **目标**：把“开新战役/切换战役”变成可重复、低出错的流程，并与热启动/增量存档完全兼容。

---

## 0) 目录与真源

- Engine（共享）：`engine/`（协议/机制/脚本）
- Cartridge（世界内容）：`cartridges/<cartridge_id>/`
- Template 卡带：`Game_Cartridge/Blank_Cartidge_template/game_cn/cartridges/_template/`（仅模板，不可直接写入）
- Template 存档：`Game_Cartridge/Blank_Cartidge_template/game_cn/campaigns/_template/`（仅模板，不可直接写入）
- Campaign（存档）：`Game_Cartridge/<cartridge_root>/game_cn/campaigns/<campaign_id>/`
- 当前战役指针：`ACTIVE.md`

**强制规则**：
- 新卡带必须创建在 **独立目录**：`Game_Cartridge/<cartridge_root>/game_cn/`
- 任何 `card_*` / 新卡带 **不得**创建在 `Blank_Cartidge_template` 内

---

## 1) 自动化方式（推荐）

使用脚本：

```bash
python3 engine/scripts/campaign_manager.py new --id campaign_0002
python3 engine/scripts/campaign_manager.py switch --path campaigns/campaign_0001
```

> 注意：脚本在当前卡带根目录下运行（`Game_Cartridge/<cartridge_root>/game_cn/`）。  
> 禁止在 `Blank_Cartidge_template` 下创建新战役。

### 用户无需运行脚本（对话式控制）

如果你在和 AI 对话，推荐直接发：
- `<新战役 campaign_0002>`
- `<切换战役 campaigns/campaign_0001>`

AI 会在后台执行脚本，并完成 `ACTIVE.md` 的更新。

---

## 2) 纯 prompt 手工方式（无脚本场景）

当用户说“新开战役”时，DM 必须按顺序执行（内部/工具层完成）：

1. 在 **独立卡带根目录** 下复制模板  
   `Game_Cartridge/Blank_Cartidge_template/game_cn/campaigns/_template`  
   → `Game_Cartridge/<cartridge_root>/game_cn/campaigns/<new_id>`
2. 更新 `ACTIVE.md` 为新路径
3. 更新新战役的 `CAMPAIGN.md`（cartridge_id/版本锁）
4. 运行 `<初始化>`（按 `engine/INIT_PROTOCOL.md` 完成落盘）

失败时：宁可停在“未切换成功”也不要写错 `ACTIVE.md`。
