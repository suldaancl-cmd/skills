' Run any command line completely hidden (no flashing console).
' Usage: wscript.exe run-hidden.vbs "C:\path\to\script.bat" [args...]
Option Explicit
Dim shell, cmd, i
Set shell = CreateObject("WScript.Shell")
cmd = ""
For i = 0 To WScript.Arguments.Count - 1
  cmd = cmd & """" & WScript.Arguments(i) & """ "
Next
shell.Run cmd, 0, False
