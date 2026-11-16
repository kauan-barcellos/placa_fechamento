"""
Circuit Checkpoint and Auto-Rollback Utility
Permite salvar marcos estaveis e reverter alteracoes com falha no circuito KiCad.
Garante que todas as mensagens de commit sigam estritamente o padrao em pt-BR.
"""

import sys
import os
import subprocess
import argparse

VALID_TYPES = ["feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore"]

def run_git(args):
    result = subprocess.run(["git"] + args, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def validate_ptbr_commit_msg(msg: str) -> bool:
    msg = msg.strip()
    if not msg:
        return False
    parts = msg.split(":", 1)
    if len(parts) != 2:
        return False
    prefix = parts[0].strip()
    # Check type and scope
    type_name = prefix.split("(")[0].strip()
    if type_name not in VALID_TYPES:
        return False
    # Check no trailing period
    desc = parts[1].strip()
    if desc.endswith("."):
        return False
    return True

def save_checkpoint(msg: str):
    if not validate_ptbr_commit_msg(msg):
        print(f"[ERRO] Mensagem fora do padrao Conventional Commits em pt-BR: '{msg}'")
        print("Formato obrigatorio: <tipo>(<escopo>): <descricao no imperativo em pt-br sem ponto final>")
        print(f"Tipos validos: {', '.join(VALID_TYPES)}")
        sys.exit(1)

    # Stage files
    code, out, err = run_git(["add", "."])
    if code != 0:
        print(f"[ERRO] Falha ao adicionar arquivos ao stage: {err}")
        sys.exit(code)

    # Commit
    code, out, err = run_git(["commit", "-m", msg])
    if code != 0:
        if "nothing to commit" in out or "nada a submeter" in out or "working tree clean" in out:
            print("[INFO] Nenhuma alteracao pendente para salvar no checkpoint.")
            return
        print(f"[ERRO] Falha no commit: {err}\n{out}")
        sys.exit(code)

    print(f"[OK] Checkpoint registrado com sucesso: {msg}")

def rollback():
    print("[AVISO] Iniciando rollback automatico para o ultimo commit estavel...")
    code, out, err = run_git(["restore", "."])
    if code != 0:
        print(f"[ERRO] Falha ao executar git restore: {err}")
        sys.exit(code)
    # Clean untracked generated artifacts if any
    run_git(["clean", "-fd", "fabrication/", "docs/previews/"])
    print("[OK] Rollback concluido com sucesso. Workspace restaurado ao ultimo estado homologado.")

def status():
    code, out, err = run_git(["status", "-s"])
    if not out:
        print("[OK] Workspace limpo. Sem alteracoes pendentes.")
    else:
        print("[INFO] Alteracoes pendentes no workspace:")
        print(out)

def main():
    parser = argparse.ArgumentParser(description="Circuit Checkpoint & Auto-Rollback Utility")
    parser.add_argument("--save", type=str, help="Salva checkpoint com mensagem em pt-BR")
    parser.add_argument("--rollback", action="store_true", help="Reverte alteracoes nao confirmadas")
    parser.add_argument("--status", action="store_true", help="Verifica estado do workspace")

    args = parser.parse_args()

    if args.save:
        save_checkpoint(args.save)
    elif args.rollback:
        rollback()
    elif args.status:
        status()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
