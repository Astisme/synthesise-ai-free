# Installation

The canonical Agent Skill is in skills/synthesise-ai-free/SKILL.md. Keep its supporting folders alongside it.

## Vercel Skills CLI (recommended)

    npx skills add astisme/synthesise-ai-free

Select a target explicitly:

    npx skills add astisme/synthesise-ai-free --agent codex
    npx skills add astisme/synthesise-ai-free --agent claude-code
    npx skills add astisme/synthesise-ai-free --agent cursor
    npx skills add astisme/synthesise-ai-free --agent github-copilot
    npx skills add astisme/synthesise-ai-free --agent gemini-cli
    npx skills add astisme/synthesise-ai-free --agent opencode
    npx skills add astisme/synthesise-ai-free --agent cline
    npx skills add astisme/synthesise-ai-free --agent roo
    npx skills add astisme/synthesise-ai-free --agent openhands

Agent identifiers and supported targets can change; check npx skills add --help if an identifier is rejected. Global installation depends on the harness.

## Harness notes

| Harness | Recommended route | Notes |
|---|---|---|
| OpenAI Codex | Skills CLI --agent codex | Project-local or global discovery, depending on setup. |
| Claude Code | Skills CLI --agent claude-code | Keep all reference folders. |
| Claude Desktop | Uploadable skill archive, where supported | Archive the complete skill folder, not only SKILL.md. Desktop UI and archive support may vary by release. |
| Cursor | Skills CLI --agent cursor | Project scope is useful for repository work. |
| GitHub Copilot | Skills CLI --agent github-copilot | Confirm the specific Copilot surface supports skills. |
| Gemini CLI | Skills CLI --agent gemini-cli | Keep relative paths intact. |
| OpenCode | Skills CLI --agent opencode | Reload session after installation. |
| Cline | Skills CLI --agent cline | Manual fallback if CLI target is unavailable. |
| Roo Code | Skills CLI --agent roo | Verify identifier against current CLI help. |
| OpenHands | Skills CLI --agent openhands | Support depends on deployment. |
| Windsurf | Manual fallback | Native skills support may vary by version. |
| Other Markdown agents | Universal fallback | Any agent that can read Markdown can use the package. |

These are installation targets, not a guarantee of identical loading behaviour in every product version. Check current harness documentation for version-specific paths.

## Manual universal installation

    mkdir -p .agents/skills
    cp -R skills/synthesise-ai-free .agents/skills/

Copy the entire folder to the agent's documented skills directory. Preserve references, workflows and templates.

## Installer scripts

From repository root:

    bash scripts/install.sh --target .agents/skills

Windows PowerShell:

    .\scripts\install.ps1 -Target .agents\skills

## Claude Desktop archive

Create an archive containing a folder named synthesise-ai-free with SKILL.md and all supporting directories. Import it only through the skill-management interface offered by the current Desktop version. If unavailable, use another supported Agent Skills client. Uploading only SKILL.md loses progressive-disclosure references.

## Verify

    python scripts/validate.py
