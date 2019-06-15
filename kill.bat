@echo off
FOR /F "tokens=5 delims= " %%P IN ('netstat -a -n -o ^| findstr :1234') DO TaskKill.exe /PID %%P /F >nul 2>&1