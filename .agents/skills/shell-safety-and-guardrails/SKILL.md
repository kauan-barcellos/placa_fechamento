---
name: shell-safety-and-guardrails
description: >-
  Diretrizes de execucao deterministica, segura e estritamente headless de comandos no terminal.
  Use ao formular comandos de shell para evitar travamentos por prompts interativos, loops infinitos ou comandos destrutivos.
---

# Shell Execution Safety & Headless Guardrails

Esta skill previne travamentos de sessão, bloqueios silenciosos de processos e danos ao sistema de arquivos ao executar comandos no terminal do assistente.

---

## 1. Regras Mandatórias de Formatação de Comandos

1. **Modo Estritamente Não-Interativo (Headless):**
   - É expressamente proibido rodar comandos que aguardem interação via teclado (`stdin`).
   - Todo instalador ou ferramenta deve utilizar flags de confirmação automática:
     - `winget install ... --accept-source-agreements --accept-package-agreements`
     - `npm install ... --yes`
     - `git commit -m "..."` (NUNCA disparar `git commit` sem `-m`, pois abre o editor interativo).
2. **Timeouts Obrigatórios:**
   - Em scripts Python ou chamadas de automação, todo `subprocess.run` ou `Popen` DEVE ter parâmetro `timeout` explícito (recomendado 15 a 30 segundos).
3. **Comandos Destrutivos Bloqueados:**
   - Proibido executar comandos com recursão irrestrita de deleção (`rmdir /s /q C:\`, `rm -rf /`, `del /s *.*`).
   - Limpezas devem ser restritas ao diretório de saída alvo (`docs/previews/`, `fabrication/`).
4. **Caminhos com Espaços e Aspas no Windows:**
   - Sempre envolver caminhos contendo espaços em aspas duplas (ex: `"$env:LOCALAPPDATA\Programs\..."`).
   - Preferir a passagem de argumentos como lista (`["arg1", "arg2"]`) em vez de concatenação crua de strings para prevenir injeção de comandos.
