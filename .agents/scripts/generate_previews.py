#!/usr/bin/env python3
"""
Gera automaticamente arquivos de preview visual da PCB e do Esquemático
para inspeção rápida no navegador e no chat.
"""

import os
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
DOCS_PREVIEWS = WORKSPACE / "docs" / "previews"
DOCS_PREVIEWS.mkdir(parents=True, exist_ok=True)

KICAD_CLI = r"C:\Users\kauam.barcellos\AppData\Local\Programs\KiCad\10.0\bin\kicad-cli.exe"
BOARD_FILE = WORKSPACE / "placa_fechamento.kicad_pcb"
SCH_FILE = WORKSPACE / "placa_fechamento.kicad_sch"

def run_cmd(cmd, desc):
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"[OK] {desc}")
            return True
        else:
            print(f"[AVISO] {desc} falhou: {res.stderr[:200]}")
            return False
    except Exception as exc:
        print(f"[ERRO] {desc}: {exc}")
        return False

def generate_svgs():
    if not os.path.isfile(KICAD_CLI):
        print(f"[ERRO] kicad-cli nao encontrado em: {KICAD_CLI}")
        return

    # 1. Esquemático
    if SCH_FILE.is_file():
        out_sch = DOCS_PREVIEWS / "schematic.svg"
        run_cmd([
            KICAD_CLI, "sch", "export", "svg",
            "-o", str(out_sch),
            str(SCH_FILE)
        ], "Exportacao SVG do Esquetamico")

    # 2. PCB Top Layer
    if BOARD_FILE.is_file():
        out_top = DOCS_PREVIEWS / "pcb_top.svg"
        run_cmd([
            KICAD_CLI, "pcb", "export", "svg",
            "-o", str(out_top),
            "--layers", "F.Cu,F.Silkscreen,F.Mask,Edge.Cuts",
            "--fit-page-to-board",
            "--exclude-drawing-sheet",
            str(BOARD_FILE)
        ], "Exportacao SVG da PCB (Top)")

        # 3. PCB Bottom Layer
        out_bot = DOCS_PREVIEWS / "pcb_bottom.svg"
        run_cmd([
            KICAD_CLI, "pcb", "export", "svg",
            "-o", str(out_bot),
            "--layers", "B.Cu,B.Silkscreen,B.Mask,Edge.Cuts",
            "--fit-page-to-board",
            "--exclude-drawing-sheet",
            "--mirror",
            str(BOARD_FILE)
        ], "Exportacao SVG da PCB (Bottom)")

def generate_ibom():
    try:
        from InteractiveHtmlBom.generate_interactive_bom import main as ibom_main
        sys.argv = [
            "generate_interactive_bom",
            "--dest-dir", str(DOCS_PREVIEWS),
            "--name-format", "ibom",
            "--no-browser",
            str(BOARD_FILE)
        ]
        ibom_main()
        print("[OK] InteractiveHtmlBom gerado em docs/previews/ibom.html")
    except Exception as exc:
        print(f"[INFO] iBOM: {exc}")

if __name__ == "__main__":
    print("=" * 60)
    print("Gerando previews visuais da placa...")
    print("=" * 60)
    generate_svgs()
    generate_ibom()
    print("Previews concluidos em:", DOCS_PREVIEWS)
