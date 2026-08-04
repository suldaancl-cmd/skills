# git-history-backup.ps1 — back up ONLY unique unpushed git work as bundles.
#
# "Unique unpushed work" = commits on local branches not reachable from ANY
# remote-tracking ref (git rev-list --branches --not --remotes). So:
#   - repo fully pushed to its remote        -> skipped (already safe on the remote)
#   - repo with local commits ahead of remote-> bundle only those commits (thin/incremental)
#   - repo with no remote at all             -> whole history is unpushed, bundled in full
#
# Usage:
#   git-history-backup.ps1                    # back up default roots
#   git-history-backup.ps1 -DryRun            # show what would be bundled, write nothing
#   git-history-backup.ps1 -Roots C:\a,C:\b   # override which trees to scan
#   git-history-backup.ps1 -SelfCheck         # run the predicate self-test and exit

[CmdletBinding()]
param(
  # ponytail: env-specific knob — a repo path, or a container of depth-1 repos.
  # .claude is itself a repo (no remote); the rest are project containers.
  [string[]] $Roots = @(
    "$env:USERPROFILE\.claude",
    "$env:USERPROFILE\.claude\_projects",
    "$env:USERPROFILE\.claude\saas",
    "$env:USERPROFILE\.claude\karim-new-sites"
  ),
  [string]   $Dst = "$env:USERPROFILE\claude-backups\git-history",
  [switch]   $DryRun,
  [switch]   $SelfCheck
)

$ErrorActionPreference = "Stop"

# Number of commits on local branches that no remote-tracking ref can reach.
function Get-UnpushedCount([string]$repo) {
  $n = & git -C $repo rev-list --count --branches --not --remotes 2>$null
  if ($LASTEXITCODE -ne 0 -or -not $n) { return 0 }
  return [int]$n
}

# Emit every repo reachable from a root, without deep-recursing (.claude holds
# gigabytes of nested trees). Two complementary sources, deduped by the caller:
#   (a) the repo that CONTAINS the root — catches roots whose .git lives in a
#       parent (e.g. .claude is tracked by the C:\Users\user HOME repo, so its
#       .git is NOT at .claude\.git).
#   (b) independent repos one level down — catches nested clones/worktrees whose
#       own .git (dir or file) sits inside a container like _projects\.
function Find-Repos([string]$root) {
  if (-not (Test-Path $root)) { return }
  $top = & git -C $root rev-parse --show-toplevel 2>$null
  if ($LASTEXITCODE -eq 0 -and $top) { $top }
  Get-ChildItem -Path $root -Directory -Force -ErrorAction SilentlyContinue |
    Where-Object { Test-Path (Join-Path $_.FullName ".git") } |
    ForEach-Object { $_.FullName }
}

if ($SelfCheck) {
  $t = Join-Path ([IO.Path]::GetTempPath()) ("ghb-selfcheck-" + [guid]::NewGuid())
  New-Item -ItemType Directory -Force -Path $t | Out-Null
  try {
    & git -C $t init -q
    & git -C $t config user.email t@t; & git -C $t config user.name t
    "a" | Set-Content (Join-Path $t a.txt); & git -C $t add -A; & git -C $t commit -qm one
    if ((Get-UnpushedCount $t) -ne 1) { throw "expected 1 unpushed before push" }
    & git -C $t update-ref refs/remotes/origin/master HEAD     # simulate a push
    if ((Get-UnpushedCount $t) -ne 0) { throw "expected 0 unpushed after push" }
    "b" | Set-Content (Join-Path $t b.txt); & git -C $t add -A; & git -C $t commit -qm two
    if ((Get-UnpushedCount $t) -ne 1) { throw "expected 1 unpushed after new local commit" }
    Write-Host "SelfCheck OK"
  } finally { Remove-Item -Recurse -Force $t -ErrorAction SilentlyContinue }
  exit 0
}

New-Item -ItemType Directory -Force -Path $Dst | Out-Null
$stamp = Get-Date -Format "yyyy-MM-dd"
$repos = $Roots | ForEach-Object { Find-Repos $_ } | Sort-Object -Unique

foreach ($repo in $repos) {
  $ahead = Get-UnpushedCount $repo
  if ($ahead -eq 0) { continue }                              # nothing unique -> skip

  $out = Join-Path $Dst ("{0}-{1}.bundle" -f (Split-Path -Leaf $repo), $stamp)
  if ($DryRun) {
    Write-Host ("would bundle {0} commit(s): {1} -> {2}" -f $ahead, $repo, $out)
    continue
  }
  & git -C $repo bundle create $out --branches --not --remotes
  Write-Host ("bundled {0} commit(s): {1} -> {2}" -f $ahead, $repo, $out)
}
