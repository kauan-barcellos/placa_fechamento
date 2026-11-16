---
name: git-hygiene-and-secrets
description: >-
  Auditor de higiene de repositorio Git e prevencao de vazamento de segredos e arquivos temporarios do KiCad.
  Use antes de cada commit e push para garantir que nenhuma chave de API, arquivo de lock ou backup polua o historico.
---

# Git Repository Hygiene & Secret Protection Protocol

Esta skill orienta a auditoria preventiva do repositório Git, impedindo que arquivos transitórios do KiCad ou dados sensíveis (tokens, chaves de API, senhas) sejam incluídos no histórico versionado.

---

## 1. Verificação de Arquivos Temporários do KiCad

Antes de qualquer `git add`, confirme que os seguintes arquivos foram ignorados pelo `.gitignore`:
- `*.kicad_prl` (preferências locais de visualização da interface gráfica do KiCad).
- `*.kicad_pcb-bak`, `*.kicad_sch-bak`, `*-bak` (arquivos automáticos de backup).
- `*.lck`, `*.tmp` (arquivos de trava de processo do KiCad).
- Relatórios intermediários brutos (`*.rpt`, `*_violations.json`).

---

## 2. Varredura Silenciosa de Segredos e Chaves de API

O agente NUNCA deve comitar arquivos contendo:
1. Chaves de API da JLCPCB (`JLCPCB_APP_ID`, `JLCPCB_API_KEY`, `JLCPCB_API_SECRET`).
2. Tokens do GitHub (`ghp_*`, `github_pat_*`).
3. Chaves privadas (`*.pem`, `*.key`, `id_rsa`).
4. Arquivos de ambiente locais (`.env`, `.env.local`).

Caso seja detectada qualquer string com padrão de chave ou credencial em um arquivo a ser versionado, a execução do commit DEVE ser abortada imediatamente e o usuário notificado para sanitização.
