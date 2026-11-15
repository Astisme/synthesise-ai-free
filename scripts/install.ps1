param([string]$Target = ".agents/skills", [switch]$Force)
$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$Source = Join-Path $RepoRoot "skills/synthesise-ai-free"
$Destination = Join-Path $Target "synthesise-ai-free"
if (-not (Test-Path (Join-Path $Source "SKILL.md"))) { throw "Canonical SKILL.md not found: $Source" }
New-Item -ItemType Directory -Force -Path $Target | Out-Null
if ((Test-Path $Destination) -and -not $Force) { throw "Destination exists: $Destination (use -Force to replace)" }
if (Test-Path $Destination) { Remove-Item -Recurse -Force $Destination }
Copy-Item -Recurse $Source $Destination
Write-Output "Installed Synthesise AI Free to: $Destination"
