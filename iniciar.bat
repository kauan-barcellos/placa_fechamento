@echo off
setlocal enabledelayedexpansion
title Assistente Antigravity - Placa Fechamento (KiCad 10.0)

:: Navega diretamente para o diretorio do script (raiz do projeto)
cd /d "%~dp0"

echo ================================================================
echo   Assistente de Hardware KiCad 10.0 - Projeto placa_fechamento
echo   Diretorio: %CD%
echo ================================================================
echo.

:: Localiza o executavel do agy
set "AGY_CMD=agy"
where agy >nul 2>nul
if %errorlevel% neq 0 (
    if exist "%LOCALAPPDATA%\agy\bin\agy.exe" (
        set "AGY_CMD=%LOCALAPPDATA%\agy\bin\agy.exe"
    ) else (
        echo [ERRO] Executavel 'agy' nao foi encontrado no PATH nem em AppData.
        echo Pressione qualquer tecla para sair...
        pause >nul
        exit /b 1
    )
)

:: Id da conversa atual registrada
set "CURRENT_CONV_ID=33e3bc8a-8590-4080-8888-8645fb3af79c"

echo [1/2] Conectando ao ambiente do projeto...
echo.

:: Tenta continuar a sessao mais recente deste diretorio (-c)
"%AGY_CMD%" -c

:: Caso a sessao nao seja encontrada pelo -c, tenta retomar pelo ID exato
if %errorlevel% neq 0 (
    echo.
    echo Retomando conversa pelo ID de registro (%CURRENT_CONV_ID%)...
    "%AGY_CMD%" --conversation %CURRENT_CONV_ID%
)

if %errorlevel% neq 0 (
    echo.
    echo Iniciando nova sessao no diretorio do projeto...
    "%AGY_CMD%"
)

pause
