#!/usr/bin/env python3
"""
Gera automaticamente arquivos de preview visual da PCB e do Esquemático
utilizando estritamente a CLI nativa (kicad-cli) com timeouts rigidos.
NUNCA importa modulos graficos ou GUI do KiCad (elimina assert PgmOrNull).
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
DOCS_PREVIEWS = WORKSPACE / "docs" / "previews"
DOCS_PREVIEWS.mkdir(parents=True, exist_ok=True)

DEFAULT_TIMEOUT_SEC = 15

def find_kicad_cli():
    # 1. PATH do sistema
    cmd = shutil.which("kicad-cli")
    if cmd:
        return cmd

    # 2. Caminhos padrao no Windows
    candidates = [
        r"C:\Users\kauam.barcellos\AppData\Local\Programs\KiCad\10.0\bin\kicad-cli.exe",
        r"C:\Program Files\KiCad\10.0\bin\kicad-cli.exe",
        r"C:\Program Files\KiCad\9.0\bin\kicad-cli.exe",
        r"C:\Program Files\KiCad\8.0\bin\kicad-cli.exe",
    ]
    for path in candidates:
        if os.path.isfile(path):
            return path
    return None

KICAD_CLI = find_kicad_cli()
BOARD_FILE = WORKSPACE / "placa_fechamento.kicad_pcb"
SCH_FILE = WORKSPACE / "placa_fechamento.kicad_sch"

def run_headless_cmd(cmd, desc, timeout_sec=DEFAULT_TIMEOUT_SEC):
    try:
        res = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            encoding="utf-8",
            errors="replace"
        )
        if res.returncode == 0:
            print(f"[OK] {desc}")
            return True
        else:
            err = res.stderr.strip()[:300] if res.stderr else res.stdout.strip()[:300]
            print(f"[AVISO] {desc} falhou (codigo {res.returncode}): {err}")
            return False
    except subprocess.TimeoutExpired:
        print(f"[ERRO] Timeout ({timeout_sec}s) expirado para: {desc}. Processo cancelado.")
        return False
    except Exception as exc:
        print(f"[ERRO] Falha ao executar {desc}: {exc}")
        return False

def generate_svg_previews():
    if not KICAD_CLI or not os.path.isfile(KICAD_CLI):
        print(f"[ERRO] kicad-cli nao localizado para renderizacao.")
        return False

    success = True

    # 1. Preview do Esquemático
    if SCH_FILE.is_file() and SCH_FILE.stat().st_size > 0:
        sch_out_dir = DOCS_PREVIEWS / "schematic"
        sch_out_dir.mkdir(parents=True, exist_ok=True)
        cmd = [
            KICAD_CLI, "sch", "export", "svg",
            "-o", str(sch_out_dir),
            str(SCH_FILE)
        ]
        if not run_headless_cmd(cmd, "SVG do Esquematico"):
            success = False

    # 2. Preview da PCB - Camada Superior (Top)
    if BOARD_FILE.is_file() and BOARD_FILE.stat().st_size > 0:
        out_top = DOCS_PREVIEWS / "pcb_top.svg"
        cmd_top = [
            KICAD_CLI, "pcb", "export", "svg",
            "-o", str(out_top),
            "--layers", "F.Cu,F.Silkscreen,F.Mask,Edge.Cuts",
            "--fit-page-to-board",
            "--exclude-drawing-sheet",
            str(BOARD_FILE)
        ]
        if not run_headless_cmd(cmd_top, "SVG da PCB (F.Cu)"):
            success = False

        # 3. Preview da PCB - Camada Inferior (Bottom)
        out_bot = DOCS_PREVIEWS / "pcb_bottom.svg"
        cmd_bot = [
            KICAD_CLI, "pcb", "export", "svg",
            "-o", str(out_bot),
            "--layers", "B.Cu,B.Silkscreen,B.Mask,Edge.Cuts",
            "--fit-page-to-board",
            "--exclude-drawing-sheet",
            "--mirror",
            str(BOARD_FILE)
        ]
        if not run_headless_cmd(cmd_bot, "SVG da PCB (B.Cu)"):
            success = False

    return success

if __name__ == "__main__":
    print("=" * 60)
    print("Executando renderizacao visual headless (kicad-cli)...")
    print(f"Diretorio de saida: {DOCS_PREVIEWS}")
    print("=" * 60)
    ok = generate_svg_previews()
    if ok:
        print("[SUCESSO] Previews gerados com seguranca (sem travas de GUI).")
    else:
        print("[CONCLUIDO COM AVISOS] Verifique as mensagens acima.")
