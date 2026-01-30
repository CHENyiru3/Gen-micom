# skills_repo

This directory stores **skills that can be installed at Codex system level** (stable kernel protocols/workflows), decoupled from story content.

## Skill List

- `rpg-dm-kernel-protocol`: RPG kernel protocols (HOT/WARM/COLD, HUD short codes, RAG minimal load, ARCHIVE_DELTA incremental archive)
- `rpg-dm-content-pack-authoring`: Content pack authoring (cartridges lore/NPC/quests/locations), does not change kernel
- `rpg-dm-fiction-sync`: Session→novel synchronization (does not create new Canon)
- `rpg-dm-maps`: Map content pack maintenance (triad: render/data/logic + fog-of-war + version)
- `rpg-dm-governance-panel`: Governance panel maintenance (assets/followers/army/income/governance clocks)
- `rpg-dm-function-calling-local`: Local function calling (JSON tool_calls + role whitelist + tools_runner)

## Installation Methods (Choose One)

### A) Direct Copy (Simplest Local)

Copy the corresponding skill directory to: `~/.codex/skills/`

For example:
- `skills_repo/rpg-dm-kernel-protocol` → `~/.codex/skills/rpg-dm-kernel-protocol`

### B) Use skill-installer (Install from GitHub Repository)

After pushing the entire repo to GitHub, can install by "path":
- repo: `<owner>/<repo>`
- path: `skills_repo/rpg-dm-kernel-protocol` (or other skill directory)

After installation, need to **Restart Codex** to load new skills.
