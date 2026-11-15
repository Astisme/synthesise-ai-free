# Installation

Synthesise AI Free has one canonical skill package at `skills/synthesise-ai-free/`. Installation follows the per-agent approach used by mature skill repositories: use each harness's native plugin/marketplace mechanism where available, and use the Skills CLI as a portable fallback.

**Choose one installation route per agent.** Do not install both the native plugin and the standalone skill into the same agent, or the skill may appear twice.

## Claude Code — native plugin marketplace

```bash
claude plugin marketplace add Astisme/synthesise-ai-free
claude plugin install synthesise-ai-free@synthesise-ai-free
```

Or run `/plugin marketplace add Astisme/synthesise-ai-free` and then `/plugin install synthesise-ai-free@synthesise-ai-free` inside a Claude Code session.

Manage it with `claude plugin list`, `claude plugin update synthesise-ai-free@synthesise-ai-free`, and `claude plugin uninstall synthesise-ai-free@synthesise-ai-free`. For the modular preview, install `synthesise-v2-preview@synthesise-ai-free` instead. The stable and preview entries remain separate. The plugin marketplace manifest lives in `.claude-plugin/marketplace.json`.

## OpenAI Codex — native plugin marketplace

```bash
codex plugin marketplace add Astisme/synthesise-ai-free
codex plugin marketplace upgrade
codex plugin marketplace list
```

Then open the Plugins Directory in the ChatGPT desktop app, select the Synthesise AI Free marketplace, and install either `synthesise-ai-free` (stable v1) or `synthesise-v2-preview` (modular preview). The repository catalog is `.agents/plugins/marketplace.json`; the v2 package is a Git subdirectory at `skills/` with its own portable `plugin.json`. The current documented repo-marketplace flow uses the desktop Plugins Directory for installation rather than a `codex plugin add` CLI command.

## Gemini CLI — native skill install

```bash
gemini skills install https://github.com/Astisme/synthesise-ai-free.git --path skills/synthesise-ai-free
```

Run the same command again to update the skill.

## Skills CLI — other compatible agents

For Cursor, OpenCode, Windsurf, and other agents supported by the Vercel Skills CLI:

```bash
npx skills@latest add Astisme/synthesise-ai-free -a cursor
```

Replace `cursor` with the relevant agent identifier. Omit `-a` to choose interactively. Agent identifiers and support evolve; check `npx skills@latest add --help` for the current list.

Update installed skills with:

```bash
npx skills@latest update
```

Re-run `add` to select newly published skills. If a target is not supported by the CLI, use the manual fallback below.

## Harness compatibility matrix

| Harness | Preferred route | Update approach |
|---|---|---|
| OpenAI Codex | Native plugin marketplace | `codex plugin marketplace upgrade`; inspect plugin updates in Codex |
| Claude Code | Native plugin marketplace | `claude plugin update synthesise-ai-free@synthesise-ai-free` |
| Claude Desktop | Upload complete skill archive where supported | Re-import updated archive |
| Cursor | Skills CLI | `npx skills@latest update` |
| GitHub Copilot CLI | Native plugin marketplace | `copilot plugin update synthesise-ai-free` |
| Gemini CLI | Native skill install | Re-run `gemini skills install` |
| OpenCode | Skills CLI | `npx skills@latest update` |
| Cline | Skills CLI if supported; otherwise manual fallback | Re-run relevant installer / replace copied folder |
| Roo Code | Skills CLI if supported; otherwise manual fallback | Re-run relevant installer / replace copied folder |
| OpenHands | Skills CLI if supported; otherwise manual fallback | Re-run relevant installer / replace copied folder |
| Windsurf | Skills CLI if supported; otherwise manual fallback | Re-run relevant installer / replace copied folder |
| Other Markdown agents | Manual fallback | Pull latest files and copy skill directory |

This matrix describes intended distribution routes, not a guarantee that every release of each harness has identical feature support. Verify current harness documentation and CLI help before installing.

## Claude Desktop uploadable package

For Claude Desktop versions that support uploaded skills, create an archive containing the complete `skills/synthesise-ai-free/` folder. Preserve `SKILL.md`, `references/`, `workflows/`, `templates/` and `examples/`. Import it through the skill-management interface offered by your version of Claude Desktop. If skill upload is unavailable, use Claude Code or another compatible agent.

## Manual universal installation

For any agent that reads Markdown skills, clone the repository and copy the complete canonical skill directory into its documented skills folder:

```bash
git clone https://github.com/Astisme/synthesise-ai-free.git
mkdir -p .agents/skills
cp -R synthesise-ai-free/skills/synthesise-ai-free .agents/skills/
```

The expected result is:

```text
.agents/skills/synthesise-ai-free/
├── SKILL.md
├── references/
├── workflows/
├── templates/
└── examples/
```

## Repository installer scripts

The repository also includes simple copy-based installers for environments where the user wants an explicit local install rather than a plugin marketplace:

```bash
bash scripts/install.sh --target .agents/skills
```

Windows PowerShell:

```powershell
.\\scripts\\install.ps1 -Target .agents\\skills
```

These scripts do not register marketplaces or manage updates. Pull the latest repository and rerun the installer to refresh the copied files. Use `--force` (Bash) or `-Force` (PowerShell) to replace an existing installation. The Bash and PowerShell copy, overwrite-protection and forced-update behaviours are covered by automated regression tests in CI.

## Verify

```bash
python scripts/validate.py
```

The validator checks the canonical skill structure and its local references.

## Modular v2.0.0 alpha preview (separate install channel)

The modular packages are available as a manual preview installation. This route does not change the stable v1.1.0 plugin identities or installer scripts.

From a repository clone, install all eleven v2 packages alongside any existing v1 installation:

```bash
python scripts/install_v2_preview.py --target .agents/skills
```

Install one package only:

```bash
python scripts/install_v2_preview.py --target .agents/skills --package synthesise-orchestrator
```

Verify a complete installation, or one selected package, without modifying the target:

```bash
python scripts/install_v2_preview.py --target .agents/skills --verify
python scripts/install_v2_preview.py --target .agents/skills --package synthesise-orchestrator --verify
```

Verification checks the install manifest, tracked package directories, skill identities and installed versions. Full verification also rejects untracked v2 package directories and duplicate skill identities. It is read-only and does not inspect or modify the stable v1 package.

The installer writes a `.synthesise-v2-preview.json` manifest, refuses unmanaged destination collisions, detects duplicate skill identities, and can resume a partial installation by rerunning the same command. A managed package at a different version requires `--force` to upgrade. Use `--remove` to remove all preview packages, or combine it with `--package` to remove one package:

```bash
python scripts/install_v2_preview.py --target .agents/skills --remove
python scripts/install_v2_preview.py --target .agents/skills --package synthesise-orchestrator --remove
```

The preview installer is cross-platform Python and never deletes or upgrades `synthesise-ai-free/`. The original `scripts/install.sh` and `scripts/install.ps1` remain v1-only. This installer is a local file-copy mechanism; it does not register native plugins, prove that a harness discovers the skills, or enable automatic cross-skill invocation.

## Native modular v2 preview packages

The v2 preview is published as a separate plugin entry; it does not replace the v1 plugin:

- Claude Code: `claude plugin install synthesise-v2-preview@synthesise-ai-free`
- Codex: add/upgrade the repository marketplace, then install `synthesise-v2-preview` from the ChatGPT desktop Plugins Directory

The Codex Git-backed marketplace entry uses `git-subdir` to resolve the plugin root at `./skills`. The plugin manifest explicitly lists the orchestrator and ten specialist directories, excluding the v1 canonical skill. The Claude Code plugin manifest uses the same package root and explicit skill paths. See [native plugin distribution](native-plugin-distribution.md) for the layout, verification steps and current limitations.

For a controlled evaluation alongside an existing v1 installation, see the [v1-to-v2 preview migration guide](v2-migration-guide.md). It covers project continuity, acceptance checks and rollback without implying automatic project conversion.
