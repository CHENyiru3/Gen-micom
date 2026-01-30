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

使用 JSON tool_calls（推荐）：

```json
{
  "tool_calls": [
    {"name": "copy_template", "arguments": {"src": "Game_Cartridge/Blank_Cartidge_template/game_cn/campaigns/_template", "dst": "Game_Cartridge/<cartridge_root>/game_cn/campaigns/<new_id>"}},
    {"name": "bind_campaign", "arguments": {"campaign_path": "Game_Cartridge/<cartridge_root>/game_cn/campaigns/<new_id>", "cartridge_id": "<new_card_id>", "version_lock": "1.0.x"}},
    {"name": "set_active", "arguments": {"campaign_path": "Game_Cartridge/<cartridge_root>/game_cn/campaigns/<new_id>"}}
  ]
}
```

### 用户无需运行脚本（对话式控制）

如果你在和 AI 对话，推荐直接发：
- `<新战役 campaign_0002>`
- `<切换战役 campaigns/campaign_0001>`

AI 会在后台执行脚本，并完成 `ACTIVE.md` 的更新。

---

## 2) 纯 prompt 手工方式（无脚本场景）

当用户说“新开战役”时，DM 必须按顺序输出 JSON tool_calls：

1. `copy_template`
2. `bind_campaign`
3. `set_active`
4. `init_campaign`（按 `engine/INIT_PROTOCOL.md` 完成落盘）

失败时：宁可停在“未切换成功”也不要写错 `ACTIVE.md`。
