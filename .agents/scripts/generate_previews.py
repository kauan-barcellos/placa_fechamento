#!/usr/bin/env python3
"""
Gera automaticamente arquivos de preview visual da PCB e do Esquemático
utilizando estritamente a CLI nativa (kicad-cli) com timeouts rígidos.
Localiza dinamicamente os arquivos *.kicad_pcb e *.kicad_sch no projeto.
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
    cmd = shutil.which("kicad-cli")
    if cmd:
        return cmd
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

def find_project_files():
    pcb_files = list(WORKSPACE.glob("*.kicad_pcb"))
    sch_files = list(WORKSPACE.glob("*.kicad_sch"))
    board = pcb_files[0] if pcb_files else None
    sch = sch_files[0] if sch_files else None
    return board, sch

KICAD_CLI = find_kicad_cli()
BOARD_FILE, SCH_FILE = find_project_files()

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
    if SCH_FILE and SCH_FILE.is_file() and SCH_FILE.stat().st_size > 0:
        sch_out_dir = DOCS_PREVIEWS / "schematic"
        sch_out_dir.mkdir(parents=True, exist_ok=True)
        cmd = [
            KICAD_CLI, "sch", "export", "svg",
            "-o", str(sch_out_dir),
            str(SCH_FILE)
        ]
        if not run_headless_cmd(cmd, f"SVG do Esquematico ({SCH_FILE.name})"):
            success = False

    # 2. Preview da PCB - Camada Superior (Top)
    if BOARD_FILE and BOARD_FILE.is_file() and BOARD_FILE.stat().st_size > 0:
        out_top = DOCS_PREVIEWS / "pcb_top.svg"
        cmd_top = [
            KICAD_CLI, "pcb", "export", "svg",
            "-o", str(out_top),
            "--layers", "F.Cu,F.Silkscreen,F.Mask,Edge.Cuts",
            "--fit-page-to-board",
            "--exclude-drawing-sheet",
            str(BOARD_FILE)
        ]
        if not run_headless_cmd(cmd_top, f"SVG da PCB Top ({BOARD_FILE.name})"):
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
        if not run_headless_cmd(cmd_bot, f"SVG da PCB Bottom ({BOARD_FILE.name})"):
            success = False

    return success

if __name__ == "__main__":
    print("=" * 60)
    print("Executando renderizacao visual headless (kicad-cli)...")
    print(f"Diretorio de saida: {DOCS_PREVIEWS}")
    if BOARD_FILE:
        print(f"Placa detectada: {BOARD_FILE.name}")
    if SCH_FILE:
        print(f"Esquematico detectado: {SCH_FILE.name}")
    print("=" * 60)
    ok = generate_svg_previews()
    if ok:
        print("[SUCESSO] Previews gerados com seguranca (sem travas de GUI).")
    else:
        print("[CONCLUIDO COM AVISOS] Verifique as mensagens acima.")
