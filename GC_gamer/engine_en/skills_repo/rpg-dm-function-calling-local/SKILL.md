---
name: rpg-dm-function-calling-local
description: Use the bundled skill tools (tools.json + tools_runner.py) for all structured operations; enforce role tool whitelist; JSON tool_calls only.
---

# Local Function Calling (EN)

## Trigger
Use this skill whenever tasks require structured reads/writes, routing, init/switch, snapshot/compress.

## Skill Resources
- Tool schemas: `references/tools.json`
- Role whitelist: `references/manifest.json`
- Runner: `scripts/tools_runner.py`

## Hard Rules
- **Output JSON tool_calls only**, no Markdown calls.
- Role tool use must follow manifest whitelist.
- Never write into `Blank_Cartidge_template`.

## Minimal Flow
1. Emit JSON tool_calls (per System_*.md role).
2. Run: `python3 scripts/tools_runner.py --json tool_calls.json`
3. Read tool_results and continue.

## Example (structure only)
```json
{
  "tool_calls": [
    {"name": "route_lookup", "arguments": {"routes_path": "cartridges/card_x/ROUTES.md", "command_head": "[LOOK]"}},
    {"name": "fetch_facts", "arguments": {"paths": ["locations/LOCATION_INDEX.md"], "limit": 10}}
  ]
}
```
