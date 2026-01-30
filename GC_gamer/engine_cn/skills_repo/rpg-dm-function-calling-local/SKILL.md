---
name: rpg-dm-function-calling-local
description: Use the bundled skill tools (tools.json + tools_runner.py) for all structured operations; enforce role tool whitelist; JSON tool_calls only.
---

# Local Function Calling (CN)

## 触发条件
当任务涉及读写存档、路由检索、初始化、切换战役、压缩/快照等结构化操作时，必须使用本技能。

## 技能资源
- 工具定义：`references/tools.json`
- 角色白名单：`references/manifest.json`
- 执行器：`scripts/tools_runner.py`

## 强制规则
- **只输出 JSON tool_calls**，不输出 Markdown 调用或手工编辑说明。
- 角色越权调用视为错误（按 manifest 白名单）。
- 禁止写入 `Blank_Cartidge_template`。

## 最小流程
1. 生成 JSON tool_calls（根据 System_*.md 的角色）。
2. 使用执行器运行：`python3 scripts/tools_runner.py --json tool_calls.json`
3. 读取 tool_results，再继续下一步。

## 例（仅结构）
```json
{
  "tool_calls": [
    {"name": "route_lookup", "arguments": {"routes_path": "cartridges/card_x/ROUTES.md", "command_head": "[LOOK]"}},
    {"name": "fetch_facts", "arguments": {"paths": ["locations/LOCATION_INDEX.md"], "limit": 10}}
  ]
}
```
