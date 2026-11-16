@echo off
setlocal
title Autodiagnostico do Ambiente KiCad 10.0 - placa_fechamento
cd /d "%~dp0"

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0.agents\scripts\check_env.ps1"

echo.
pause
