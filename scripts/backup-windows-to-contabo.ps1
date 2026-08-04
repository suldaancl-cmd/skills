# Authoritative Windows -> Contabo backup. Sources from C: directly, KEEPS .git,
# excludes node_modules + regenerable caches + secrets. Resumable (rclone skips existing).
$ErrorActionPreference = 'Continue'
$rc   = "$env:LOCALAPPDATA\Microsoft\WinGet\Links\rclone.exe"
$dest = "contabo:contabo/backup/2026-07-23/windows"
$H    = $env:USERPROFILE

$excl = @(
  'node_modules/**','.venv/**','venv/**','__pycache__/**','.cache/**','.next/**','dist/**',
  'build/**','out/**','.turbo/**','target/**','coverage/**','.pytest_cache/**','.expo/**',
  '*.log','ms-playwright/**','Cache/**','CachedData/**',
  # secrets — never to cloud
  '.env','*.env','keys.env','api_keys.json','*token*','*credential*','*.pem','*.key',
  'id_rsa*','id_ed25519*','*oauth*','*.p12'
)
$exArgs = @(); foreach($e in $excl){ $exArgs += '--exclude'; $exArgs += $e }

# root -> dest-subfolder  (huge regenerable dot-dirs deliberately omitted)
$map = [ordered]@{
  "$H\.claude\skills"        = 'claude-skills'
  "$H\.claude\projects"      = 'claude-projects'
  "$H\.claude\_projects"     = 'claude-_projects'
  "$H\.claude\plugins"       = 'claude-plugins'
  "$H\.claude\snapshots"     = 'claude-snapshots'
  "$H\.claude\notion-backup" = 'notion-backup'
  "$H\.claude\hooks"         = 'claude-config/hooks'
  "$H\.claude\scripts"       = 'claude-config/scripts'
  "$H\.codex"                = 'codex'
  "$H\.agents"               = 'agents-lib/.agents'
  "$H\.adal"                 = 'agents-lib/.adal'
}

foreach($src in $map.Keys){
  if(-not (Test-Path $src)){ Write-Host "SKIP (missing): $src"; continue }
  Write-Host "=== $src -> $($map[$src]) ($(Get-Date -Format HH:mm:ss)) ==="
  & $rc copy $src "$dest/$($map[$src])" @exArgs --transfers 8 --checkers 16 --fast-list --stats 60s --stats-one-line 2>&1 | Select-Object -Last 1
}

# loose top-level .claude config files
& $rc copy "$H\.claude" "$dest/claude-config" --include 'CLAUDE.md' --include 'settings.json' --include 'settings.local.json' --include 'skill-routes.json' --include '*.jsonl' --max-depth 1 2>&1 | Select-Object -Last 1

# home project folders (non-dot, non-system) — keep .git, drop node_modules
$sys = 'AppData','Application Data','Contacts','Cookies','Desktop','Documents','Downloads',
       'Favorites','Links','Local Settings','My Documents','NetHood','OneDrive','PrintHood',
       'Recent','Saved Games','Searches','SendTo','Start Menu','Templates','IntelGraphicsProfiles',
       'node_modules','Videos','Music','Pictures','_projects'
Get-ChildItem $H -Directory -Force -EA SilentlyContinue |
  Where-Object { $_.Name -notlike '.*' -and $_.Name -notin $sys -and -not $_.LinkTarget } |
  ForEach-Object {
    & $rc copy $_.FullName "$dest/home-projects/$($_.Name)" @exArgs --transfers 8 --checkers 16 --stats 120s --stats-one-line 2>&1 | Select-Object -Last 1
  }

Write-Host "=== agent config dot-dirs (keep .git, drop caches/secrets) ==="
$skipDot = '.npm-cache','.vscode','.u2net','.local','.git','.m2','.npm','.cache','.thumbnails','.claude','.codex','.agents','.adal'
Get-ChildItem $H -Directory -Force -EA SilentlyContinue |
  Where-Object { $_.Name -like '.*' -and $_.Name -notin $skipDot -and -not $_.LinkTarget } |
  ForEach-Object {
    & $rc copy $_.FullName "$dest/agent-configs/$($_.Name)" @exArgs --transfers 8 --checkers 16 2>&1 | Select-Object -Last 1
  }

Write-Host "=== WINDOWS BACKUP DONE $(Get-Date -Format HH:mm:ss) ==="
& $rc size $dest 2>&1 | Select-Object -Last 2
