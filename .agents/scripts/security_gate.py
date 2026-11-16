import sys
import json
import re

def main():
    try:
        raw = sys.stdin.read()
        if not raw:
            sys.exit(0)
        data = json.loads(raw)
    except Exception:
        sys.exit(0)
    
    tool = data.get("tool", "")
    args = data.get("arguments", {})
    
    if tool == "run_command":
        cmd = args.get("CommandLine", "").strip()
        
        # Padroes destrutivos que podem apagar o projeto ou repositorio
        forbidden_patterns = [
            r"git\s+reset\s+--hard",
            r"git\s+clean\s+-f",
            r"(Remove-Item|rmdir|del|rm)\s+.*(\.git|placa_fechamento\.kicad_pro|GEMINI\.md|PROJECT_MEMORY\.md)",
            r"format\s+[a-zA-Z]:",
        ]
        
        for pattern in forbidden_patterns:
            if re.search(pattern, cmd, re.IGNORECASE):
                print(f"[SECURITY GATE] Comando potencialmente destrutivo bloqueado preventivamente: '{cmd}'.", file=sys.stderr)
                sys.exit(2)
                
    sys.exit(0)

if __name__ == "__main__":
    main()
