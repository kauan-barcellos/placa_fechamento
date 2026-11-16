# Script de Autodiagnostico do Ambiente KiCad 10.0 & Antigravity
# Executa validacoes rapidas dos componentes de infraestrutura de hardware

$ErrorActionPreference = "Continue"

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "  Autodiagnostico do Ambiente - Projeto placa_fechamento" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan

$allOk = $true

# 1. KiCad CLI
$kicadCli = "C:\Users\kauam.barcellos\AppData\Local\Programs\KiCad\10.0\bin\kicad-cli.exe"
if (-not (Test-Path $kicadCli)) {
    $cmd = Get-Command kicad-cli -ErrorAction SilentlyContinue
    if ($cmd) { $kicadCli = $cmd.Source }
}

if (Test-Path $kicadCli) {
    $ver = & $kicadCli --version 2>&1
    Write-Host "[OK] KiCad CLI: $ver" -ForegroundColor Green
} else {
    Write-Host "[ERRO] KiCad CLI nao encontrado." -ForegroundColor Red
    $allOk = $false
}

# 2. Python VirtualEnv do MCP
$venvPy = "C:\AI_Tools\KiCAD-MCP-Server\venv\Scripts\python.exe"
if (Test-Path $venvPy) {
    $pyVer = & $venvPy --version 2>&1
    Write-Host "[OK] Python MCP VirtualEnv: $pyVer ($venvPy)" -ForegroundColor Green
} else {
    Write-Host "[ERRO] Python VirtualEnv nao encontrado em: $venvPy" -ForegroundColor Red
    $allOk = $false
}

# 3. Banco de Dados SQLite da JLCPCB
$dbPath = "C:\Users\kauam.barcellos\.kicad-mcp\data\jlcpcb_parts.db"
if (-not (Test-Path $dbPath)) {
    $dbPath = "C:\Users\kauam.barcellos\.kicad-mcp\jlcpcb_parts.db"
}
if (Test-Path $dbPath) {
    $dbSizeMB = [math]::Round((Get-Item $dbPath).Length / 1MB, 2)
    Write-Host "[OK] JLCPCB Database: Presente ($dbSizeMB MB em $dbPath)" -ForegroundColor Green
} else {
    Write-Host "[ERRO] Banco SQLite da JLCPCB nao encontrado em: $dbPath" -ForegroundColor Red
    $allOk = $false
}

# 4. Java 25 & FreeRouting JAR
$freeroutingJar = "C:\Users\kauam.barcellos\.kicad-mcp\freerouting.jar"
if (Test-Path $freeroutingJar) {
    Write-Host "[OK] FreeRouting JAR: Presente ($freeroutingJar)" -ForegroundColor Green
} else {
    Write-Host "[AVISO] FreeRouting JAR nao encontrado em: $freeroutingJar" -ForegroundColor Yellow
}

$javaCmd = Get-Command java -ErrorAction SilentlyContinue
if ($javaCmd) {
    $javaVer = & java -version 2>&1 | Select-Object -First 1
    Write-Host "[OK] Java Runtime: $javaVer" -ForegroundColor Green
} else {
    Write-Host "[AVISO] Java nao encontrado no PATH do sistema." -ForegroundColor Yellow
}

# 5. Git & Template de Commit em pt-BR
$commitTemplate = git config --get commit.template
if ($commitTemplate -eq ".gitmessage.txt" -and (Test-Path ".gitmessage.txt")) {
    Write-Host "[OK] Git Commit Template: Configurado em pt-BR ($commitTemplate)" -ForegroundColor Green
} else {
    Write-Host "[AVISO] Git Commit Template nao configurado ou arquivo ausente." -ForegroundColor Yellow
}

$gitBranch = git rev-parse --abbrev-ref HEAD 2>&1
Write-Host "[OK] Git Branch Ativa: $gitBranch" -ForegroundColor Green

Write-Host "----------------------------------------------------------------" -ForegroundColor Cyan
if ($allOk) {
    Write-Host "Status Geral: AMBIENTE 100% OPERACIONAL E HOMOLOGADO." -ForegroundColor Green
} else {
    Write-Host "Status Geral: PENDENCIAS IDENTIFICADAS ACIMA." -ForegroundColor Red
}
Write-Host "================================================================" -ForegroundColor Cyan
