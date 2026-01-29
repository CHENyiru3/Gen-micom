# RAG_ENGINE.md — 路由检索与碎片事实

## 目的
- 用命令头路由检索范围，限制上下文大小。
- 只抽取碎片事实（8-12条，每条≤16字）。

## 输入
- 玩家输入（必须含命令头）
- cartridges/<id>/CARTRIDGE.md 的 routes
- campaigns/<id>/HOT_PACK.md
- campaigns/<id>/index.md（只取顶部快照）

## 输出
- ROUTE_FACTS（8-12条）
- 参与检索的文件清单

## 规则
1) 依据命令头选择 routes 列表。
2) 只读取索引/摘要/条目头部，不吞全文。
3) 每次最多 4 个文件片段，每段≤80字。
4) 优先读取：*_INDEX.md / *_roster.md / QUEST_LOG.md 的表头与首段。
5) 与 engine/mechanics/RAG_RULES.md 一致，若冲突以该文件为准。

## 失败处理
- 未知命令头：返回错误提示 + 可用命令头列表 + 1条示例。
- 目标文件缺失：记录到 ARCHIVE_DELTA 的 risk_flag。

## 长度限制
- ROUTE_FACTS：8-12条，每条≤16字。
- HOT_PACK：≤100行。
