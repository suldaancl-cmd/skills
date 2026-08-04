@echo off
REM Hourly second-brain refresh: pull vmi chats -> convert -> rebuild Brain/.
REM Resilient: if vmi is unreachable, still rebuilds from local + previously-pulled data.
setlocal

REM 1. Pull vmi Claude transcripts to a temp tarball (byte-safe; no pipe corruption)
ssh -o ConnectTimeout=15 -o BatchMode=yes vmi "cd /root/.claude/projects && find . -name '*.jsonl' -print0 | tar --null -czf - -T -" > "%TEMP%\vmi_sessions.tgz" 2>nul
if %ERRORLEVEL%==0 (
  if not exist "C:\Users\user\.claude\from-vmi\projects" mkdir "C:\Users\user\.claude\from-vmi\projects"
  tar xzf "%TEMP%\vmi_sessions.tgz" -C "C:\Users\user\.claude\from-vmi\projects" 2>nul
  del "%TEMP%\vmi_sessions.tgz" 2>nul
)

REM 2. Convert any pulled vmi transcripts into vault Sessions/vmi--*/
python "C:\Users\user\.claude\scripts\convert_vmi_sessions.py"

REM 3. Rebuild the connected Brain/ index (skills + links + reports + chats)
python "C:\Users\user\.claude\scripts\build_second_brain.py"

endlocal
