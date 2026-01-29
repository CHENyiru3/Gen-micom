# GC_gamer — Engine Infrastructure

This repo hosts the shared RPG engine layer (protocols, CLI, RAG, save specs, scripts).

Engine root:
- `engine/`

Cartridge repos should link to this engine (symlink or submodule) so that:
- Engine stays stable and shared.
- Cartridges only store world content + campaigns.
