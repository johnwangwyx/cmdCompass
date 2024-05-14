@echo off
setlocal
set Path=%~dp0;%Path%
if not "%GROFF_BIN_PATH%" == "" set Path=%GROFF_BIN_PATH%;%Path%
eqn -Tascii %*
endlocal
