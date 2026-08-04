# mirror.ps1 — bidirectional sync orchestrator (Windows <-> vmi)
#
# Usage:
#   mirror.ps1                          # incremental sync, priority 1 only (fast)
#   mirror.ps1 -Full                    # all priorities (slower, used by 30-min task)
#   mirror.ps1 -Init                    # FIRST RUN ONLY — runs --resync (Windows wins)
#   mirror.ps1 -DryRun                  # show what would change, don't actually sync
#   mirror.ps1 -Pair karim-site         # sync only one pair
#   mirror.ps1 -Quiet                   # no console output (used by triggers)
#
# Pairs config:    ~/.claude/scripts/mirror-pairs.txt
# Filter files:    ~/.claude/scripts/mirror-filters/*.txt
# Lock file:       ~/.claude/mirror.lock          (prevents concurrent runs)
# Debounce file:   ~/.claude/mirror.lastrun       (skips if last run < $DebounceSeconds ago)
# Log:             ~/.claude/logs/mirror.log
# Conflict files:  *.conflict_<DateMs> on either side (newer wins, loser preserved)

[CmdletBinding()]
param(
  [switch] $Full,
  [switch] $Init,
  [switch] $DryRun,
  [string] $Pair,
  [switch] $Quiet,
  [int] $DebounceSeconds = 120
)

$ErrorActionPreference = "Stop"

$Root         = "$env:USERPROFILE\.claude"
$Rclone       = "$Root\bin\rclone.exe"
$Config       = "$Root\rclone.conf"
$PairsFile    = "$Root\scripts\mirror-pairs.txt"
$FiltersDir   = "$Root\scripts\mirror-filters"
$LogFile      = "$Root\logs\mirror.log"
$LockFile     = "$Root\mirror.lock"
$LastRunFile  = "$Root\mirror.lastrun"
$WorkDirBase  = "$Root\.rclone-bisync"

if (-not (Test-Path "$Root\logs")) { New-Item -ItemType Directory -Path "$Root\logs" | Out-Null }
if (-not (Test-Path $WorkDirBase))  { New-Item -ItemType Directory -Path $WorkDirBase | Out-Null }

# Rotate at 50 MB, keep one generation. A failing bisync logs every file it sees;
# on 2026-07-22 that grew this log to 13.9 GB and filled C:.
if (Test-Path $LogFile) {
  if ((Get-Item $LogFile).Length -gt 50MB) {
    Move-Item -Path $LogFile -Destination "$LogFile.1" -Force -ErrorAction SilentlyContinue
  }
}

function Write-MirrorLog($msg) {
  $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $msg
  Add-Content -Path $LogFile -Value $line
  if (-not $Quiet) { Write-Host $line }
}

function Acquire-Lock {
  if (Test-Path $LockFile) {
    $lockAge = (Get-Date) - (Get-Item $LockFile).LastWriteTime
    if ($lockAge.TotalMinutes -lt 30) {
      Write-MirrorLog "lock held (age=$([int]$lockAge.TotalSeconds)s), skipping"
      return $false
    }
    Write-MirrorLog "stale lock ($([int]$lockAge.TotalMinutes)m), forcing"
  }
  $PID | Set-Content -Path $LockFile
  return $true
}

function Release-Lock {
  Remove-Item -Path $LockFile -ErrorAction SilentlyContinue
}

function Should-DebounceSkip {
  if ($Init -or $Full -or $Pair) { return $false }
  if (-not (Test-Path $LastRunFile)) { return $false }
  $age = (Get-Date) - (Get-Item $LastRunFile).LastWriteTime
  if ($age.TotalSeconds -lt $DebounceSeconds) {
    Write-MirrorLog ("debounce: last run {0}s ago < {1}s, skip" -f [int]$age.TotalSeconds, $DebounceSeconds)
    return $true
  }
  return $false
}

function Touch-LastRun {
  (Get-Date).ToString("o") | Set-Content -Path $LastRunFile
}

function Read-Pairs {
  $lines = Get-Content $PairsFile | Where-Object { $_ -and ($_ -notmatch '^\s*#') }
  $pairs = @()
  foreach ($line in $lines) {
    $parts = $line -split '\s*\|\s*'
    if ($parts.Count -lt 4) { continue }
    $pairs += [PSCustomObject]@{
      Local    = $parts[0].Trim()
      Remote   = "vmi:" + $parts[1].Trim()
      Filter   = "$FiltersDir\$($parts[2].Trim())"
      Priority = [int]$parts[3].Trim()
      Name     = (Split-Path -Leaf $parts[0].Trim())
    }
  }
  return $pairs
}

function Sync-Pair($item) {
  $name = $item.Name
  if ($Pair -and $name -ne $Pair) { return }

  if (-not (Test-Path $item.Local)) {
    Write-MirrorLog "[$name] local missing ($($item.Local)), creating"
    New-Item -ItemType Directory -Path $item.Local -Force | Out-Null
  }
  if (-not (Test-Path $item.Filter)) {
    Write-MirrorLog "[$name] FILTER MISSING: $($item.Filter), skipping"
    return
  }

  # Ensure the remote dir exists on vmi (rclone bisync --resync needs both sides present).
  if ($Init) {
    $remotePath = $item.Remote -replace '^vmi:', ''
    & $Rclone mkdir $item.Remote --config $Config 2>$null | Out-Null
    Write-MirrorLog "[$name] ensured remote dir exists: $($item.Remote)"
  }

  $workdir = "$WorkDirBase\$name"
  if (-not (Test-Path $workdir)) { New-Item -ItemType Directory -Path $workdir | Out-Null }

  $args = @(
    "bisync",
    $item.Local,
    $item.Remote,
    "--config", $Config,
    "--filter-from", $item.Filter,
    "--workdir", $workdir,
    "--conflict-resolve", "newer",
    "--conflict-suffix", "conflict_{DateMs}",
    "--conflict-loser", "pathname",
    "--resilient",
    "--recover",
    "--max-lock", "20m",
    "--transfers", "4",
    "--checkers", "8",
    "--copy-links",
    "--ignore-errors",
    "--log-file", $LogFile,
    "--log-level", "NOTICE"
  )

  if ($Init)   { $args += "--resync"; $args += "--resync-mode"; $args += "path1" }
  if ($DryRun) { $args += "--dry-run" }

  Write-MirrorLog "[$name] start (Init=$Init Full=$Full DryRun=$DryRun)"
  $start = Get-Date
  & $Rclone @args
  $rc = $LASTEXITCODE
  $secs = [int]((Get-Date) - $start).TotalSeconds
  Write-MirrorLog "[$name] end rc=$rc duration=${secs}s"
}

# --- main ---
if (Should-DebounceSkip) { exit 0 }
if (-not (Acquire-Lock))  { exit 0 }
try {
  Write-MirrorLog "=== mirror start (Init=$Init Full=$Full DryRun=$DryRun Pair=$Pair) ==="
  $pairs = Read-Pairs
  Write-MirrorLog "parsed $($pairs.Count) pair(s) from $PairsFile"
  foreach ($p in $pairs) { Write-MirrorLog "  - name=$($p.Name) prio=$($p.Priority) local=$($p.Local) remote=$($p.Remote)" }
  $maxPriority = if ($Full -or $Init -or $Pair) { 99 } else { 1 }
  foreach ($p in $pairs | Where-Object { $_.Priority -le $maxPriority }) {
    Sync-Pair $p
  }
  Touch-LastRun
  Write-MirrorLog "=== mirror done ==="
} finally {
  Release-Lock
}
