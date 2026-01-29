# skills_repo

This directory stores **installable skills at the Codex system level** (stable kernel protocols/workflows), decoupled from narrative content.

## Skill List

- `rpg-dm-kernel-protocol`: RPG kernel protocol (HOT/WARM/COLD, HUD shortcodes, minimal RAG, ARCHIVE_DELTA incremental saves)
- `rpg-dm-content-pack-authoring`: Content pack authoring (lore/NPC/quests/locations/sessions/state), without modifying kernel
- `rpg-dm-fiction-sync`: Session-to-novel synchronization (does not produce new Canon)
- `rpg-dm-maps`: Map content pack maintenance (triad: render/data/logic + fog-of-war + versioning)
- `rpg-dm-governance-panel`: Governance panel maintenance (assets/followers/army/income/governance clocks)
- `rpg-dm-campaign-manager`: Campaign management (create/switch/init campaigns)

## Installation (Choose One)

### A) Direct Copy (Simplest Local)

Copy the skill directory to: `~/.codex/skills/`

For example:
- `skills_repo/rpg-dm-kernel-protocol` → `~/.codex/skills/rpg-dm-kernel-protocol`

### B) Using skill-installer (Install from GitHub Repo)

After pushing the entire repo to GitHub, install by path:
- repo: `<owner>/<repo>`
- path: `skills_repo/rpg-dm-kernel-protocol` (or other skill directory)

After installation, **Restart Codex** to load new skills.
