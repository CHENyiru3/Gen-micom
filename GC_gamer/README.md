# GC_gamer — Engine Infrastructure

This repo hosts the shared RPG engine layer (protocols, CLI, RAG, save specs, scripts).

Engine roots:
- `engine_cn/` (current)
- `engine_en/` (future)

Cartridge repos should link to `engine_cn/` (symlink or submodule) so that:
- Engine stays stable and shared.
- Cartridges only store world content + campaigns.

Local function-calling:
- Tool schemas: `engine_cn/tools/tools.json`
- Runner: `engine_cn/scripts/tools_runner.py`
