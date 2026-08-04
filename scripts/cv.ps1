# cv.ps1 - "Claude on vmi". Dispatch a task to the 48GB VPS to save local RAM.
#
# Usage:
#   cv "summarize the README in /root/work/foo"
#   cv -Interactive                    # drop into a live claude session on vmi
#   cv -Resume <session-id>            # resume an existing vmi claude session
#   cv -Cwd /root/calaf "do X"         # set vmi working directory for this run
#   cv -Tail                           # tail the most recent cv log on vmi
#   cv -Logs                           # list recent cv logs on vmi
#
# How it works:
#   - Pipes the prompt over SSH to /root/bin/cv-run on vmi.
#   - cv-run logs the full transcript to /root/.claude/logs/cv/cv-<ts>.log.
#   - Claude runs on vmi (47GB RAM available); only output streams to your terminal.
#   - Logs are pulled back to ~/.claude/from-vmi/logs/ by ClaudeSyncFromVmi (every 30 min).

param(
  [Parameter(Position=0, ValueFromRemainingArguments=$true)]
  [string[]] $Prompt,

  [switch] $Interactive,
  [string] $Resume,
  [string] $Cwd = "/root/work",
  [switch] $Tail,
  [switch] $Logs,
  [switch] $Help
)

function Show-Help {
  Write-Host ""
  Write-Host "cv - run Claude Code on vmi VPS (47GB RAM) instead of locally" -ForegroundColor Cyan
  Write-Host ""
  Write-Host "  cv `"<task>`"               run a one-shot task on vmi"
  Write-Host "  cv -Interactive          interactive claude session on vmi"
  Write-Host "  cv -Resume <session-id>  resume a vmi claude session"
  Write-Host "  cv -Cwd /root/calaf ...  set vmi working dir (default: /root/work)"
  Write-Host "  cv -Tail                 tail most recent cv log on vmi"
  Write-Host "  cv -Logs                 list recent cv logs on vmi"
  Write-Host "  cv -Help                 this message"
  Write-Host ""
}

if ($Help) { Show-Help; return }

if ($Tail) {
  ssh vmi "ls -t /root/.claude/logs/cv/*.log 2>/dev/null | head -1 | xargs -r tail -n 200 -f"
  return
}

if ($Logs) {
  ssh vmi "ls -lhtr /root/.claude/logs/cv/ | tail -20"
  return
}

if ($Interactive) {
  Write-Host "[cv] interactive claude on vmi (cwd=$Cwd)" -ForegroundColor Yellow
  ssh -t vmi "cd '$Cwd' && claude"
  return
}

if ($Resume) {
  Write-Host "[cv] resuming vmi session $Resume (cwd=$Cwd)" -ForegroundColor Yellow
  ssh -t vmi "cd '$Cwd' && claude --resume $Resume"
  return
}

if (-not $Prompt) { Show-Help; return }

$task = ($Prompt -join ' ').Trim()
if ([string]::IsNullOrWhiteSpace($task)) { Show-Help; return }

Write-Host "[cv] dispatching to vmi (cwd=$Cwd, $($task.Length) chars)" -ForegroundColor Yellow
$task | ssh vmi "CV_CWD='$Cwd' /root/bin/cv-run"
