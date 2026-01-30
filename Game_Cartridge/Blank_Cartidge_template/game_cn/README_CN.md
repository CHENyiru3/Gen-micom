# Blank Cartridge Template (CN)

此模板用于通过 **AI 对话** 快速创建“新卡带 + 新存档”。

## 对话式流程（推荐）

1. **创建新卡带**
   - 复制本模板的卡带目录：
     `cartridges/_template/` → `cartridges/<new_card_id>/`
   - 更新 `CARTRIDGE.md`（routes / aliases / invariants / feature_flags）

2. **创建新存档（战役）**
   - 发送：`<新战役 campaigns/<new_campaign>>`
   - AI 会自动复制存档模板并绑定 `cartridge_id`

3. **初始化开局**
   - 发送：`<初始化>`
   - AI 会按 `engine/INIT_PROTOCOL.md` 写入首批运行态文件

## 模板目录

```
game_cn/
├── cartridges/_template/          # 卡带模板（最小内容索引）
└── campaigns/_template/          # 存档模板（HOT_PACK/STATE_PANEL/sessions/…）
    └── .DM_BLUEPRINT.md          # 主线蓝图（DM Only）
    ├── MAINLINE_PANEL.json         # 主线面板（极短）
    └── clues/CLUE_LOG.json         # 线索日志（与任务分离）
```
