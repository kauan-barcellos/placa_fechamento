---
name: systematic-debugging
description: >-
  Protocolo de depuração sistemática em 4 fases para erros de ERC, DRC, montagem e scripts.
  Use sempre que encontrar um erro de projeto ou falha de ferramenta para diagnosticar a causa raiz antes de modificar arquivos.
---

# Systematic & Phase-Gated Debugging Protocol

Esta skill proíbe o comportamento não-determinístico de "tentativa e erro desordenada" em falhas de hardware ou scripts, impondo um método científico de 4 fases para resolução de qualquer erro de ERC, DRC ou compilação.

---

## As 4 Fases Obrigatórias de Resolução

```
[1. Reproduzir Erro] ──► [2. Analisar Causa Raiz (5 Whys)] ──► [3. Formular Hipótese] ──► [4. Aplicar e Validar]
```

### Fase 1: Reprodução Determinística
- Nunca altere arquivos imediatamente após uma falha.
- Isole a mensagem exata de erro retornada pela ferramenta (ex: `ERC: Pin connected to other pins, but not driven by any pin` no nó `+3.3V` ou `DRC: Clearance violation between track and pad`).
- Confirme se o erro é reproduzível de forma consistente.

### Fase 2: Análise da Causa Raiz (Técnica dos "5 Porquês")
- Pergunte a causa física ou sintática real:
  - *Exemplo:* "Por que o DRC acusou violação de folga?" -> Porque a trilha passou a 0.12 mm do pad.
  - "Por que passou a 0.12 mm?" -> Porque a netclass atribuída tinha clearance configurado como padrão geral (0.15 mm), mas o roteamento manual fez curva viva a 90°.
  - "Causa Raiz:" O nó requer curva a 45° ou o ajuste da folga de netclass para componentes de pitch fino.

### Fase 3: Formulação da Hipótese Técnica
- Proponha uma única correção cirúrgica baseada na causa raiz.
- Declare o efeito esperado antes de executar qualquer comando.

### Fase 4: Aplicação Cirúrgica e Validação de Efeitos Colaterais
- Aplique o ajuste pontual (sem reescrever blocos alheios).
- Execute imediatamente a ferramenta de teste (`run_erc` ou `run_drc`).
- Verifique se o erro desapareceu E se a contagem total de outros erros não aumentou.
- Se o erro persistir após 2 tentativas com hipóteses fundamentadas, acione o rollback de segurança via `circuit_checkpoint.py --rollback`.
